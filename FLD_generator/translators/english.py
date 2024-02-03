import re
import random
import logging
from typing import Set, Optional

from FLD_generator.formula import Formula
from FLD_generator.utils import starts_with_vowel_sound
from FLD_generator.word_banks import POS, ATTR
from FLD_generator.word_banks.english import MODAL_VERBS
from FLD_generator.person_names import get_person_names
from .templated import TemplatedTranslator
from .base import PredicatePhrase, ConstantPhrase

import line_profiling


logger = logging.getLogger(__name__)


class EnglishTranslator(TemplatedTranslator):

    def __init__(self,
                 *args,
                 no_transitive_object=False,
                 **kwargs):
        super().__init__(*args, **kwargs)

        self._no_transitive_object = no_transitive_object

        self._male_names: Set[str] = set()
        self._female_names: Set[str] = set()
        for person in get_person_names(country='US', details=True):
            if person['gender'] == 'M':
                self._male_names.add(person['name'])
            else:
                self._female_names.add(person['name'])

    def _postprocess_template(self, template: str) -> str:
        # return self._add_the_or_it_to_successive_appearance(template)
        return template

    # @profile
    # def _add_the_or_it_to_successive_appearance(self, sentence_with_templates: str) -> str:
    #     constants = [c.rep for c in Formula(sentence_with_templates).constants]

    #     if len(constants) >= 2:
    #         # If we have many constants, replacing one with pronoun may induce ambiguity
    #         return sentence_with_templates

    #     with_definite = sentence_with_templates
    #     for constant in constants:
    #         if with_definite.count(constant) < 2:  # have two appearance
    #             continue

    #         first_pos = with_definite.find(constant)

    #         until_first = with_definite[:first_pos + len(constant)]
    #         from_second = with_definite[first_pos + len(constant):]

    #         if re.match(f'.*a {constant} is.*', from_second):
    #             # HONOKA
    #             # the/itは，<<phrase::it>>に移したので，この関数は使われていないと思っている．
    #             # もし使っているようなら，複数系(they)を追加したい．
    #             # 無論，複数系の追加を待たずにこの関数を使うこともできる．
    #             # raise Exception('This function is not expected to be used.')

    #             replace_with_it = random.random() >= 0.5
    #         else:
    #             replace_with_it = False

    #         if replace_with_it:
    #             from_second_with_definite = re.sub(
    #                 f'a {constant} is',
    #                 'it is',
    #                 from_second,
    #             )
    #         else:
    #             from_second_with_definite = re.sub(
    #                 f'(.*)a (.*){constant}',
    #                 f'\g<1>the \g<2>{constant}',
    #                 from_second,
    #             )
    #         with_definite = until_first + from_second_with_definite
    #     if sentence_with_templates != with_definite:
    #         logger.info('particles "a (...) %s" are modified as:    "%s"    ->    "%s"',
    #                     constant,
    #                     sentence_with_templates,
    #                     with_definite)
    #     return with_definite

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
        # translation = self._pronoun_thing_to_person(translation)
        # translation = self._fix_pred_singularity(translation)   # we will handle singular/plural matter in the translation configs
        translation = self._randomly_convert_thing_to_person(translation)
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

    def _randomly_convert_thing_to_person(self, translation: str) -> str:
        if random.random() < 0.5:
            return translation

        # convert appearance of thhing such as 'the thing' and 'something' into person nouns
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

        # convert thing pronouns into person pronouns
        # we have to handle only 'it', as 'they' is OK for person pronouns
        person_pronouns = ['he', 'she', 'he/she', 'she/he', 'the one', 'the person']
        person_pronoun = random.choice(person_pronouns)
        tokens = translation.split(' ')
        tokens = [person_pronoun if token == 'it' else token
                  for token in tokens]
        translation = ' '.join(tokens)

        return translation

    # def _pronoun_thing_to_person(self, translation: str) -> str:
    #     thing_pronouns = ['it', 'the thing']
    #     person_pronouns = ['he', 'she', 'he/she', 'she/he', 'the one', 'the person']
    #     if translation.find('someone') >= 0 or translation.find('somebody') >= 0:
    #         for thing_pronoun in thing_pronouns:
    #             person_pronoun = random.choice(person_pronouns)
    #             translation = translation.replace(f' {thing_pronoun} ', f' {person_pronoun} ')
    #     return translation

    # def _fix_pred_singularity(self, translation: str) -> str:
    #     # TODO: A and B {is, runs} => currently, we do not have ({A}{a} and {B}{a}) so that we do not this fix.
    #     translation_fixed = translation

    #     def fix_all_thing_is(translation: str, src_pred: str, dst_pred: str) -> str:
    #         if re.match(f'.*all .*things? {src_pred}.*', translation):
    #             translation_fixed = re.sub(f'(.*)all (.*)things? {src_pred}(.*)',
    #                                        '\g<1>all \g<2>things ' + dst_pred + '\g<3>', translation)
    #             return translation_fixed
    #         else:
    #             return translation

    #     translation_fixed = fix_all_thing_is(translation_fixed, 'is an', 'are')
    #     translation_fixed = fix_all_thing_is(translation_fixed, 'is a', 'are')
    #     translation_fixed = fix_all_thing_is(translation_fixed, 'is', 'are')

    #     translation_fixed = fix_all_thing_is(translation_fixed, 'was an', 'were')
    #     translation_fixed = fix_all_thing_is(translation_fixed, 'was a', 'were')
    #     translation_fixed = fix_all_thing_is(translation_fixed, 'was', 'wer')

    #     translation_fixed = fix_all_thing_is(translation_fixed, 'does', 'do')

    #     # all kind thing squashes apple -> all kind thing squash apple
    #     if re.match('(.*)all (.*)things? ([^ ]*)(.*)', translation_fixed):
    #         word_after_things = re.sub('(.*)all (.*)things? ([^ ]*)(.*)', '\g<3>', translation_fixed)
    #         if POS.VERB in self._word_bank.get_pos(word_after_things):
    #             verb_normal = self._word_bank.change_word_form(word_after_things, POS.VERB, 'normal')[0]
    #             translation_fixed = re.sub('(.*)all (.*)things? ([^ ]*)(.*)',
    #                                        '\g<1>all \g<2>things ' + verb_normal + '\g<4>', translation_fixed)

    #     # target   : A and B causes C -> A and B cause C
    #     # negagive : A runs and it is also kind
    #     # def fix_A_and_B_is(translation: str, src_pred: str, dst_pred: str) -> str:
    #     #     if re.match(f'.*[^ ]* and [^ ]* {src_pred}.*', translation):
    #     #         translation_fixed = re.sub('.*([^ ]*) and ([^ ]*) {src_pred}(.*)', '\g<1>all \g<2>things ' + dst_pred + '\g<3>', translation)
    #     #         return translation_fixed
    #     #     else:
    #     #         return translation

    #     if translation_fixed != translation:
    #         logger.info('translation is fixed as:\norig : "%s"\nfixed: "%s"', translation, translation_fixed)

    #     return translation_fixed

    def _strip_the_from_named_entities(self, translation: str) -> str:
        tokens = translation.split(' ')

        NE_indices = [i for i, token in enumerate(tokens)
                      if ATTR.can_be_named_entity_noun in self._word_bank.get_attrs(token, pos_not_found_warning=False)]
        unwanted_the_indices = [i - 1
                                for i in NE_indices
                                if i - 1 >= 0 and tokens[i - 1] == 'the']
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
