import re
import random
import logging
from typing import Set, Optional, List, Any, Dict

from FLD_generator.formula import Formula
from FLD_generator.utils import starts_with_vowel_sound
from FLD_generator.word_banks import POS, ATTR
from FLD_generator.word_banks.english import MODAL_VERBS
from .templated import TemplatedTranslator
from .base import PredicatePhrase, ConstantPhrase

import line_profiling


logger = logging.getLogger(__name__)


class EnglishTranslator(TemplatedTranslator):

    _IDENTIFIERS = [
        'the',
        'this',
        'that',
    ]
    _IDENTIFIERS_PLURAL = [
        'the',
        'these',
        'those',
    ]

    _THING_PRONOUNS = [
        'it',
        'this',
        'that',
    ] + [
        f'{identifier} thing' for identifier in _IDENTIFIERS
    ]

    _THING_PRONOUNS_PLURAL = [
        'they',
        'these',
        'those',
    ] + [
        f'{identifier} things' for identifier in _IDENTIFIERS_PLURAL
    ]

    _PERSON_PRONOUNS = [
        'he', 'she', 'he/she', 'she/he',
    ] + [
        f'{identifier} one' for identifier in _IDENTIFIERS
    ] + [
        f'{identifier} person' for identifier in _IDENTIFIERS
    ]

    _PERSON_PRONOUNS_PLURAL = [
        'they',
    ] + [
        f'{identifier} ones' for identifier in _IDENTIFIERS_PLURAL
    ] + [
        f'{identifier} persons' for identifier in _IDENTIFIERS_PLURAL
    ] + [
        f'{identifier} people' for identifier in _IDENTIFIERS_PLURAL
    ]

    def __init__(self,
                 *args,
                 no_transitive_object=False,
                 **kwargs):
        super().__init__(*args, **kwargs)

        self._no_transitive_object = no_transitive_object

    def _postprocess_template(self, template: str) -> str:
        return template

    def _reset_assets(self) -> None:
        pass

    def _make_constant_phrase_str(self, const: ConstantPhrase) -> str:
        rep = const.constant
        if const.left_modifier is not None:
            rep = f'{const.left_modifier} ' + rep
        if const.right_modifier is not None:
            rep = rep + f' {const.right_modifier} '
        return rep

    def _make_predicate_phrase_str(self, pred: PredicatePhrase) -> str:
        rep = pred.predicate
        if pred.left_modifier is not None:
            rep = f'{pred.left_modifier} ' + rep

        if pred.object is not None and pred.right_modifier is not None:
            raise Exception(
                'Can not determine the order of these phrases. We do not expect to pass this code, therefore, might be a bug.')
        if pred.object is not None and not self._no_transitive_object:
            rep += f' {pred.object}'
        if pred.right_modifier is not None:
            rep += f' {pred.right_modifier}'
        return rep

    def _postprocess_translation(self, translation: str) -> str:
        translation = self._correct_indefinite_particles(translation)
        translation = self._argument_thing_vs_person_and_pronouns(translation)
        translation = self._reduce_degenerate_blanks(translation)
        translation = self._strip_the_from_named_entities(translation)

        for mv0 in MODAL_VERBS:
            for mv1 in MODAL_VERBS:
                # something like "does can run fast"  "does not can run fast", which cause from knowledge bank
                translation = translation.replace(f'{mv0} {mv1}', f'{mv1}')
                translation = translation.replace(f'{mv0} not {mv1}', f'{mv1} not')
                translation = translation.replace(f'{mv0}n\'t {mv1}', f'{mv1} not')

        # translation = self._uppercase_beggining(translation)  # this module should not know whether this is the beginning if a sentence
        translation = self._add_ending_period(translation)
        return translation

    def _postprocess_translations_at_once(self, translations: List[Optional[str]]) -> List[Optional[str]]:
        translations = self._argument_pronouns_at_once(translations)
        return translations

    def _argument_pronouns_at_once(self, translations: List[Optional[str]]) -> List[Optional[str]]:

        ng_list = [
            # replacement of pronouns is done in _arugment_thing_vs_person_and_pronouns
            'the thing',
            'the one', 'the body', 'the person', 'the man',

            'the fact', 'the claim', 'the statement', 'the proposition',
        ]
        string_concat = ' '.join([t for t in translations if t is not None])
        entities_with_the = re.findall(r'\bthe \w+\b', string_concat)

        # we first make replacement, such as 'the apple' to 'that apple',
        # which is used for all the translations for consistnecy.
        identifiers = ['this', 'that']
        replace_entities: Dict[str, str] = {}
        for entity_with_the in entities_with_the:
            if entity_with_the in ng_list:
                continue
            if random.random() < 0.5:
                identifier = random.choice(identifiers)
                entity = re.sub(r'^the ', '', entity_with_the)
                replace_entities[entity_with_the] = f'{identifier} {entity}'

        translations_processed: List[Optional[str]] = []
        for translation in translations:
            if translation is None:
                translations_processed.append(None)
                continue

            for entity, replacement in replace_entities.items():
                translation = translation.replace(entity, replacement)

            translations_processed.append(translation)

        return translations_processed


    @profile
    def _correct_indefinite_particles(self, sentence_wo_templates: str) -> str:
        """ choose an appropriate indefinite particls, i.e., "a" or "an", depending on the word pronounciation """
        words = sentence_wo_templates.split(' ')
        corrected_words = []
        for i_word, word in enumerate(words):
            if word.lower() in ['a', 'an']:
                if len(words) >= i_word + 2:
                    next_word = words[i_word + 1]
                    if starts_with_vowel_sound(next_word):
                        corrected_words.append('an')
                    else:
                        corrected_words.append('a')
                else:
                    logger.warning('Sentence might end with particle: "%s"', sentence_wo_templates)
                    corrected_words.append(word)
            else:
                corrected_words.append(word)
        corrected_sentence = ' '.join(corrected_words)
        return corrected_sentence

    def _argument_thing_vs_person_and_pronouns(self, translation: str) -> str:
        is_person = random.random() < 0.5

        if is_person:
            # convert appearance of thing such as 'the thing' and 'something' into person nouns
            person_postfix = random.choice(['one', 'body', 'person', 'man'])
            if person_postfix == 'one':
                translation = translation.replace('everything', 'everyone')
                translation = translation.replace('something', 'someone')
                translation = translation.replace('nothing', 'noone')
                translation = translation.replace('things', 'ones')
                translation = translation.replace('thing', 'one')

                translation = translation.replace('noone', random.choice(['no one', 'none']))

            elif person_postfix == 'body':
                translation = translation.replace('everything', 'everybody')
                translation = translation.replace('something', 'somebody')
                translation = translation.replace('nothing', 'nobody')
                translation = translation.replace('things', 'ones')
                translation = translation.replace('thing', 'one')

            elif person_postfix == 'person':
                translation = translation.replace('everything', 'every person')
                translation = translation.replace('something', 'some person')
                translation = translation.replace('nothing', 'no person')
                translation = translation.replace('things', random.choice(['persons', 'people']))
                translation = translation.replace('thing', 'person')

            elif person_postfix == 'man':
                translation = translation.replace('everything', 'every man')
                translation = translation.replace('something', 'some man')
                translation = translation.replace('nothing', 'no man')
                translation = translation.replace('things', 'men')
                translation = translation.replace('thing', 'man')

            else:
                raise ValueError()

        translation = self._argument_pronouns(translation, is_person=is_person)

        return translation

    def _argument_pronouns(self,
                          translation: str,
                          is_person=False) -> str:
        tokens = translation.split(' ')

        if is_person:
            pronoun_src = 'it'
            if random.random() < 0.5:
                pronouns_dst = random.choice(self._PERSON_PRONOUNS)
            else:
                pronouns_dst = pronoun_src
            tokens = self._replace_list(tokens, pronoun_src, pronouns_dst)

            pronoun_src = 'they'
            if random.random() < 0.5:
                pronouns_dst = random.choice(self._PERSON_PRONOUNS_PLURAL)
            else:
                pronouns_dst = pronoun_src
            tokens = self._replace_list(tokens, pronoun_src, pronouns_dst)

        else:
            pronoun_src = 'it'
            if random.random() < 0.5:
                pronouns_dst = random.choice(self._THING_PRONOUNS)
            else:
                pronouns_dst = pronoun_src
            tokens = self._replace_list(tokens, pronoun_src, pronouns_dst)

            pronoun_src = 'they'
            if random.random() < 0.5:
                pronouns_dst = random.choice(self._THING_PRONOUNS_PLURAL)
            else:
                pronouns_dst = pronoun_src
            tokens = self._replace_list(tokens, pronoun_src, pronouns_dst)

        return ' '.join(tokens)

    def _strip_the_from_named_entities(self, translation: str) -> str:
        tokens = translation.split(' ')

        NE_indices = [i for i, token in enumerate(tokens)
                      if ATTR.can_be_named_entity_noun in self._word_bank.get_attrs(token, pos_not_found_warning=False)]
        unwanted_the_indices = [
            i - 1
            for i in NE_indices
            # we do not replace "that" here do prevent replcing "that" of other uses, e.g., "that Alice is red is .."
            if i - 1 >= 0 and tokens[i - 1] in ['the', 'this']
        ]
        translation = ' '.join([token for i, token in enumerate(tokens)
                                if i not in unwanted_the_indices])

        return translation

    def _reduce_degenerate_blanks(self, translation: str) -> str:
        return re.sub(r'\s+', ' ', translation).strip(' ')

    def _uppercase_beggining(self, translation: str) -> str:
        return translation[0].upper() + translation[1:]

    def _add_ending_period(self, translation: str) -> str:
        if not translation.endswith('.'):
            return translation + '.'
        else:
            return translation

    def _replace_list(self, items: List[Any], src: Any, dst: Any) -> List[Any]:
        return [dst if item == src else item for item in items]
