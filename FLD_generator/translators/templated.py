from abc import abstractmethod
from typing import List, Dict, Optional, Tuple, Iterator, Any, Set, Callable, Union, Generator, Iterator
from collections import OrderedDict, defaultdict
import statistics
import re
import random
import logging
from pprint import pformat, pprint
from functools import lru_cache
import math
from copy import deepcopy, copy

from FLD_generator.settings import DEFAULT_CACHE_SIZE
import timeout_decorator
from FLD_generator.formula import Formula, PREDICATES, CONSTANTS, remove_outer_brace
from FLD_generator.word_banks.base import WordBank, ATTR
from FLD_generator.interpretation import (
    generate_mappings_from_formula,
    generate_mappings_from_predicates_and_constants,
    interpret_formula,
    formula_can_not_be_identical_to,
)
from FLD_generator.word_banks import POS
from FLD_generator.utils import (
    compress,
    decompress,
    make_pretty_msg,
    weighted_chained_sampling,
    generate_combinations_from_generators,
    shuffle,
    RandomCycle,
    LRUCache,
)
from FLD_generator.knowledge_banks.base import KnowledgeBankBase
from .base import (
    Translator,
    TranslationNotFoundError,
    calc_formula_specificity,
    Phrase,
    PredicatePhrase,
    ConstantPhrase,
)
import line_profiling

logger = logging.getLogger(__name__)

_SENTENCE_TRANSLATION_PREFIX = 'sentence'

# _LOGS_FOR_DEBUG = True
_LOGS_FOR_DEBUG = False

# _PREFER_CONDITION_MATCHING_BRANCHES = True   # SLOW!
_PREFER_CONDITION_MATCHING_BRANCHES = False

# leaf nl to generator such as "is", "are".
# _LEAF_NL_GENERATOR_CACHE = LRUCache(DEFAULT_CACHE_SIZE)   # LRUCache is slower!
_LEAF_NL_GENERATOR_CACHE = {}

# _UNCONDITIONED_VOLUME_CACHE = LRUCache(DEFAULT_CACHE_SIZE)  # LRUCache is slower!
_UNCONDITIONED_VOLUME_CACHE = {}

# For each nl, we store "possible" conditions.
# "Possible" means that we can have other conditions not stored in the cache.
_POSSIBLE_CONDITIONS_CACHE: Dict[str, Set['_PosFormConditionSet']] = defaultdict(set)


class _PosFormConditionSet(set):

    def __new__(cls, elems: Iterator[Tuple[str, Optional[POS], Optional[str]]]):
        keys = [elem[0] for elem in elems]
        key_set = set(keys)
        if len(key_set) < len(keys):
            raise Exception(f'Duplicated condition for found in {elems}')
        unique_elems = set(elems)
        return super().__new__(cls, unique_elems)


TemplatedNLAndCondition = Iterator[Tuple[str, _PosFormConditionSet]]


# We place this functions in global domain just to be measured by the line-profiler.
@profile
def generate_resolved_template_combinations(parent_translator: 'TemplatedTranslator',
                                            resolved_template_generators: List[Generator],
                                            condition: _PosFormConditionSet,
                                            templated_nl: str,
                                            templates: List[str]) -> Iterator:
    for combination in generate_combinations_from_generators(resolved_template_generators):
        updated_condition = condition.copy()
        resolved_nl = templated_nl

        for template, (resolved_template, new_condition) in zip(templates, combination):
            resolved_nl = resolved_nl.replace(
                f'{parent_translator._TEMPLATE_BRACES[0]}{template}{parent_translator._TEMPLATE_BRACES[1]}',
                resolved_template,
                1,
            )
            updated_condition = parent_translator._merge_condition(updated_condition, new_condition)

        yield resolved_nl, updated_condition


# We place this trivial function just to be symmetric with the above.
@profile
def generate_weighted_chained_samples(iterators: List[Iterator], weights) -> Iterator:
    for resolved_templated_nl, condition in weighted_chained_sampling(iterators, weights):
        yield resolved_templated_nl, condition


class ResolvedTemplateGenerator:

    # SLOW: Called many many times
    @profile
    def __init__(self,
                 parent_translator: 'TemplatedTranslator',
                 template: str,
                 ancestor_templated_nls,
                 constraint_interpret_mapping,
                 constraint_pos_mapping,
                 constraint_push_mapping,
                 block_shuffle,
                 volume_to_weight,
                 compute_volume,
                 check_condition,
                 log_indent):
        self.ancestor_templated_nls = ancestor_templated_nls
        self.constraint_interpret_mapping = constraint_interpret_mapping
        self.constraint_pos_mapping = constraint_pos_mapping
        self.constraint_push_mapping = constraint_push_mapping
        self.block_shuffle = block_shuffle
        self.volume_to_weight = volume_to_weight
        self._compute_volume = compute_volume
        self.check_condition = check_condition
        self.log_indent = log_indent

        self._template = template
        self._parent_translator = parent_translator

        self._volume_cache = _UNCONDITIONED_VOLUME_CACHE
        self._volume_cache_key = (id(self.volume_to_weight), tuple(ancestor_templated_nls), self._template)

    @profile
    def __call__(self) -> Iterator[TemplatedNLAndCondition]:
        return self._make_conditioned_iterator()

    @profile
    def _make_conditioned_iterator(self) -> Iterator[TemplatedNLAndCondition]:
        """ Make an iterator that returns resolved template items that matches the coditions.

        This function invokes recursive computation, via calling compute_unconditioned_volume().
        Therefore, the recursion will stop if the compute_unconditioned_volume() does not invoke future recursion,
        i.e., when self._compute_volume is False or the volume is in the cache.
        """
        return self._parent_translator._make_sampler_from_template(
            self._template,
            self.ancestor_templated_nls,
            constraint_interpret_mapping=self.constraint_interpret_mapping,
            constraint_pos_mapping=self.constraint_pos_mapping,
            constraint_push_mapping=self.constraint_push_mapping,
            shuffle=self.block_shuffle,
            volume_to_weight=self.volume_to_weight,
            compute_volume=self._compute_volume,
            check_condition=self.check_condition,
            log_indent=self.log_indent + 4
        )[0]

    @profile
    # XXX: Adding the timeout decorator does not work due to the following reasons:
    # (i) If we use use_signal=True, the program will hang up as the signal here interfere with the signal used by run_with_timeout_retry()
    # (ii) If we use use_signal=False, then the funtion will be executed in another process, which does not share the calculated volumes via _UNCONDITIONED_VOLUMES.
    # @timeout_decorator.timeout(0.01, use_signals=True, timeout_exception=VolumeCalculationTimeoutError)
    def compute_unconditioned_volume(self) -> int:
        """ Calculate the volume (i.e., the number of items) of the iterator without considering the conditions.

        This function invokes recursive computation if self._compute_volume is True and the volume is not in the cache.
        """

        if not self._compute_volume or self._volume_cache_key in self._volume_cache:
            return self._volume_cache.get(self._volume_cache_key, None)

        # The iterator created here can not be used for the sampling, as they may not meet the conditions.
        _, volume = self._parent_translator._make_sampler_from_template(
            self._template,

            # should include this to avoid infinite loop.
            self.ancestor_templated_nls,

            # should shuffle if specified to do random exploration on descendant branches to cache volumes of various branches.
            shuffle=self.block_shuffle,

            volume_to_weight=self.volume_to_weight,
            compute_volume=True,
            check_condition=False,
            log_indent=self.log_indent + 4
        )

        if volume is not None:
            self._volume_cache[self._volume_cache_key] = volume

        return volume


class TemplatedTranslator(Translator):

    _TEMPLATE_BRACES = ['<<', '>>']

    def __init__(self,
                 config_json: Dict[str, Dict],
                 word_bank: WordBank,
                 use_fixed_translation: bool,
                 reused_object_nouns_max_factor=0.0,
                 limit_vocab_size_per_type: Optional[int] = None,
                 # words_per_type=5000,
                 volume_to_weight: str = 'log10',
                 default_weight_factor_type='W_VOL__1.0',
                 do_translate_to_nl=True,
                 no_adj_verb_as_zeroary=False,
                 adj_verb_noun_ratio: Optional[List] = None,
                 knowledge_banks: Optional[List[KnowledgeBankBase]] = None,
                 log_stats=False):
        super().__init__(log_stats=log_stats)

        self._default_weight_factor_type = default_weight_factor_type
        self._two_layered_config = self._build_two_layered_config(config_json)

        self._load_words_by_pos_attrs_cache: Dict[Any, set] = {}
        self._load_words_by_pos_attrs_cache_interm: Dict[Any, set] = defaultdict(set)

        self._translations: Dict[str, List[Tuple[str, str]]] = self._two_layered_config[_SENTENCE_TRANSLATION_PREFIX]
        # sort by specificity
        self._translations = OrderedDict((
            (key, val)
            for key, val in sorted(self._translations.items(),
                                   key=lambda key_val: calc_formula_specificity(Formula(key_val[0])))[::-1]
        ))
        logger.debug(make_pretty_msg(title='loaded translations', boundary_level=0))
        for key, templated_nls in self._translations.items():
            logger.debug('translation key = "%s"', key)
            for templated_nl in templated_nls:
                logger.debug('    "%s"', templated_nl)

        # self.words_per_type = words_per_type

        self._word_bank = word_bank

        self.use_fixed_translation = use_fixed_translation
        self.reused_object_nouns_max_factor = reused_object_nouns_max_factor
        self._no_adj_verb_as_zeroary = no_adj_verb_as_zeroary
        self._zeroary_predicates, self._unary_predicates, self._constants = self._load_phrases(
            self._word_bank, adj_verb_noun_ratio=adj_verb_noun_ratio)
        if limit_vocab_size_per_type is not None:
            self._zeroary_predicates = self._sample(self._zeroary_predicates, limit_vocab_size_per_type)
            self._unary_predicates = self._sample(self._unary_predicates, limit_vocab_size_per_type)
            self._constants = self._sample(self._constants, limit_vocab_size_per_type)
        self._constant_set = set(self._constants)

        if volume_to_weight == 'linear':
            self._volume_to_weight_func = lambda volume: volume
        elif volume_to_weight == 'sqrt':
            self._volume_to_weight_func = lambda volume: (math.sqrt(volume) if volume > 0 else 0)
        elif volume_to_weight == 'logE':
            self._volume_to_weight_func = lambda volume: (1 + math.log(volume) if volume > 0 else 0)
        elif volume_to_weight == 'log10':
            self._volume_to_weight_func = lambda volume: (1 + math.log10(volume) if volume > 0 else 0)
        elif volume_to_weight == 'inv_linear':
            self._volume_to_weight_func = lambda volume: (1.0 / volume if volume > 0 else 0)
        elif volume_to_weight.startswith('pow-'):
            ind = float(volume_to_weight.split('-')[1])
            self._volume_to_weight_func = lambda volume: (math.pow(volume, ind) if volume > 0 else 0)
        else:
            raise ValueError()

        self._do_translate_to_nl = do_translate_to_nl

        self._knowledge_banks = knowledge_banks or []

    def _build_two_layered_config(self, config: Dict) -> Dict[str, Dict[str, List[Tuple[str, str]]]]:
        flat_config = self._completely_flatten_config(config)

        two_layered_config: Dict[str, Dict[str, List[str]]] = defaultdict(dict)
        for key, val in flat_config.items():
            if key.startswith('__'):
                logger.info('skip key "%s"', key)
                continue
            elif key.find('::') >= 0:
                prefix = '::'.join(key.split('::')[:-1])
                transl_key = key.split('::')[-1]
            else:
                prefix = 'others'
                transl_key = key
            if transl_key.startswith('__'):
                logger.info('skip key "%s"', key)
                continue
            two_layered_config[prefix][transl_key] = val
        return two_layered_config

    def _completely_flatten_config(self, config: Dict) -> Dict[str, List[Tuple[float, str]]]:
        flat_config = {}
        for key, val in config.items():
            if isinstance(val, list):
                children = []
                for child in val:
                    if isinstance(child, list):
                        if not len(child) == 2:
                            raise ValueError('invalid template {str(child)}')
                        children.append(tuple(child))
                    else:
                        if not isinstance(child, str):
                            raise ValueError('invalid template {str(child)}')
                        children.append((self._default_weight_factor_type, child))
                flat_config[key] = children

            elif isinstance(val, dict):
                for child_key, child_val in self._completely_flatten_config(val).items():
                    flat_config[f'{key}::{child_key}'] = child_val

            else:
                raise ValueError()

        return flat_config

    @profile
    def _load_phrases(self,
                      word_bank: WordBank,
                      adj_verb_noun_ratio: Optional[List[float]] = None,
                      # prioritize_form_abundant_words=False,
                      ) -> Tuple[Iterator[PredicatePhrase], Iterator[PredicatePhrase], List[ConstantPhrase]]:

        logger.info('loading nouns ...')
        intermediate_constant_noun_set = set(word_bank.get_intermediate_constant_words())

        event_nouns = [word
                       for word in self._load_words_by_pos_attrs(word_bank, pos=POS.NOUN)
                       if ATTR.can_be_event_noun in word_bank.get_attrs(word)]
        event_nouns = list(set(event_nouns) - intermediate_constant_noun_set)
        random.shuffle(event_nouns)

        entity_nouns = [word
                        for word in self._load_words_by_pos_attrs(word_bank, pos=POS.NOUN)
                        if ATTR.can_be_entity_noun in word_bank.get_attrs(word)]
        entity_nouns = list(set(entity_nouns) - intermediate_constant_noun_set)
        random.shuffle(entity_nouns)

        predicate_nouns = [word
                           for word in self._load_words_by_pos_attrs(word_bank, pos=POS.NOUN)
                           if ATTR.can_be_predicate_noun in word_bank.get_attrs(word)]
        predicate_nouns = list(set(predicate_nouns) - intermediate_constant_noun_set)

        logger.info('loading adjs ...')
        adjs = [word
                for word in self._load_words_by_pos_attrs(word_bank, pos=POS.ADJ)]
        random.shuffle(adjs)

        logger.info('loading intransitive_verbs ...')
        intransitive_verbs = [word
                              for word in self._load_words_by_pos_attrs(word_bank, pos=POS.VERB)
                              if ATTR.can_be_intransitive_verb in word_bank.get_attrs(word)]
        random.shuffle(intransitive_verbs)

        logger.info('loading transitive_verbs ...')
        transitive_verbs = [word
                            for word in self._load_words_by_pos_attrs(word_bank, pos=POS.VERB)
                            if ATTR.can_be_transitive_verb in word_bank.get_attrs(word)]
        random.shuffle(transitive_verbs)

        logger.info('making transitive verb and object combinations ...')

        @profile
        def build_transitive_verb_PASs() -> Iterator[Tuple[str, str]]:
            _transitive_verbs = shuffle(transitive_verbs)
            _nouns = shuffle(predicate_nouns)
            for i in range(min(len(_transitive_verbs), len(_nouns))):
                verb = _transitive_verbs[i]
                obj = _nouns[i]
                # yield pair_pred_with_obj_mdf(verb, obj, None)
                # yield PredicatePhrase(predicate=verb, object=obj)
                yield verb, obj
        is_transitive_verbs_empty = len(transitive_verbs) == 0 or len(predicate_nouns) == 0

        if adj_verb_noun_ratio is not None and len(adj_verb_noun_ratio) != 3:
            raise ValueError()
        adj_verb_noun_ratio = adj_verb_noun_ratio or [1, 2, 1]
        adj_verb_noun_weight = [3 * ratio / sum(adj_verb_noun_ratio) for ratio in adj_verb_noun_ratio]

        def make_chained_sampling_from_weighted_iterators(words, weights):
            _cyclic_words = []
            _weights = []
            for _words, weight in zip(words, weights):
                if _words == build_transitive_verb_PASs:
                    if is_transitive_verbs_empty:
                        continue
                    random_cycle = RandomCycle(_words, shuffle=False)
                else:
                    if len(_words) == 0:
                        continue
                    random_cycle = RandomCycle(_words)
                _cyclic_words.append(random_cycle)
                _weights.append(weight)
            return weighted_chained_sampling(_cyclic_words, _weights)

        if self._no_adj_verb_as_zeroary:
            zeroary_words = (event_nouns,)
            zeorary_weights = (1.0,)
        else:
            zeroary_words = (adjs, intransitive_verbs, build_transitive_verb_PASs, event_nouns)
            zeorary_weights = (adj_verb_noun_weight[0], adj_verb_noun_weight[1] * 1 / 3,
                               adj_verb_noun_weight[1] * 2 / 3, adj_verb_noun_weight[2])
        zeroary_predicates = make_chained_sampling_from_weighted_iterators(zeroary_words, zeorary_weights)

        unary_words = (adjs, intransitive_verbs, build_transitive_verb_PASs, predicate_nouns)
        unary_weights = (adj_verb_noun_weight[0], adj_verb_noun_weight[1] * 1 / 3,
                         adj_verb_noun_weight[1] * 2 / 3, adj_verb_noun_weight[2])
        unary_predicates = make_chained_sampling_from_weighted_iterators(unary_words, unary_weights)

        constants = entity_nouns

        return (
            (PredicatePhrase(predicate=pred[0], object=pred[1]) if isinstance(pred, tuple) else PredicatePhrase(predicate=pred)
             for pred in zeroary_predicates),
            (PredicatePhrase(predicate=pred[0], object=pred[1]) if isinstance(pred, tuple) else PredicatePhrase(predicate=pred)
             for pred in unary_predicates),
            [ConstantPhrase(constant=constant) for constant in constants],
        )

    @profile
    def _load_words_by_pos_attrs(self,
                                 word_bank: WordBank,
                                 pos: Optional[POS] = None,
                                 attrs: Optional[List[ATTR]] = None) -> Iterator[str]:
        cache_key = (id(word_bank), pos, tuple(attrs) if attrs is not None else None)
        if cache_key in self._load_words_by_pos_attrs_cache:
            yield from self._load_words_by_pos_attrs_cache[cache_key]
            return

        intermediate_cache = self._load_words_by_pos_attrs_cache_interm[cache_key]
        attrs = attrs or []
        for word in word_bank.get_words(slice_='extra_or_default'):
            if word in intermediate_cache:
                continue
            if pos is not None and pos not in word_bank.get_pos(word, not_found_warning=False):
                continue
            if any(attr not in word_bank.get_attrs(word)
                   for attr in attrs):
                continue
            intermediate_cache.add(word)
            yield word

        self._load_words_by_pos_attrs_cache[cache_key] = intermediate_cache

    @property
    def acceptable_formulas(self) -> List[str]:
        return list(self._translations.keys())

    @property
    def translation_names(self) -> List[str]:
        return [self._translation_name(sentence_key, weighted_nl[1])
                for sentence_key, templated_nls in self._translations.items()
                for weighted_nl in templated_nls]

    def _translation_name(self, sentence_key: str, templated_nl: str) -> str:
        return '____'.join([sentence_key, templated_nl])

    @profile
    def _translate(self, *args, **kwargs) -> Tuple[List[Tuple[Optional[str], Optional[str], Optional[Formula], Optional[str]]], Dict[str, int]]:
        return self._translate_inner(*args, **kwargs, compute_volume=True)

    @profile
    def _translate_fast(self, *args, **kwargs) -> Tuple[List[Tuple[Optional[str], Optional[str], Optional[Formula], Optional[str]]], Dict[str, int]]:
        return self._translate_inner(*args, **kwargs, compute_volume=False)

    @profile
    def _translate_inner(self,
                         formulas: List[Formula],
                         intermediate_constant_formulas: List[Formula],
                         knowledge_idxs: Optional[List[int]] = None,
                         collapsed_knowledge_idxs: Optional[List[int]] = None,
                         raise_if_translation_not_found=True,
                         compute_volume=True) -> Tuple[List[Tuple[Optional[str], Optional[str], Optional[Formula], Optional[str]]], Dict[str, int]]:
        if len(_UNCONDITIONED_VOLUME_CACHE) > DEFAULT_CACHE_SIZE:
            _UNCONDITIONED_VOLUME_CACHE.clear()
        if len(_LEAF_NL_GENERATOR_CACHE) > DEFAULT_CACHE_SIZE:
            _LEAF_NL_GENERATOR_CACHE.clear()
        if len(_POSSIBLE_CONDITIONS_CACHE) > DEFAULT_CACHE_SIZE:
            _POSSIBLE_CONDITIONS_CACHE.clear()
        logger.info('translation start with volume cache = %d', len(_UNCONDITIONED_VOLUME_CACHE))

        knowledge_idxs = knowledge_idxs or []
        collapsed_knowledge_idxs = collapsed_knowledge_idxs or []
        self._reset_assets()

        def raise_or_warn(msg: str) -> None:
            if raise_if_translation_not_found:
                raise TranslationNotFoundError(msg)
            else:
                logger.warning(msg)

        translations: List[Optional[str]] = []
        SO_swap_formulas: List[Optional[Formula]] = []
        translation_names: List[Optional[str]] = []
        count_stats: Dict[str, int] = {'inflation_stats': defaultdict(int)}

        knowledge_mapping = {}
        knowledge_pos_mapping = {}
        knowledge_types = [None] * len(formulas)
        if len(knowledge_idxs) > 0 or len(collapsed_knowledge_idxs) > 0:
            if len(self._knowledge_banks) == 0:
                raise ValueError()
            for type_, idxs in [('knowledge', knowledge_idxs),
                                ('collapsed_knowledge', collapsed_knowledge_idxs)]:
                should_knowledge_formulas = [formulas[idx] for idx in idxs]
                (
                    knowledge_mapping,
                    knowledge_pos_mapping,
                    is_injected,
                ) = self._sample_interpret_mapping(should_knowledge_formulas,
                                                   [],
                                                   constraints=knowledge_mapping,
                                                   POS_constraints=knowledge_pos_mapping,
                                                   knowledge_type=type_)
                for knowledge_formula, _is_injected in zip(should_knowledge_formulas, is_injected):
                    if _is_injected:
                        knowledge_types[formulas.index(knowledge_formula)] = type_

        interpret_mapping = self._sample_interpret_mapping(formulas,
                                                           intermediate_constant_formulas,
                                                           constraints=knowledge_mapping)
        pos_mapping = knowledge_pos_mapping

        for formula in formulas:
            found_keys = 0
            is_found = False

            key_push_mappings = list(self._get_translation_config_keys(formula))
            if not self.use_fixed_translation:
                random.shuffle(key_push_mappings)

            for translation_key, push_mapping in key_push_mappings:
                found_keys += 1

                # Choose a translation
                chosen_nl, _pos_mapping = self._sample_condition_match_nl(
                    translation_key,
                    interpret_mapping,
                    push_mapping,
                    pos_mapping=pos_mapping,
                    block_shuffle=not self.use_fixed_translation,
                    compute_volume=compute_volume,
                    volume_to_weight=self._volume_to_weight_func,
                )
                if chosen_nl is None:
                    msgs = [
                        f'translation not found for "{formula.rep}" in key="{translation_key}"',
                        'The possible causes includes:',
                        f'(i) the key="{translation_key}" in config indeed have no translation',
                        '(ii) we have found translations, but the sampled interpretation mapping could not match the pos and word inflation required by the translations. The interpret_mapping is the following:',
                        '\n    ' + '\n    '.join(pformat(interpret_mapping).split('\n')),
                        '\n    ' + '\n    '.join(pformat(pos_mapping or {}).split('\n')),
                    ]
                    logger.info('\n'.join(msgs))
                    continue

                pos_mapping.update(_pos_mapping)

                chosen_nl_pushed = interpret_formula(Formula(chosen_nl), push_mapping).rep

                # Generate word inflated mapping.
                inflated_mapping, _inflation_stats = self._make_phrase_inflated_interpret_mapping(
                    interpret_mapping,
                    chosen_nl_pushed,
                )

                if self.log_stats:
                    for inflation_type, count in _inflation_stats.items():
                        count_stats['inflation_stats'][f'{inflation_type}'] = count

                interpret_templated_translation_pushed = re.sub('\[[^\]]*\]', '', chosen_nl_pushed)

                # do interpretation using predicates and constants using interpret_mapping
                if self._do_translate_to_nl:
                    interpret_templated_translation_pushed_with_the_or_it = self._postprocess_template(
                        interpret_templated_translation_pushed)
                    translation = interpret_formula(Formula(interpret_templated_translation_pushed_with_the_or_it),
                                                    self._make_phrase_str_mapping(inflated_mapping)).rep
                else:
                    translation = interpret_templated_translation_pushed

                SO_swap_formula: Optional[Formula] = None
                # something like {A}{a}
                if len(formula.unary_PASs) == 1 and len(formula.predicates) == 1 and len(formula.constants) == 1:
                    constant = formula.constants[0].rep
                    predicate = formula.predicates[0].rep

                    constant_transl = interpret_mapping[constant]
                    predicate_transl = interpret_mapping[predicate]

                    if predicate_transl.object is not None:
                        SO_swap_interpret_mapping = deepcopy(inflated_mapping)
                        SO_swap_interpret_mapping[constant] = ConstantPhrase(constant=predicate_transl.object)
                        swap_object = ' '.join([rep for rep in [constant_transl.left_modifier, constant_transl.constant, constant_transl.right_modifier]
                                               if rep is not None])
                        SO_swap_interpret_mapping[predicate] = PredicatePhrase(predicate=predicate_transl.predicate,
                                                                               object=swap_object,
                                                                               right_modifier=predicate_transl.right_modifier,
                                                                               left_modifier=predicate_transl.left_modifier)

                        SO_swap_inflated_mapping, _ = self._make_phrase_inflated_interpret_mapping(
                            SO_swap_interpret_mapping,
                            chosen_nl_pushed,
                        )
                        interpret_templated_translation_pushed_with_the_or_it = self._postprocess_template(
                            interpret_templated_translation_pushed)
                        SO_swap_translation = interpret_formula(Formula(interpret_templated_translation_pushed_with_the_or_it),
                                                                self._make_phrase_str_mapping(SO_swap_inflated_mapping)).rep

                        used_predicates = {pred.rep
                                           for formula in formulas + SO_swap_formulas
                                           if formula is not None
                                           for pred in formula.predicates}
                        used_constants = {constant.rep
                                          for formula in formulas + SO_swap_formulas
                                          if formula is not None
                                          for constant in formula.constants}
                        unused_predicate = sorted(set(PREDICATES) - set(used_predicates))[0]
                        unused_constant = sorted(set(CONSTANTS) - set(used_constants))[0]

                        if self._do_translate_to_nl:
                            SO_swap_formula = interpret_formula(
                                formula, {predicate: unused_predicate, constant: unused_constant})
                            SO_swap_formula.translation = SO_swap_translation
                            logger.debug('make subj obj swapped translation: %s', SO_swap_translation)

                translations.append(translation)

                SO_swap_formulas.append(SO_swap_formula)

                translation_names.append(self._translation_name(translation_key, chosen_nl))
                is_found = True
                break

            if not is_found:
                if found_keys == 0:
                    raise_or_warn(f'translation not found for "{formula.rep}", since the translation_key was not found.')
                else:
                    raise_or_warn(
                        f'translation not found for "{formula.rep}" due to the reasons stated the above: (i) or (ii).')
                translations.append(None)
                translation_names.append(None)

        translations = [
            (self._all_postprocess_translation(translation, knowlege_type=knowlege_type) if translation is not None else None)
            for translation, knowlege_type in zip(translations, knowledge_types)
        ]

        for SO_swap_formula in SO_swap_formulas:
            if SO_swap_formula is not None and SO_swap_formula.translation is not None:
                SO_swap_formula.translation = (
                    self._all_postprocess_translation(SO_swap_formula.translation, knowlege_type=None)
                    if SO_swap_formula.translation is not None
                    else None
                )

        all_translations = translations + \
            [SO_swap_formula.translation if SO_swap_formula is not None else None for SO_swap_formula in SO_swap_formulas]
        all_translations = self._postprocess_translations_at_once(all_translations)
        translations = all_translations[:len(translations)]
        for SO_swap_formula, translation in zip(SO_swap_formulas, all_translations[len(translations):]):
            if SO_swap_formula is not None:
                SO_swap_formula.translation = translation

        return list(zip(translation_names, translations, SO_swap_formulas, knowledge_types)), count_stats

    def is_knowledge_translatable(self, formula: Formula) -> bool:
        return any(knowledge_bank.is_formula_accepatable(formula)
                   for knowledge_bank in self._knowledge_banks)

    @profile
    def _get_translation_config_keys(self, formula: Formula) -> Iterator[Tuple[str, Dict[str, str]]]:
        for _remove_outer_brace in [False, True]:
            if _remove_outer_brace:
                _formula = remove_outer_brace(formula)
            else:
                _formula = formula
            for _transl_key, _ in self._translations.items():
                if formula_can_not_be_identical_to(Formula(_transl_key), _formula):
                    continue

                for push_mapping in generate_mappings_from_formula([Formula(_transl_key)], [_formula]):
                    _transl_key_pushed = interpret_formula(Formula(_transl_key), push_mapping).rep
                    if _transl_key_pushed == _formula.rep:
                        yield _transl_key, push_mapping

    @profile
    def _sample_interpret_mapping(self,
                                  formulas: List[Formula],
                                  intermediate_constant_formulas: List[Formula],
                                  constraints: Optional[Dict[str, Phrase]] = None,
                                  POS_constraints: Optional[Dict[str, POS]] = None,
                                  knowledge_type: Optional[str] = None) -> Union[Dict[str, str], Tuple[Dict[str, Phrase], Dict[str, str], List[bool]]]:

        if knowledge_type is not None:
            if knowledge_type == 'knowledge':
                collapse = False
            elif knowledge_type == 'collapsed_knowledge':
                collapse = True
            else:
                raise ValueError(knowledge_type)

            mapping: Dict[str, Phrase] = copy(constraints or {})
            pos_mapping: Dict[str, POS] = copy(POS_constraints or {})
            is_injected = [False] * len(formulas)
            for knowledge_bank in shuffle(self._knowledge_banks):
                for i_formula, formula in enumerate(formulas):
                    new_mapping = knowledge_bank.sample_mapping(formula, collapse=collapse)
                    if new_mapping is None:
                        continue
                    if any(new_key in mapping for new_key in new_mapping):
                        continue
                    if any(new_key in pos_mapping for new_key in new_mapping):
                        raise ValueError('"pos_mapping" is inconsistent with "mapping"')
                    mapping.update({key: val[0] for key, val in new_mapping.items()})
                    pos_mapping.update({key: val[1] for key, val in new_mapping.items()
                                        if val[1] is not None})
                    is_injected[i_formula] = True

            return mapping, pos_mapping, is_injected

        else:
            constraints = constraints or {}

            zeroary_predicates = list({predicate.rep
                                       for formula in formulas
                                       for predicate in formula.zeroary_predicates})
            unary_predicates = list({predicate.rep
                                     for formula in formulas
                                     for predicate in formula.unary_predicates})
            constants = list({constant.rep for formula in formulas for constant in formula.constants})
            intermediate_constants = sorted({constant.rep for constant in intermediate_constant_formulas})

            # we sample more phrases so that we have more chance of POS/FORM condition matching.
            adj_verb_nouns = self._sample(self._unary_predicates, len(unary_predicates) * 3)

            if self.reused_object_nouns_max_factor > 0.0:
                obj_nouns = list({phrase.object for phrase in adj_verb_nouns
                                  if isinstance(phrase, PredicatePhrase)})
            else:
                obj_nouns = []

            event_noun_size = int(len(zeroary_predicates) * 2.0)
            event_nouns = self._sample(self._zeroary_predicates, max(event_noun_size, 0))

            entity_noun_size = int(math.ceil(len(constants) * 1.0))   # since all the constants have pos=NOUN, x 1.0 is enough
            while True:
                entity_nouns = [noun for noun in obj_nouns if noun in self._constant_set][: int(
                    entity_noun_size * self.reused_object_nouns_max_factor)]
                if len(entity_nouns) > 0:
                    logger.info('the following object nouns may be reused as as entity nouns: %s', str(entity_nouns))

                sampled_constants = self._sample(self._constants, max((entity_noun_size - len(entity_nouns)) * 5, 0))
                for constant in sampled_constants:
                    if len(entity_nouns) >= entity_noun_size:
                        break
                    if constant not in entity_nouns:
                        entity_nouns.append(constant)

                if len(entity_nouns) >= entity_noun_size:
                    break

            intermediate_constant_nouns = [
                ConstantPhrase(constant=word)
                for word in self._sample(self._word_bank.get_intermediate_constant_words(), len(intermediate_constants))
            ]

            zeroary_constraints = {k: v for k, v in constraints.items() if k in zeroary_predicates}
            # zero-ary predicate {A}, which appears as ".. {A} i ..", shoud be Noun.
            zeroary_mapping = next(
                generate_mappings_from_predicates_and_constants(
                    zeroary_predicates,
                    [],
                    event_nouns,
                    [],
                    shuffle=True,
                    allow_many_to_one=False,
                    constraints=zeroary_constraints,
                )
            )

            # Unary predicate {A}, which appears as "{A}{a}", shoud be adjective or verb.
            unary_constraints = {
                **dict(zip(intermediate_constants, intermediate_constant_nouns)),
                **{k: v for k, v in constraints.items() if k in unary_predicates + constants}
            }
            unary_mapping = next(
                generate_mappings_from_predicates_and_constants(
                    unary_predicates,
                    constants,
                    adj_verb_nouns,
                    entity_nouns,
                    shuffle=True,
                    allow_many_to_one=False,
                    constraints=unary_constraints,
                )
            )

            interpret_mapping = zeroary_mapping.copy()
            interpret_mapping.update(unary_mapping)

            return interpret_mapping

    @profile
    def _sample_condition_match_nl(self,
                                   sentence_key: str,
                                   interpret_mapping: Dict[str, Phrase],
                                   push_mapping: Dict[str, str],
                                   pos_mapping: Optional[Dict[str, str]] = None,
                                   block_shuffle=True,
                                   volume_to_weight=lambda weight: weight,
                                   compute_volume=True,
                                   log_indent=0) -> Tuple[Optional[str], Optional[Dict[str, POS]]]:
        """ Find templated NL that matches the conditions given by interpret_mapping, push_mapping and pos_mapping. """
        if _LOGS_FOR_DEBUG:
            print()
            print(' ' * log_indent + '**** _sample_condition_match_nl() ****')
            print(' ' * log_indent + '    sentence_key:', sentence_key)
            print(' ' * log_indent + '    pos_mapping:', pformat(pos_mapping))

        weights_and_templated_nls = self._translations[sentence_key]
        if block_shuffle:
            # shuffle to inject randomness to search.
            random.shuffle(weights_and_templated_nls)

        iterators = []
        weight_types: List[str] = []
        volumes: List[int] = []

        for weight_type, templated_nl in weights_and_templated_nls:
            iterator, volume = self._make_sampler_from_templated_nl(
                templated_nl,
                # set(['::'.join([_SENTENCE_TRANSLATION_PREFIX, sentence_key])]),
                set([templated_nl]),
                constraint_interpret_mapping=interpret_mapping,
                constraint_pos_mapping=pos_mapping,
                constraint_push_mapping=push_mapping,
                block_shuffle=block_shuffle,
                volume_to_weight=volume_to_weight,
                compute_volume=compute_volume,
                log_indent=log_indent + 4,
            )

            iterators.append(iterator)
            weight_types.append(weight_type)
            volumes.append(volume)

        if block_shuffle:
            weights = self._get_weights(volumes, weight_types, volume_to_weight)
            nl_and_conditions = (item for item in generate_weighted_chained_samples(iterators, weights))
        else:
            nl_and_conditions = (item for iterator in iterators for item in iterator)

        for nl, condition in nl_and_conditions:
            condition_is_consistent, _pos_mapping = self._is_mapping_and_condition_match(
                condition,
                interpret_mapping,
                push_mapping,
                pos_mapping=pos_mapping,
            )
            if not condition_is_consistent:
                continue

            pos_mapping_updated = deepcopy(pos_mapping)
            pos_mapping_updated.update(_pos_mapping)
            return nl, pos_mapping_updated

        return None, None

    def _get_weights(self,
                     volumes: List[Optional[float]],
                     weight_types: List[str],
                     volume_to_weight,
                     templated_nls=None,
                     interpret_mapping={}) -> List[float]:
        estimated_volume = self._estimate_volume(volumes)
        estimated_volumes = [volume if volume is not None else estimated_volume
                             for volume in volumes]
        volume_weights = [volume_to_weight(volume) for volume in estimated_volumes]
        weights = [self._get_compute_weight_func(weight_type)(volume_weights, i_iterator)
                   for i_iterator, weight_type in enumerate(weight_types)]
        return weights

    def _estimate_volume(self, volumes: List[Optional[float]]) -> float:
        """ Estimate the volumes, which have not been computed yet

        volume can be None if compute_volume is False and the volume is not in the cache.
        For such cases, we take RL strategy of "optimistic under uncertainty",
        that is, we assume the volume as large to encourage the exploration of such branches.
        Eventually we will get the exact volume, as the volume computation will become faster and faster with more cache.
        """
        not_null_volumes = [volume for volume in volumes if volume is not None]
        if len(not_null_volumes) > 0:
            return max(max(not_null_volumes), 1)
        else:
            return 1

    @lru_cache(maxsize=DEFAULT_CACHE_SIZE)
    @profile
    def _get_compute_weight_func(self, type_: str) -> Callable[[List[float], float], float]:
        """

        examples of type_
            "W_VOL__1.0"
            "W_VOL_AVG__0.1"
        """
        volume_weight_agg, factor = type_.split('__')

        _factor = float(factor)

        if volume_weight_agg == 'W_VOL':

            def agg_volume_weights(volume_weights: List[float], i: int) -> float:
                return volume_weights[i]

        elif volume_weight_agg == 'W_VOL_AVG':

            def agg_volume_weights(volume_weights: List[float], i: int) -> float:
                if len(volume_weights) == 1:
                    return volume_weights[i]
                else:
                    other_avg = statistics.mean(volume_weights[j] for j in range(len(volume_weights))
                                                if j != i)

                    if other_avg == 0.0:
                        return volume_weights[i]
                    else:
                        return other_avg

        else:
            raise ValueError(f'Unknown volume weight aggregation type "{volume_weight_agg}"')

        def get_weight(volume_weights: List[float], i: int) -> float:
            return agg_volume_weights(volume_weights, i) * _factor

        return get_weight

    # 再帰元1
    @profile
    def _make_sampler_from_templated_nl(self,
                                        templated_nl: str,
                                        ancestor_templated_nls: Set[str],
                                        constraint_interpret_mapping: Optional[Dict[str, Phrase]] = None,
                                        constraint_pos_mapping: Optional[Dict[str, str]] = None,
                                        constraint_push_mapping: Optional[Dict[str, str]] = None,
                                        block_shuffle=True,
                                        volume_to_weight=lambda volume: volume,
                                        compute_volume=True,
                                        check_condition=True,
                                        log_indent=0) -> Tuple[Iterator[TemplatedNLAndCondition], float]:
        """ Resolve templated nl such as "<<phrase::thing>> is <<phrase::{A}predicate>>" """
        if templated_nl.startswith('__'):
            return iter([]), 0
        if templated_nl in _LEAF_NL_GENERATOR_CACHE:
            return _LEAF_NL_GENERATOR_CACHE[templated_nl](), 1

        condition = self._extract_condition(templated_nl)
        if _PREFER_CONDITION_MATCHING_BRANCHES:
            for ancestor_templated_nl in ancestor_templated_nls:
                _POSSIBLE_CONDITIONS_CACHE[ancestor_templated_nl].add(tuple(condition))

        _constraint_pos_mapping = copy(constraint_pos_mapping)
        if check_condition and (constraint_push_mapping or _constraint_pos_mapping):
            have_consistent, _pos_mapping = self._is_mapping_and_condition_match(condition,
                                                                                 constraint_interpret_mapping,
                                                                                 constraint_push_mapping,
                                                                                 pos_mapping=_constraint_pos_mapping)
            if not have_consistent:
                return iter([]), 0
            else:
                _constraint_pos_mapping.update(_pos_mapping)

        templates = self._extract_templates(templated_nl)
        if len(templates) == 0:
            volume = 1

            def generate_leaf_nl():
                yield templated_nl, condition

            if len(condition) == 0:
                _LEAF_NL_GENERATOR_CACHE[templated_nl] = generate_leaf_nl

            return generate_leaf_nl(), volume

        else:
            # This sorting is VERY important for speed.
            # These templates will be input to generate_combination() function, which expand the generators in the order of the input.
            # So, if we place first the generators with more conditions such as [A.VERB] or [a.NOUN], which could be rejected due to condition mismatch,
            # we can reject the combination earlier.
            # Note that the inverse order will be much much slower, as only when we reach the last generators, can we reject the combination.
            sorted_templates = sorted(templates, key=self._condition_coeff)[::-1]

            template_resolved_generators = [
                ResolvedTemplateGenerator(
                    self,
                    template,
                    ancestor_templated_nls,
                    constraint_interpret_mapping,
                    constraint_pos_mapping,
                    constraint_push_mapping,
                    block_shuffle,
                    volume_to_weight,
                    compute_volume,
                    check_condition,
                    log_indent,
                )
                for template in sorted_templates
            ]

            total_volume = 1
            for generator in template_resolved_generators:
                volume = generator.compute_unconditioned_volume()
                if volume is None:
                    total_volume = None
                    break
                else:
                    total_volume *= volume

            return (
                generate_resolved_template_combinations(
                    self,
                    template_resolved_generators,
                    condition,
                    templated_nl,
                    sorted_templates,
                ),
                total_volume,
            )

    # 再帰元2
    @profile
    def _make_sampler_from_template(self,
                                    template: str,
                                    ancestor_templated_nls: Set[str],
                                    constraint_interpret_mapping: Optional[Dict[str, Phrase]] = None,
                                    constraint_pos_mapping: Optional[Dict[str, str]] = None,
                                    constraint_push_mapping: Optional[Dict[str, str]] = None,
                                    shuffle=True,
                                    volume_to_weight=lambda volume: volume,
                                    compute_volume=True,
                                    check_condition=True,
                                    log_indent=0) -> Tuple[Iterator[TemplatedNLAndCondition], float]:
        """ Resolve template such as "<<phrase::thing>>" """
        if _LOGS_FOR_DEBUG:
            print()
            print(' ' * log_indent + '-- _make_resolved_template_sampler() --')
            print(' ' * log_indent + '    template:', template)
            print(' ' * log_indent + '    ancestor_nls:', ancestor_templated_nls)
        template_key, templated_nls = self._find_templated_nls_from_config(template, log_indent=log_indent + 4)
        if template_key is None:
            raise Exception(f'template for {template} not found.')

        if shuffle:
            # shuffle to inject randomness to search.
            random.shuffle(templated_nls)

        iterators = []
        weight_types: List[str] = []
        volumes: List[int] = []
        condition_match_bonus_factors: List[float] = []
        for weight, templated_nl in templated_nls:
            if templated_nl in ancestor_templated_nls:
                continue

            exploitation_bonus_factor = 1.0
            if _PREFER_CONDITION_MATCHING_BRANCHES:
                multiplier = 3
                if constraint_interpret_mapping is not None\
                        and constraint_push_mapping is not None\
                        and constraint_pos_mapping is not None:
                    for possible_condition in _POSSIBLE_CONDITIONS_CACHE[templated_nl]:
                        have_consistent, _ = self._is_mapping_and_condition_match(
                            set(possible_condition),
                            constraint_interpret_mapping,
                            constraint_push_mapping,
                            pos_mapping=constraint_pos_mapping,
                        )
                        if have_consistent:
                            exploitation_bonus_factor * multiplier
                        else:
                            # note that we can not reject the templated_nl here, as we can have conditions other than possible_condition
                            pass

            iterator, volume = self._make_sampler_from_templated_nl(
                templated_nl,
                ancestor_templated_nls.union(set([templated_nl])),
                constraint_interpret_mapping=constraint_interpret_mapping,
                constraint_pos_mapping=constraint_pos_mapping,
                constraint_push_mapping=constraint_push_mapping,
                block_shuffle=shuffle,
                volume_to_weight=volume_to_weight,
                compute_volume=compute_volume,
                check_condition=check_condition,
                log_indent=log_indent + 4,
            )

            iterators.append(iterator)
            weight_types.append(weight)
            volumes.append(volume)
            condition_match_bonus_factors.append(exploitation_bonus_factor)

        if shuffle:
            weights = self._get_weights(volumes,
                                        weight_types,
                                        volume_to_weight,
                                        templated_nls=templated_nls,
                                        interpret_mapping=constraint_interpret_mapping)
            weights = [weight * exploitation_bonus_factor
                       for weight, exploitation_bonus_factor in zip(weights, condition_match_bonus_factors)]

            def generate():
                return generate_weighted_chained_samples(iterators, weights)

        else:
            def generate():
                for iterator in iterators:
                    for resolved_templated_nl, condition in iterator:
                        yield resolved_templated_nl, condition

        if any(volume is None for volume in volumes):
            volume_sum = None
        else:
            volume_sum = sum(volumes)

        return generate(), volume_sum

    @profile
    def _is_mapping_and_condition_match(self,
                                        condition: _PosFormConditionSet,
                                        interpret_mapping: Dict[str, Phrase],
                                        push_mapping: Dict[str, str],
                                        pos_mapping: Optional[Dict[str, POS]] = None) -> Tuple[bool, Dict[str, POS]]:
        if len(condition) == 0:
            return True, pos_mapping

        _pos_mapping = copy(pos_mapping)
        is_match = True
        for interprand_rep, pos, form in condition:
            interprand_rep_pushed = push_mapping[interprand_rep]
            phrase = interpret_mapping[interprand_rep_pushed]
            forced_pos = _pos_mapping.get(interprand_rep_pushed, None)

            allowed_pos = [forced_pos] if forced_pos is not None else self._get_pos(phrase)

            if pos not in allowed_pos:
                is_match = False
                break

            inflated_phrases = self._get_inflated_phrases(phrase, pos, form)
            if len(inflated_phrases) == 0:
                is_match = False
                break

            _pos_mapping[interprand_rep_pushed] = pos

        if is_match:
            return True, _pos_mapping
        else:
            return False, {}

    @lru_cache(maxsize=DEFAULT_CACHE_SIZE)
    @profile
    def _find_templated_nls_from_config(self,
                                        template: str,
                                        log_indent=0) -> Tuple[Optional[str], Optional[List[Tuple[str, str]]]]:
        if _LOGS_FOR_DEBUG:
            print()
            print(' ' * log_indent + '-- _find_templated_nls() --')
            print(' ' * log_indent + '    template:', template)

        template_prefix = '::'.join(template.split('::')[:-1])
        template_key = template.split('::')[-1]
        template_key_formula = Formula(template_key)

        found_templated_nls = None
        found_template_key = None

        config = self._two_layered_config[template_prefix]
        for transl_key, transl_nls in config.items():
            key_formula = Formula(transl_key)
            if formula_can_not_be_identical_to(key_formula, template_key_formula):
                continue

            for mapping in generate_mappings_from_formula([key_formula],
                                                          [template_key_formula]):
                key_formula_pulled = interpret_formula(key_formula, mapping)
                if key_formula_pulled.rep == template_key_formula.rep:
                    found_template_key = transl_key
                    found_templated_nls = []
                    for weighted_nl in transl_nls:
                        weight_type, nl = weighted_nl
                        found_templated_nls.append((weight_type, interpret_formula(Formula(nl), mapping).rep))
                    break

            if found_templated_nls is not None:
                break

        return (
            '::'.join([template_prefix, found_template_key]) if found_template_key is not None else None,
            found_templated_nls,
        )

    @lru_cache(maxsize=DEFAULT_CACHE_SIZE)
    def _condition_coeff(self, template: str) -> int:
        formula = Formula(template)
        # we to not need to consider constants, as their condition, that is they all should be nouns, is always met.
        return len(formula.predicates)

    def _make_phrase_str_mapping(self, mapping: Dict[str, Phrase]) -> Dict[str, str]:
        return {
            key: self._make_phrase_str(val)
            for key, val in mapping.items()
        }

    def _make_phrase_str(self, phrase: Phrase) -> str:
        if isinstance(phrase, ConstantPhrase):
            return self._make_constant_phrase_str(phrase)
        elif isinstance(phrase, PredicatePhrase):
            return self._make_predicate_phrase_str(phrase)
        else:
            raise ValueError(f'{str(phrase)}')

    @abstractmethod
    def _make_constant_phrase_str(self, const: ConstantPhrase) -> str:
        pass

    @abstractmethod
    def _make_predicate_phrase_str(self, pred: PredicatePhrase) -> str:
        pass

    def _merge_condition(self, this: _PosFormConditionSet, that: _PosFormConditionSet) -> _PosFormConditionSet:
        return this.union(that)

    @lru_cache(maxsize=DEFAULT_CACHE_SIZE)
    @profile
    def _extract_templates(self, templated_nl: str) -> List[str]:
        return [
            templated_nl[match.span()[0] + len(self._TEMPLATE_BRACES[0]): match.span()[1] - len(self._TEMPLATE_BRACES[1])]
            for match in re.finditer(f'{self._TEMPLATE_BRACES[0]}((?!{self._TEMPLATE_BRACES[1]}).)*{self._TEMPLATE_BRACES[1]}', templated_nl)
        ]

    @lru_cache(maxsize=DEFAULT_CACHE_SIZE)
    def _extract_condition(self, templated_nl: str) -> _PosFormConditionSet:
        formula = Formula(templated_nl)
        interprands = formula.predicates + formula.constants

        conditions: List[Tuple[str, POS, str]] = []
        for interprand in interprands:
            pos_form = self._get_interprand_condition_from_template(interprand.rep, formula.rep)
            if pos_form is None:
                continue
            pos, form = pos_form
            conditions.append((interprand.rep, pos, form))

        return _PosFormConditionSet(conditions)

    @profile
    def _sample(self,
                elems: Union[List[Any], Iterator[Any]],
                size: int,
                allow_duplicates=False) -> List[Any]:
        if isinstance(elems, list):
            if len(elems) < size:
                logger.warning('Can\'t sample %d elements. Will sample only %d elements.',
                               size,
                               len(elems))
                samples = random.sample(elems, len(elems))
            else:
                samples = random.sample(elems, size)
            if not allow_duplicates and len(samples) != len(set(samples)):
                raise ValueError('The given "elems" seems to have duplicates')
        else:
            samples: Set[Any] = set([])
            for elem in elems:
                samples.add(elem)
                if len(samples) >= size:
                    break
            if len(samples) < size:
                raise Exception('Could not sample %d elements from the iterator', size)
            samples = list(samples)
        return samples

    @profile
    def _take(self, elems: Union[Iterator[Any], List[Any]], size: int, allow_duplicates=False) -> List[Any]:
        if isinstance(elems, list):
            if len(elems) < size:
                logger.warning('Can\'t take %d elements. Will take only %d elements.',
                               size,
                               len(elems))
            samples = elems[:size]
            if not allow_duplicates and len(samples) != len(set(samples)):
                raise ValueError('The given "elems" seems to have duplicates')
        else:
            samples: Set[Any] = set([])
            for elem in elems:
                samples.add(elem)
                if len(samples) >= size:
                    break
            if len(samples) < size:
                raise Exception('Could not sample %d elements from the iterator', size)
            samples = list(samples)
        return samples

    @profile
    def _make_phrase_inflated_interpret_mapping(self,
                                                interpret_mapping: Dict[str, Phrase],
                                                interprand_templated_translation_pushed: str) -> Tuple[Dict[str, Phrase], Dict[str, int]]:
        inflated_mapping = {}
        stats = defaultdict(int)

        for interprand_formula in Formula(interprand_templated_translation_pushed).predicates\
                + Formula(interprand_templated_translation_pushed).constants:
            interprand_rep = interprand_formula.rep
            if interprand_templated_translation_pushed.find(f'{interprand_rep}[') >= 0:
                phrase = interpret_mapping[interprand_rep]
                pos_form = self._get_interprand_condition_from_template(
                    interprand_rep, interprand_templated_translation_pushed)
                if pos_form is None:
                    raise ValueError(
                        f'Could not extract pos and form information about "{interprand_rep}" from "{interprand_templated_translation_pushed}"')
                pos, form = pos_form
                if self.log_stats:
                    stats[f'{pos.value}.{form}'] += 1
                inflated_phrases = self._get_inflated_phrases(phrase, pos, form)

                assert len(inflated_phrases) > 0
                inflated_phrase = random.choice(inflated_phrases)
            else:
                raise Exception(
                    f'Something wrong. Since we have checked in that the translation indeed exists, this program must not pass this block.  The problematic translation is "{interprand_templated_translation_pushed}" and unfound string is "{interprand_rep}["',
                )
            inflated_mapping[interprand_rep] = inflated_phrase
        return inflated_mapping, stats

    @profile
    def _get_interprand_condition_from_template(self, interprand: str, rep: str) -> Optional[Tuple[POS, Optional[str]]]:
        interprand_begin = rep.find(interprand)
        if interprand_begin < 0:
            # raise Exception(f'Information for "{interprand}" can not be extracted from "{rep}".')
            return None
        interprand_end = interprand_begin + len(interprand)

        info_begin = interprand_end
        if rep[info_begin] != '[':
            # raise Exception(f'Information for "{interprand}" can not be extracted from "{rep}".')
            return None
        info_end_offset = rep[info_begin:].find(']')
        info_end = info_begin + info_end_offset + 1

        info = rep[info_begin + 1: info_end - 1]

        if len(info.split('.')) >= 2:
            pos_str, form = info.split('.')
        else:
            pos_str, form = info, 'normal'

        return POS[pos_str], form

    @lru_cache(maxsize=DEFAULT_CACHE_SIZE)
    @profile
    def _get_inflated_phrases(self, phrase: Phrase, pos: POS, form: str) -> Union[Tuple[str, ...], Tuple[Phrase, ...]]:
        if pos in [POS.ADJ, POS.ADJ_SAT]:
            force = True
        else:
            force = False

        if isinstance(phrase, PredicatePhrase):
            _word, obj, right_modifier, left_modifier = phrase.predicate, phrase.object, phrase.right_modifier, phrase.left_modifier
        elif isinstance(phrase, ConstantPhrase):
            _word, right_modifier, left_modifier = phrase.constant, phrase.right_modifier, phrase.left_modifier
        else:
            raise ValueError()

        inflated_words = self._word_bank.change_word_form(_word, pos, form, force=False)   # SLOW
        if len(inflated_words) == 0 and force:
            inflated_words = self._word_bank.change_word_form(_word, pos, form, force=True)

        if isinstance(phrase, PredicatePhrase):
            return tuple(PredicatePhrase(predicate=_inflated_word, object=obj, right_modifier=right_modifier, left_modifier=left_modifier)
                         for _inflated_word in inflated_words)

        elif isinstance(phrase, ConstantPhrase):
            return tuple(ConstantPhrase(constant=_inflated_word, right_modifier=right_modifier, left_modifier=left_modifier)
                         for _inflated_word in inflated_words)

        else:
            raise ValueError()

    @lru_cache(maxsize=DEFAULT_CACHE_SIZE)
    def _get_pos(self, phrase: Phrase) -> List[POS]:
        if isinstance(phrase, PredicatePhrase):
            POSs = self._word_bank.get_pos(phrase.predicate)
            if phrase.object is not None:
                assert POS.VERB in POSs
                POSs = [POS.VERB]
        elif isinstance(phrase, ConstantPhrase):
            POSs = self._word_bank.get_pos(phrase.constant)
        else:
            raise ValueError(str(phrase))
        return POSs

    @abstractmethod
    def _postprocess_template(self, template: str) -> str:
        pass

    @abstractmethod
    def _reset_assets(self) -> None:
        pass

    def _all_postprocess_translation(self, translation: str, knowlege_type: Optional[str] = None) -> str:
        # We need to postprocess not only "knowlege_type" formulas but others,
        # because the translations can "spills" to other formulas.
        for knowledge_bank in self._knowledge_banks:
            translation = knowledge_bank.postprocess_translation(translation)
        translation = self._postprocess_translation(translation)
        return translation

    @abstractmethod
    def _postprocess_translation(self, translation: str) -> str:
        pass

    @abstractmethod
    def _postprocess_translations_at_once(self, translations: List[str]) -> List[str]:
        pass
