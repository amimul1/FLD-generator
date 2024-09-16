from typing import Dict, List, Any
import copy


def _to_range(begin: int, end: int) -> List[int]:
    return list(range(begin, end + 1))



_DEFAULT_DATASET_SETTINGS = {

    '20221115': {
        'unknown_ratio': 0.33,
        'sample_all_stances_per_logic': False,
        'context_shuffles_per_instance': 1,

        'propositional_arguments_factor': 1.0,

        'knowledge_range': None,
        'collapsed_knowledge_range': None,
        'knowledge_argument_factor': 1.0,
        'atomic_filepath': None,
        'concept_net_100k_filepath': None,
        'dbpedia_filepath': None,

        'quantifier_axioms': [
            'universal_quantifier_elim',
            # 'universal_quantifier_intro',

            # we do not use existential_quantifier_intro since it has no linkable_args without existential_quantifier_elim, which is not implemented yet.
            # 'existential_quantifier_intro',
        ],

        'fallback_from_formula_to_translation_distractor': True,



        'translation_volume_to_weight': 'sqrt',
        'translation_adj_verb_noun_ratio': '1-2-1',
        'translation_configs': ['old-thing.v0'],
        'translation_no_transitive_object': False,

        'distractor_variants_per_tree': 1,
        'translation_variants_per_logic': 1,
    },


    '20221203': {
        'unknown_ratio': 0.33,
        'sample_all_stances_per_logic': False,
        'context_shuffles_per_instance': 1,

        'propositional_arguments_factor': 1.0,

        'knowledge_range': None,
        'collapsed_knowledge_range': None,
        'knowledge_argument_factor': 1.0,
        'atomic_filepath': None,
        'concept_net_100k_filepath': None,
        'dbpedia_filepath': None,

        'quantifier_axioms': [
            'universal_quantifier_elim',
            # 'universal_quantifier_intro',

            # we do not use existential_quantifier_intro since it has no linkable_args without existential_quantifier_elim, which is not implemented yet.
            # 'existential_quantifier_intro',
        ],

        'distractor': 'mixture(negative_tree.simplified_formula.various_form)',
        'fallback_from_formula_to_translation_distractor': True,
        'swap_ng_words_config': './configs/translation_distractors/swap_ng_words.json',



        'translation_volume_to_weight': 'sqrt',
        'translation_adj_verb_noun_ratio': '1-2-1',
        'translation_configs': ['old-thing.v0'],
        'translation_no_transitive_object': False,


        'generate_stem_steps_distrib': 'flat',

        'distractor_variants_per_tree': 1,
        'translation_variants_per_logic': 1,

    },


    '20230626.many_bugs_fixed': {
        'unknown_ratio': 0.33,
        'sample_all_stances_per_logic': False,
        'context_shuffles_per_instance': 1,

        'propositional_arguments_factor': 1.0,

        'knowledge_range': None,
        'collapsed_knowledge_range': None,
        'knowledge_argument_factor': 1.0,
        'atomic_filepath': None,
        'concept_net_100k_filepath': None,
        'dbpedia_filepath': None,

        # 'negative_tree_negated_hypothesis_ratio': 0.5,
        'distractor': 'mixture(negative_tree-0.5.simplified_formula.various_form)',
        'fallback_from_formula_to_translation_distractor': False,


        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,

        'translation_volume_to_weight': 'sqrt',
        'translation_adj_verb_noun_ratio': '1-2-1',
        'translation_lang': 'eng',
        'translation_configs': ['old-thing.v1'],
        'translation_no_transitive_object': False,

        'distractor_variants_per_tree': 1,
        'translation_variants_per_logic': 1,

    },


    '20231018.thing_person_config_translation': {
        'unknown_ratio': 0.33,
        'sample_all_stances_per_logic': False,
        'context_shuffles_per_instance': 1,

        'propositional_arguments_factor': 1.0,

        'knowledge_range': None,
        'collapsed_knowledge_range': None,
        'knowledge_argument_factor': 1.0,
        'atomic_filepath': None,
        'concept_net_100k_filepath': None,
        'dbpedia_filepath': None,

        # 'negative_tree_negated_hypothesis_ratio': 0.5,
        'distractor': 'mixture(negative_tree-0.5.simplified_formula.various_form)',
        'fallback_from_formula_to_translation_distractor': False,

        'generate_stem_steps_distrib': 'flat',

        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,

        'translation_volume_to_weight': 'sqrt',
        'translation_adj_verb_noun_ratio': '1-2-1',
        'translation_lang': 'eng',
        'translation_configs': ['thing_person.v0'],
        'translation_no_transitive_object': False,

        'distractor_variants_per_tree': 1,
        'translation_variants_per_logic': 1,

    },





}



_DATASET_SETTINGS = {


    '20231203.jpn.D1_wo_dist': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 1),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 0),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 500,
            'train': 10000,
        }

    },


    '20231203.jpn.D1': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 1),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 500,
            'train': 10000,
        }

    },


    '20231203.jpn.D3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            # 'test': 500,
            'train': 1000,

            # 'test': 1000,
        }

    },



    '20231203.jpn.D5': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 5),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 500,
            'train': 1000,
        }

    },




    '20231203.jpn.D8': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 8),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            # 'test': 500,
            'train': 1000,
        }

    },








    '20231213.jpn.D1_wo_dist': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 1),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 0),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 5000,
            'valid': 5000,
            'train': 30000,
        }

    },


    '20231213.jpn.D1': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 1),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 5000,
            'valid': 5000,
            'train': 30000,
        }

    },


    '20231213.jpn.D3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 5000,
            'valid': 5000,
            'train': 30000,
        }

    },



    '20231213.jpn.D5': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 5),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 5000,
            'valid': 5000,
            'train': 30000,
        }

    },




    '20231213.jpn.D8': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 8),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 5000,
            'valid': 5000,
            'train': 30000,
        }

    },













    '20230115.jpn.BCCWJ.D3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1.pretty'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'BCCWJ',


        'split_sizes': {
            'test': 100,
            # 'valid': 5000,
            # 'train': 30000,
        }

    },

    '20230115.jpn.punipuni.D3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1.pretty'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 100,
            # 'valid': 5000,
            # 'train': 30000,
        }

    },




    '20230116.jpn.BCCWJ.D3.argument_pred_arg_only': {

        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'BCCWJ',


        'split_sizes': {
            'test': 300,
            # 'valid': 5000,
            # 'train': 30000,
        }
    },

    '20230116.jpn.punipuni.D3.argument_pred_arg_only': {

        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 300,
            # 'valid': 5000,
            # 'train': 30000,
        }

    },






    '20230118.jpn.wordnet.D3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': False,
        'translation_vocab': 'wordnet',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            'train': 30000,
        }
    },


    '20230118.jpn.wordnet.D3.argument_pred_arg_only': {

        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': False,
        'translation_vocab': 'wordnet',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            'train': 30000,
        }
    },


    '20230118.jpn.wordnet.D3.argument_pred_arg_only.no_kaku': {

        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'wordnet',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            'train': 30000,
        }
    },





    '20230118.jpn.BCCWJ.D3': {

        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'BCCWJ',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            'train': 30000,
        }
    },




    '20230118.jpn.punipuni.D3': {

        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            'train': 30000,
        }

    },






    '20230118.jpn.wordnet.D3.extension-3.distractor-10': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 3),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 10),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': False,
        'translation_vocab': 'wordnet',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            # 'train': 30000,
        }
    },



    '20230118.jpn.wordnet.D3.extension-3.distractor-5': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 3),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 5),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': False,
        'translation_vocab': 'wordnet',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            # 'train': 30000,
        }
    },


    '20230118.jpn.wordnet.D3.extension-3.distractor-3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 3),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 3),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': False,
        'translation_vocab': 'wordnet',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            # 'train': 30000,
        }
    },



    '20230118.jpn.wordnet.D3.extension-2.distractor-5': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 2),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 5),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': False,
        'translation_vocab': 'wordnet',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            # 'train': 30000,
        }
    },


    '20230118.jpn.wordnet.D3.extension-2.distractor-3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 2),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 3),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': False,
        'translation_vocab': 'wordnet',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            # 'train': 30000,
        }
    },



    '20230118.jpn.wordnet.D3.extension-1.distractor-5': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 1),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 5),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': False,
        'translation_vocab': 'wordnet',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            # 'train': 30000,
        }
    },


    '20230118.jpn.wordnet.D3.extension-1.distractor-3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 1),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 3),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': False,
        'translation_vocab': 'wordnet',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            # 'train': 30000,
        }
    },

















    '20230120.jpn.wordnet.D3': {


        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'wordnet',


        'split_sizes': {
            # 'test': 5000,
            'valid': 5000,
            'train': 30000,
        }
    },










    '20230120.jpn.wordnet_repro_w_proposition.D1_wo_dist': {


        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',

            # './configs/arguments/predicate/axioms/and_or.json',
            # './configs/arguments/predicate/axioms/implication_intro.json',
            # './configs/arguments/predicate/axioms/negation.json',
            # './configs/arguments/predicate/axioms/implication_elim.json',
            # './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 1),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 0),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': False,
        'translation_vocab': 'wordnet',


        'split_sizes': {
            'test': 5000,
            'valid': 5000,
            'train': 30000,
        }
    },


    '20230120.jpn.wordnet_repro_w_proposition.D1': {


        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',

            # './configs/arguments/predicate/axioms/and_or.json',
            # './configs/arguments/predicate/axioms/implication_intro.json',
            # './configs/arguments/predicate/axioms/negation.json',
            # './configs/arguments/predicate/axioms/implication_elim.json',
            # './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 1),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': False,
        'translation_vocab': 'wordnet',


        'split_sizes': {
            'test': 5000,
            'valid': 5000,
            'train': 30000,
        }
    },



    '20230120.jpn.wordnet_repro_w_proposition.D3': {


        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',

            # './configs/arguments/predicate/axioms/and_or.json',
            # './configs/arguments/predicate/axioms/implication_intro.json',
            # './configs/arguments/predicate/axioms/negation.json',
            # './configs/arguments/predicate/axioms/implication_elim.json',
            # './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': False,
        'translation_vocab': 'wordnet',


        'split_sizes': {
            'test': 5000,
            'valid': 5000,
            'train': 30000,
        }
    },



    '20230120.jpn.wordnet_repro_w_proposition.D8': {


        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',

            # './configs/arguments/predicate/axioms/and_or.json',
            # './configs/arguments/predicate/axioms/implication_intro.json',
            # './configs/arguments/predicate/axioms/negation.json',
            # './configs/arguments/predicate/axioms/implication_elim.json',
            # './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 8),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': False,
        'translation_vocab': 'wordnet',


        'split_sizes': {
            'test': 5000,
            'valid': 5000,
            'train': 30000,
        }
    },










    '20230120.jpn.wordnet_repro_wo_proposition.D1_wo_dist': {


        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 1),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 0),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': False,
        'translation_vocab': 'wordnet',


        'split_sizes': {
            'test': 5000,
            'valid': 5000,
            'train': 30000,
        }
    },


    '20230120.jpn.wordnet_repro_wo_proposition.D1': {


        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 1),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': False,
        'translation_vocab': 'wordnet',


        'split_sizes': {
            'test': 5000,
            'valid': 5000,
            'train': 30000,
        }
    },



    '20230120.jpn.wordnet_repro_wo_proposition.D3': {


        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': False,
        'translation_vocab': 'wordnet',


        'split_sizes': {
            'test': 5000,
            'valid': 5000,
            'train': 30000,
        }
    },



    '20230120.jpn.wordnet_repro_wo_proposition.D8': {


        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 8),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': False,
        'translation_vocab': 'wordnet',


        'split_sizes': {
            'test': 5000,
            'valid': 5000,
            'train': 30000,
        }
    },











    '20230120.jpn.BCCWJ.D1_wo_dist': {


        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 1),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 0),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'BCCWJ',


        'split_sizes': {
            # 'test': 5000,
            'valid': 5000,
            'train': 30000,
        }
    },


    '20230120.jpn.BCCWJ.D1': {


        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 1),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'BCCWJ',


        'split_sizes': {
            # 'test': 5000,
            'valid': 5000,
            'train': 30000,
        }
    },



    '20230120.jpn.BCCWJ.D3': {


        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'BCCWJ',


        'split_sizes': {
            # 'test': 5000,
            'valid': 5000,
            'train': 30000,
        }
    },



    '20230120.jpn.BCCWJ.D8': {


        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 8),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'BCCWJ',


        'split_sizes': {
            # 'test': 5000,
            'valid': 5000,
            'train': 30000,
        }
    },















    '20230120.jpn.punipuni.D1_wo_dist': {


        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 1),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 0),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            # 'test': 5000,
            'valid': 5000,
            'train': 30000,
        }
    },


    '20230120.jpn.punipuni.D1': {


        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 1),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            # 'test': 5000,
            'valid': 5000,
            'train': 30000,
        }
    },



    '20230120.jpn.punipuni.D3': {


        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            # 'test': 5000,
            'valid': 5000,
            'train': 30000,
        }
    },



    '20230120.jpn.punipuni.D8': {


        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 8),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            # 'test': 5000,
            'valid': 5000,
            'train': 30000,
        }
    },


















    '20230122.jpn.ICL.punipuni.D1_wo_dist': {


        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 1),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 0),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            # 'train': 30000,
        }
    },


    '20230122.jpn.ICL.punipuni.D1': {


        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 1),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            # 'train': 30000,
        }
    },



    '20230122.jpn.ICL.punipuni.D3_wo_dist': {


        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 0),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            # 'train': 30000,
        }
    },




    '20230122.jpn.ICL.punipuni.D3': {


        'argument_configs': [
            # './configs/arguments/axioms/',
            # './configs/arguments/references/',

            './configs/arguments/predicate/axioms/and_or.json',
            './configs/arguments/predicate/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/negation.json',
            './configs/arguments/predicate/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/references/reference.json',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            # 'train': 30000,
        }
    },







    '2024-01-29.enhance_arguments.past_reproduce': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 500,
            # 'train': 300000,
        },

    },



    '2024-01-29.enhance_arguments.theorems': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems/',
            './configs/arguments/predicate/quantified/theorems',
            './configs/arguments/propositional/theorems/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            # 'test': 500,
            # 'valid': 500,
            'train': 300000,
        },

    },


    '2024-01-29.enhance_arguments.theorems.allow_smaller_proofs': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems/',
            './configs/arguments/predicate/quantified/theorems',
            './configs/arguments/propositional/theorems/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',

        'allow_smaller_proofs': True,


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            # 'test': 500,
            # 'valid': 500,
            'train': 300000,
        },

    },




    '2024-02-25.translation-augmentation.timeout_test': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 8),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 2000,
            # 'valid': 500,
            # 'train': 300000,
        },

    },



    '2024-01-29.enhance_arguments.past_reproduce.D8': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 8),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 500,
            # 'valid': 500,
            'train': 300000,
        },

    },



    '2024-02-09.enhance_translation.past_reproduce': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 2000,
            # 'valid': 500,
            # 'train': 300000,
        },

    },


    '2024-02-09.enhance_translation.D8': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 8),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 2000,
            # 'valid': 500,
            # 'train': 300000,
        },

    },


    '2024-02-09.enhance_translation.propositional-0.2': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 0.2,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 2000,
            # 'valid': 500,
            # 'train': 300000,
        },

    },


    '2024-02-09.enhance_translation.theorems': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems/',
            './configs/arguments/predicate/quantified/theorems',
            './configs/arguments/propositional/theorems/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 2000,
            # 'valid': 500,
            # 'train': 300000,
        },

    },


    '2024-02-09.enhance_translation.theorems.allow_smaller_proofs': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',
            './configs/arguments/propositional/theorems/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems/',
            './configs/arguments/predicate/quantified/theorems',
            './configs/arguments/propositional/theorems/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'allow_smaller_proofs': True,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 2000,
            # 'valid': 500,
            # 'train': 300000,
        },

    },


    '2024-02-09.enhance_translation.translation-v2': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 2000,
            # 'valid': 500,
            # 'train': 300000,
        },

    },


    '2024-02-09.enhance_translation.translation-v3': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v3'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 2000,
            # 'valid': 500,
            # 'train': 300000,
        },

    },



    



    '2024-02-14.translation_speedup.past_reproduce': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            # 'test': 2000,
            # 'valid': 500,
            'train': 300000,
        },

    },


    '2024-02-14.translation_speedup.D8': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 8),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            # 'test': 2000,
            # 'valid': 500,
            'train': 300000,
        },

    },


    '2024-02-14.translation_speedup.propositional-0.2': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 0.2,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            # 'test': 2000,
            # 'valid': 500,
            'train': 300000,
        },

    },


    '2024-02-14.translation_speedup.theorems': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems/',
            './configs/arguments/predicate/quantified/theorems',
            './configs/arguments/propositional/theorems/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            # 'test': 2000,
            # 'valid': 500,
            'train': 300000,
        },

    },


    '2024-02-14.translation_speedup.theorems.allow_smaller_proofs': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',
            './configs/arguments/propositional/theorems/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems/',
            './configs/arguments/predicate/quantified/theorems',
            './configs/arguments/propositional/theorems/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'allow_smaller_proofs': True,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            # 'test': 2000,
            # 'valid': 500,
            'train': 300000,
        },

    },


    '2024-02-14.translation_speedup.translation-v2': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 2000,
            # 'valid': 500,
            'train': 300000,
        },

    },


    '2024-02-14.translation_speedup.translation-v3': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v3'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            # 'test': 2000,
            # 'valid': 500,
            'train': 300000,
        },

    },


    '2024-02-14.translation_speedup.translation-v3.propositional-0.2': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 0.2,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v3'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 2000,
            # 'valid': 500,
            'train': 300000,
        },

    },



    '2024-02-14.translation_speedup.translation-v3.propositional-0.5': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v3'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 500,
            # 'train': 300000,
        },

    },





    '2024-02-14.translation_speedup.translation-v3': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v3'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            # 'test': 2000,
            # 'valid': 500,
            'train': 300000,
        },

    },





    '2024-03-29.JSAI_best': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v3'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 300000,
        },

    },




    '2024-03-29.JSAI_best.D8': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 8),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v3'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 300000,
        },

    },





    '2024-03-29.JSAI_best.theorems': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',
            './configs/arguments/propositional/theorems/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems/',
            './configs/arguments/predicate/quantified/theorems',
            './configs/arguments/propositional/theorems/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v3'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 300000,
        },

    },



    '2024-03-29.FLD_v2': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 300000,
        }

    },




    '2024-03-29.FLD_v2.D8': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 8),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        }

    },



    '2024-03-29.FLD_v2.theorems-0.03': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'theorem_arguments_factor': 0.03,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        }

    },


    '2024-03-29.FLD_v2.theorems-0.3.fix': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'theorem_arguments_factor': 0.3,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        }

    },



    '2024-03-29.FLD_v2.theorems-0.1.fix': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'theorem_arguments_factor': 0.1,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        }

    },




    '2024-03-29.FLD_v2.theorems-0.03.fix': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'theorem_arguments_factor': 0.03,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        }

    },




    '2024-03-29.JSAI_best.no_aug.trnsl-thing': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },





    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10.stps-3-3': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 3),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },

    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10.stps-5-5': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 5),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10.theorems-0.1': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.1,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10.theorems-0.2': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.2,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10.stps-3-0': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10.stps-1-2': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 1),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 2),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.stps-3-3': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 3),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.stps-5-3': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 5),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 3),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.stps-5-5': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 5),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.05': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.05,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.1': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.1,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.2': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.2,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.30': {

        'reference_tree_prob': 0.30,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.40': {

        'reference_tree_prob': 0.40,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.stps-3-0': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.stps-1-2': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 1),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 2),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.voc-100': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'limit_vocab_size_per_type': 100,


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-03-29.JSAI_best.no_aug.trnsl-thing.dstrct-0': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 0),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.rule-G_MP': {

        'argument_configs': [
            # './configs/arguments/predicate/specified/axioms/',
            # './configs/arguments/propositional/axioms/',

            # './configs/arguments/predicate/specified/references/',
            # './configs/arguments/propositional/references/',
            # './configs/arguments/predicate/quantified/references/',


            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/axioms/implication_elim.json',
            './configs/arguments/predicate/quantified/theorems/theorems/implication_elim.json',
            './configs/arguments/predicate/quantified/theorems/axioms/implication_elim.json',

        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-03-29.JSAI_best.no_aug.trnsl-thing.stps-3': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-03-29.JSAI_best.no_aug.trnsl-thing.rule-G_MP.stps-3': {

        'argument_configs': [
            # './configs/arguments/predicate/specified/axioms/',
            # './configs/arguments/propositional/axioms/',

            # './configs/arguments/predicate/specified/references/',
            # './configs/arguments/propositional/references/',
            # './configs/arguments/predicate/quantified/references/',


            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/axioms/implication_elim.json',
            './configs/arguments/predicate/quantified/theorems/theorems/implication_elim.json',
            './configs/arguments/predicate/quantified/theorems/axioms/implication_elim.json',

        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.stps-5-3': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 5),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 3),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-03-29.JSAI_best.no_aug.trnsl-thing.stps-8-0': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 8),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-03-29.JSAI_best.no_aug.trnsl-thing.stps-1-2': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 1),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 2),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.stps-1-1': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 1),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 1),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-03-29.JSAI_best.no_aug.trnsl-thing.stps-1-0': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 1),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.transl-small': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'use_fixed_translation': True,
        'reused_object_nouns_max_factor': 0.0,
        'translation_no_transitive_object': True,


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-03-29.JSAI_best.no_aug.trnsl-thing.transl-small.trnsl-old': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['old-thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'use_fixed_translation': True,
        'reused_object_nouns_max_factor': 0.0,
        'translation_no_transitive_object': True,


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },




    '2024-03-29.JSAI_best.no_aug.trnsl-thing.transl_sttng-0': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'use_fixed_translation': False,
        'reused_object_nouns_max_factor': 0.0,
        'translation_no_transitive_object': False,


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },




    '2024-03-29.JSAI_best.no_aug.trnsl-thing.transl_sttng-1': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'use_fixed_translation': False,
        'reused_object_nouns_max_factor': 1.0,
        'translation_no_transitive_object': True,


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems-0.03': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.03,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems-0.1': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.1,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems-0.3': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.3,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-v2': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-v2.theorems-0.03': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.03,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-v2.theorems-0.1': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.1,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-v2.theorems-0.3': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.3,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },




    '2024-03-29.JSAI_best.no_aug': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v3'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 300000,
        },

    },



    '2024-03-29.JSAI_best.no_aug.theorems-0.1': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.1,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v3'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-03-29.JSAI_best.no_aug.theorems-0.3': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.3,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v3'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.theorems-0.03': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.03,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v3'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-03-29.JSAI_best.D8.no_aug': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 8),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v3'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },





    '2024-03-29.JSAI_best.theorems.no_aug': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',
            './configs/arguments/propositional/theorems/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems/',
            './configs/arguments/predicate/quantified/theorems',
            './configs/arguments/propositional/theorems/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v3'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },




    '2024-03-29.JSAI_best.theorems-0.1.no_aug': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',
            './configs/arguments/propositional/theorems/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems/',
            './configs/arguments/predicate/quantified/theorems',
            './configs/arguments/propositional/theorems/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.1,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v3'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },




    '2024-03-29.JSAI_best.no_aug.dstrctr-10': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 10),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v3'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.cmplx-0.25': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.25,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v3'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-03-29.JSAI_best.no_aug.quant-0.5': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.5,
        'complex_formula_arguments_weight': 0.25,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v3'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },








    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.1.voc-100': {
        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.1,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'limit_vocab_size_per_type': 100,


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },




    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.1.dstrct-0': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.1,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 0),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.1.rule-G_MP': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            # './configs/arguments/predicate/specified/axioms/',
            # './configs/arguments/propositional/axioms/',

            # './configs/arguments/predicate/specified/references/',
            # './configs/arguments/propositional/references/',
            # './configs/arguments/predicate/quantified/references/',


            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/axioms/implication_elim.json',
            './configs/arguments/predicate/quantified/theorems/theorems/implication_elim.json',
            './configs/arguments/predicate/quantified/theorems/axioms/implication_elim.json',

        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.1,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },












    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.1.stps-3-0': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.1,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },











    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.1.transl_sttng-1': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.1,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'use_fixed_translation': False,
        'reused_object_nouns_max_factor': 1.0,
        'translation_no_transitive_object': True,


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },





    '2024-03-29.JSAI_best.no_aug.trnsl-thing.large': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            # 'test': 5000,
            # 'valid': 5000,
            # 'train': 100000,
            # 'train': 1000000,
            # 'train': 2000000,
            # 'train': 3000000,
            # 'train': 5000000,
            'train': 10000000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.4-4': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 4),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 4),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 5000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.5-3': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 5),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 3),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 5000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.1': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 5000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.1.debug': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15': {

        'reference_tree_prob': 0.15,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 5000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.1.theorems=0.1': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',

        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.1,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 5000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems=0.05': {

        # 'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',

        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.05,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 5000,
            # 'train': 100000,
        },

    },

    
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems=0.01': {

        # 'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',

        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.01,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 5000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems=0.01.adjust_theorems': {

        # 'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',

        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 5000,
            'train': 100000,
        },

    },

    '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems=0.03': {

        # 'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',

        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.03,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 5000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems=0.03.adjust_theorems': {

        # 'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',

        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.03,
        'adjust_theorem_argument_weight': True,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 5000,
            'train': 100000,
        },

    },

    '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems=0.05.adjust_theorems': {

        # 'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',

        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.05,
        'adjust_theorem_argument_weight': True,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 5000,
            'train': 100000,
        },

    },

    '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems=0.10.adjust_theorems': {

        # 'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',

        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.10,
        'adjust_theorem_argument_weight': True,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 5000,
            'train': 100000,
        },

    },

    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.1.theorems=0.2': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',

        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.2,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 5000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.2': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 5000,
            'train': 100000,
        },

    },


    '2024-03-29.JSAI_best.no_aug.trnsl-thing.steps': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 8),
        'extend_branches_steps_range': (0, 8),
        'steps_limit': 8,
        'depth_limit': None,
        'increase_depth_by_extend_branches': True,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 5000,
            'valid': 5000,
            'train': 100000,
        },

    },



    '2024-03-29.JSAI_best.no_aug.trnsl-thing.steps-5': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 5),
        'extend_branches_steps_range': (0, 5),
        'steps_limit': 5,
        'depth_limit': None,
        'increase_depth_by_extend_branches': True,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 5000,
            'valid': 5000,
            'train': 10000000,
        },

    },


    '20240419.20230120.jpn.wordnet_repro_w_proposition.reimpl.D3': {


        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_vocab': 'wordnet',


        'split_sizes': {
            'test': 5000,
            'valid': 5000,
            'train': 100000,
        }
    },








    '2024-07-02.debug_punipuni.0': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 5),
        'extend_branches_steps_range': (0, 5),
        'steps_limit': None,
        'depth_limit': None,
        'increase_depth_by_extend_branches': False,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            # 'train': 30000,
        }
    },


    '2024-07-02.debug_punipuni.1': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 5),
        'extend_branches_steps_range': (0, 5),
        'steps_limit': 3,
        'depth_limit': None,
        'increase_depth_by_extend_branches': False,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            # 'train': 30000,
        }
    },



    '2024-07-02.debug_punipuni.2': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 5),
        'extend_branches_steps_range': (0, 5),
        'steps_limit': None,
        'depth_limit': 3,
        'increase_depth_by_extend_branches': False,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            # 'train': 30000,
        }
    },



    '2024-07-02.debug_punipuni.3': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 5),
        'extend_branches_steps_range': (0, 5),
        'steps_limit': 8,
        'depth_limit': None,
        'increase_depth_by_extend_branches': True,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            # 'train': 30000,
        }
    },



    '2024-07-02.debug_punipuni.4': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),
        'steps_limit': 8,
        'depth_limit': None,
        'increase_depth_by_extend_branches': True,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            # 'train': 30000,
        }
    },










    '2024-07-08.JFLD.step-1': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 1),
        'extend_branches_steps_range': (0, 1),
        'steps_limit': 1,
        'depth_limit': None,
        'increase_depth_by_extend_branches': True,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 500,
            # 'valid': 500,
            'train': 500,
        }
    },


    '2024-07-08.JFLD.step-3': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 3),
        'steps_limit': 3,
        'depth_limit': None,
        'increase_depth_by_extend_branches': True,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 500,
            # 'valid': 500,
            'train': 500,
        }
    },



    '2024-07-08.JFLD.step-5': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 5),
        'extend_branches_steps_range': (0, 5),
        'steps_limit': 5,
        'depth_limit': None,
        'increase_depth_by_extend_branches': True,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 500,
            # 'valid': 500,
            'train': 500,
        }
    },











    '2024-07-08.JFLD.cmpl-0.2.step-1': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.2,


        'generate_stem_steps_range': (1, 1),
        'extend_branches_steps_range': (0, 1),
        'steps_limit': 1,
        'depth_limit': None,
        'increase_depth_by_extend_branches': True,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 500,
            # 'valid': 500,
            'train': 500,
        }
    },




    '2024-07-08.JFLD.cmpl-0.2.step-3': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.2,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 3),
        'steps_limit': 3,
        'depth_limit': None,
        'increase_depth_by_extend_branches': True,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 500,
            # 'valid': 500,
            'train': 500,
        }
    },



    '2024-07-08.JFLD.cmpl-0.2.step-5': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.2,


        'generate_stem_steps_range': (1, 5),
        'extend_branches_steps_range': (0, 5),
        'steps_limit': 5,
        'depth_limit': None,
        'increase_depth_by_extend_branches': True,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 500,
            # 'valid': 500,
            'train': 500,
        }
    },






    '2024-07-08.JFLD.dstrct-5.step-1': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 1),
        'extend_branches_steps_range': (0, 1),
        'steps_limit': 1,
        'depth_limit': None,
        'increase_depth_by_extend_branches': True,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 5),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 500,
            # 'valid': 500,
            'train': 500,
        }
    },



    '2024-07-08.JFLD.dstrct-5.step-3': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 3),
        'steps_limit': 3,
        'depth_limit': None,
        'increase_depth_by_extend_branches': True,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 5),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 500,
            # 'valid': 500,
            'train': 500,
        }
    },



    '2024-07-08.JFLD.dstrct-5.step-5': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 5),
        'extend_branches_steps_range': (0, 5),
        'steps_limit': 5,
        'depth_limit': None,
        'increase_depth_by_extend_branches': True,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 5),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 500,
            # 'valid': 500,
            'train': 500,
        }
    },










    '2024-07-08.JFLD.cmpl-0.2.dstrct-5.step-1': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.2,


        'generate_stem_steps_range': (1, 1),
        'extend_branches_steps_range': (0, 1),
        'steps_limit': 1,
        'depth_limit': None,
        'increase_depth_by_extend_branches': True,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 5),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 3000,
            # 'valid': 3000,
            'train': 3000,
        }
    },


    '2024-07-08.JFLD.cmpl-0.2.dstrct-5.step-2': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.2,


        'generate_stem_steps_range': (1, 2),
        'extend_branches_steps_range': (0, 2),
        'steps_limit': 2,
        'depth_limit': None,
        'increase_depth_by_extend_branches': True,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 5),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 3000,
            # 'valid': 3000,
            'train': 3000,
        }
    },


    '2024-07-08.JFLD.cmpl-0.2.dstrct-5.step-3': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.2,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 3),
        'steps_limit': 3,
        'depth_limit': None,
        'increase_depth_by_extend_branches': True,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 5),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 3000,
            # 'valid': 3000,
            'train': 3000,
        }
    },


    '2024-07-08.JFLD.cmpl-0.2.dstrct-5.step-5': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.2,


        'generate_stem_steps_range': (1, 5),
        'extend_branches_steps_range': (0, 5),
        'steps_limit': 5,
        'depth_limit': None,
        'increase_depth_by_extend_branches': True,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 5),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': ['punipuni.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'translation_no_transitive_object': True,
        'translation_vocab': 'punipuni',


        'split_sizes': {
            'test': 3000,
            # 'valid': 3000,
            'train': 3000,
        }
    },













    '2024-03-29.JSAI_best.no_aug.trnsl-thing.voc-100.fixed': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'limit_vocab_size_per_type': 200,


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-03-29.JSAI_best.no_aug.trnsl-thing.voc-50.fixed': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'limit_vocab_size_per_type': 50,


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },





    '2024-03-29.JSAI_best.no_aug.trnsl-thing.voc-50.fixed.ref_prob=0.20.theorems-0.1': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.1,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'limit_vocab_size_per_type': 50,


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-03-29.JSAI_best.no_aug.trnsl-thing.transl_sttng-1.ref_prob=0.20.theorems-0.1': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.1,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'use_fixed_translation': False,
        'reused_object_nouns_max_factor': 1.0,
        'translation_no_transitive_object': True,


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },




    '2024-03-29.JSAI_best.no_aug.trnsl-thing.rule-G_MP.ref_prob=0.20.theorems-0.1': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            # './configs/arguments/predicate/specified/axioms/',
            # './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',


            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/axioms/implication_elim.json',
            './configs/arguments/predicate/quantified/theorems/theorems/implication_elim.json',
            './configs/arguments/predicate/quantified/theorems/axioms/implication_elim.json',

        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.1,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },





    '2024-03-29.JSAI_best.no_aug.trnsl-thing.transl-small.ref_prob=0.20.theorems-0.1': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.1,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'use_fixed_translation': True,
        'reused_object_nouns_max_factor': 0.0,
        'translation_no_transitive_object': True,


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },






    '2024-03-29.JSAI_best.no_aug.trnsl-thing.transl-small.trnsl-old.ref_prob=0.20.theorems-0.1': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.1,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['old-thing.v1'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'use_fixed_translation': True,
        'reused_object_nouns_max_factor': 0.0,
        'translation_no_transitive_object': True,


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },

















    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-v2': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-v3': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v3'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },

    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.05': {

        'reference_tree_prob': 0.05,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },

    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15': {

        'reference_tree_prob': 0.15,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15.steps-3-4': {

        'reference_tree_prob': 0.15,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 4),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },

    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15.steps-4-4': {

        'reference_tree_prob': 0.15,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 4),
        'extend_branches_steps_range': (0, 4),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15.steps-4-5': {

        'reference_tree_prob': 0.15,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 4),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },




    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15.steps-5-3': {

        'reference_tree_prob': 0.15,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 5),
        'extend_branches_steps_range': (0, 3),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15.steps-5': {

        'reference_tree_prob': 0.15,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 5),
        'extend_branches_steps_range': (0, 5),
        'steps_limit': 5,
        'depth_limit': None,
        'increase_depth_by_extend_branches': True,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },




    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15.steps-8': {

        'reference_tree_prob': 0.15,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 8),
        'extend_branches_steps_range': (0, 8),
        'steps_limit': 8,
        'depth_limit': None,
        'increase_depth_by_extend_branches': True,


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob_in_1=0.10': {

        'reference_argument_prob_in_depth_1': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },

    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob_in_1=0.25': {

        'reference_argument_prob_in_depth_1': 0.25,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },




    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob_in_1=0.5': {

        'reference_argument_prob_in_depth_1': 0.5,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },




    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob_in_1=0.5.theorems=0.01': {

        'reference_argument_prob_in_depth_1': 0.5,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.01,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },




    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob_in_1=0.5.theorems=0.03': {

        'reference_argument_prob_in_depth_1': 0.5,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.03,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob_in_1=0.5.theorems=0.03.adjust_theorems': {

        'reference_argument_prob_in_depth_1': 0.5,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.03,
        'adjust_theorem_argument_weight': True,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-08-09.depth_fix.2024-03-29.FLD_v2': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            # 'train': 100000,
            'train': 300000,
        }

    },



    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            # 'train': 100000,
            'train': 300000,
        }

    },


    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.ref_prob-0.05': {

        'reference_tree_prob': 0.05,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        }

    },


    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.ref_prob-0.20': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        }

    },



    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.15': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            # 'train': 100000,
            'train': 200000,
        }

    },




    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.05': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.05,
        'adjust_theorem_argument_weight': True,



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 200000,
        }

    },



    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.15.w_flag': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 200000,
        }

    },


    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.15.w_flag.super_theorems': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            # 'train': 100000,
            'train': 300000,
        }

    },


    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.15.w_flag.super_theorems.ref_prob=0.20': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            # 'train': 100000,
            'train': 150000,
        }

    },

    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.15.w_flag.super_theorems.syllogism': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            # 'train': 100000,
            'train': 300000,
        }

    },


    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.15.w_flag.super_theorems.syllogism.contraposition': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            # 'train': 100000,
            'train': 300000,
        }

    },


    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.15.w_flag.super_theorems.syllogism.contraposition.and_interchangeability': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            # 'train': 100000,
            'train': 300000,
        }

    },

    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.05.w_flag': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.05,
        'adjust_theorem_argument_weight': True,



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 200000,
        }

    },


    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.25.w_flag': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'theorem_tree_prob': 0.25,
        'theorem_arguments_factor': 0.05,
        'adjust_theorem_argument_weight': True,



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 200000,
        }

    },

    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.wo_suppress_if': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0.wo_suppress_if'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        }

    },


    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.wo_phrase': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0.wo_phrase'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        }

    },


    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.wo_clause': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0.wo_clause'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        }

    },



    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v2': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            # 'train': 100000,
            'train': 300000,
        }

    },


    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v2.ref_prob-0.1': {

        'reference_tree_prob': 0.10,

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        }

    },


    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v2.ref_prob-0.126': {

        'reference_tree_prob': 0.126,

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        }

    },

    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v2.ref_prob-0.1.theorems-0.25': {

        'reference_tree_prob': 0.10,

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'theorem_tree_prob': 0.25,
        'theorem_arguments_factor': 0.1,
        'adjust_theorem_argument_weight': True,



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        }

    },


    '2024-08-12.neurips_camera_ready.towards_best_corpora': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },




    '2024-08-12.neurips_camera_ready.towards_best_corpora.wo_trnsl-v2': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },




    '2024-08-12.neurips_camera_ready.towards_best_corpora.wo_theorems': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.00,
        'adjust_theorem_argument_weight': True,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },




    '2024-08-12.neurips_camera_ready.towards_best_corpora.suppress_dilemma': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-08-12.neurips_camera_ready.towards_best_corpora.suppress_dilemma.theorems-0.003': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.003,
        'adjust_theorem_argument_weight': True,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorems-0.0001': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_arguments_factor': 0.0001,
        'adjust_theorem_argument_weight': True,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },







    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem_tree_prob-0.1': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_tree_prob': 0.0,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            # 'train': 100000,
        },

    },




    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--1.0--0.1': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_tree_prob': 1.0,
        'theorem_arguments_factor': 0.1,
        'adjust_theorem_argument_weight': True,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },




    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--0.5--0.1': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_tree_prob': 0.5,
        'theorem_arguments_factor': 0.1,
        'adjust_theorem_argument_weight': True,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--0.25--0.1': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_tree_prob': 0.25,
        'theorem_arguments_factor': 0.1,
        'adjust_theorem_argument_weight': True,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },






    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--0.25--0.1.G_MP-3': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_tree_prob': 0.25,
        'theorem_arguments_factor': 0.1,
        'adjust_theorem_argument_weight': True,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },

    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--0.25--0.1.G_MP-10': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_tree_prob': 0.25,
        'theorem_arguments_factor': 0.1,
        'adjust_theorem_argument_weight': True,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--0.10--0.1': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_tree_prob': 0.10,
        'theorem_arguments_factor': 0.1,
        'adjust_theorem_argument_weight': True,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },



    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--1.0--0.01': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_tree_prob': 1.0,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },




    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--0.5--0.01': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_tree_prob': 0.5,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },


    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--0.25--0.01': {

        'reference_tree_prob': 0.10,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'propositional_arguments_factor': 1.0,
        'theorem_tree_prob': 0.25,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,


        'generate_stem_steps_range': (1, 3),
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        },

    },




    '2024-08-16.neurips_camera_ready.FLD.small_vocab': {

        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,
        'limit_vocab_size_per_type': 5000,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 100000,
        }

    },




    '2024-08-30.FLD.ref_prob-0.20': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,
        'limit_vocab_size_per_type': 5000,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            'train': 300000,
        }

    },



    '2024-08-30.trnsl-thing_person-v0.ref_prob-0.20': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            'train': 300000,
        }
    },


    '2024-08-30.trnsl-thing_person-v0.ref_prob-0.20.theorem-G_MP': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,

        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,
        'theorem_subset': 'G_MP',



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            'train': 300000,
        }
    },


    '2024-08-30.trnsl-thing_person-v0.ref_prob-0.066.theorem-G_MP': {

        'reference_tree_prob': 0.066,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,

        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,
        'theorem_subset': 'G_MP',



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            'train': 300000,
        }
    },
    '2024-08-30.trnsl-thing_person-v0.ref_prob-0.20.theorem-G_MP.syllogism': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,

        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,
        'theorem_subset': 'G_MP.syllogism',



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            'train': 300000,
        }
    },




    '2024-08-30.trnsl-thing_person-v0.ref_prob-0.20.theorem-G_MP.syllogism.contraposition': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,

        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,
        'theorem_subset': 'G_MP.syllogism.contraposition',



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            'train': 300000,
        }
    },



    '2024-08-30.trnsl-thing_person-v0.ref_prob-0.20.theorem-G_MP.syllogism.contraposition.interchangeability': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,

        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,
        'theorem_subset': 'G_MP.syllogism.contraposition.interchangeability',



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            'train': 300000,
        }
    },


    '2024-08-30.trnsl-thing_person-v0.ref_prob-0.13.theorem-G_MP.syllogism.contraposition.interchangeability': {

        'reference_tree_prob': 0.13,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,

        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,
        'theorem_subset': 'G_MP.syllogism.contraposition.interchangeability',



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            'train': 150000,
        }
    },


    '2024-08-30.trnsl-thing_person-v0.ref_prob-0.05.theorem-G_MP.syllogism.contraposition.interchangeability': {

        'reference_tree_prob': 0.05,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,

        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,
        'theorem_subset': 'G_MP.syllogism.contraposition.interchangeability',



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            'train': 150000,
        }
    },
    '2024-08-30.trnsl-thing_person-v0.ref_prob-0.20.theorem-all': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,

        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,
        'theorem_subset': 'all',



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            'train': 300000,
        }
    },











    '2024-09-03.trnsl-thing_person-v2': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,

        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,
        'theorem_subset': 'G_MP.syllogism.contraposition.interchangeability',



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            'train': 200000,
        }
    },



     '2024-09-03.trnsl-thing_person-v2.voc-100': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,

        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,
        'theorem_subset': 'G_MP.syllogism.contraposition.interchangeability',



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'limit_vocab_size_per_type': 50,


        'split_sizes': {
            'test': 1000,
            'train': 150000,
        }
    },   



    '2024-09-03.trnsl-thing_person-v2.dstrct-0': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,

        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,
        'theorem_subset': 'G_MP.syllogism.contraposition.interchangeability',



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 0),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            'train': 150000,
        }
    },


    '2024-09-03.trnsl-thing_person-v2.rule-G_MP': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            # './configs/arguments/predicate/specified/axioms/',
            # './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',


            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/axioms/implication_elim.json',
            './configs/arguments/predicate/quantified/theorems/theorems/implication_elim.json',
            './configs/arguments/predicate/quantified/theorems/axioms/implication_elim.json',

        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,

        'theorem_tree_prob': 0.75,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': False,
        'theorem_subset': 'all',



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            'train': 150000,
        }
    },



    '2024-09-03.trnsl-thing_person-v2.stps-3-0': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,

        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,
        'theorem_subset': 'G_MP.syllogism.contraposition.interchangeability',



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            'train': 150000,
        }
    },



    '2024-09-03.trnsl-thing_person-v2.trnsl-small': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,

        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,
        'theorem_subset': 'G_MP.syllogism.contraposition.interchangeability',



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v2'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'use_fixed_translation': True,
        'reused_object_nouns_max_factor': 0.0,
        'translation_no_transitive_object': True,


        'split_sizes': {
            'test': 1000,
            'train': 150000,
        }
    },











    '2024-09-03.trnsl-thing_person-v0': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,

        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,
        'theorem_subset': 'G_MP.syllogism.contraposition.interchangeability',



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            'train': 1000000,
        }
    },



     '2024-09-03.trnsl-thing_person-v0.voc-100': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,

        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,
        'theorem_subset': 'G_MP.syllogism.contraposition.interchangeability',



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'limit_vocab_size_per_type': 50,


        'split_sizes': {
            'test': 1000,
            'train': 150000,
        }
    },   



    '2024-09-03.trnsl-thing_person-v0.dstrct-0': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,

        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,
        'theorem_subset': 'G_MP.syllogism.contraposition.interchangeability',



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 0),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            'train': 150000,
        }
    },


    '2024-09-03.trnsl-thing_person-v0.rule-G_MP': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            # './configs/arguments/predicate/specified/axioms/',
            # './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',


            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/specified/axioms/implication_elim.json',
            './configs/arguments/predicate/quantified/theorems/theorems/implication_elim.json',
            './configs/arguments/predicate/quantified/theorems/axioms/implication_elim.json',

        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,

        'theorem_tree_prob': 0.75,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': False,
        'theorem_subset': 'all',



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            'train': 150000,
        }
    },



    '2024-09-03.trnsl-thing_person-v0.stps-3-0': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,

        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,
        'theorem_subset': 'G_MP.syllogism.contraposition.interchangeability',



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 0),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            'train': 150000,
        }
    },



    '2024-09-03.trnsl-thing_person-v0.trnsl-small': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',

            './configs/arguments/predicate/specified/theorems',
            './configs/arguments/propositional/theorems',
            './configs/arguments/predicate/quantified/theorems',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,

        'theorem_tree_prob': 0.15,
        'theorem_arguments_factor': 0.01,
        'adjust_theorem_argument_weight': True,
        'theorem_subset': 'G_MP.syllogism.contraposition.interchangeability',



        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_configs': ['thing_person.v0'],
        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',
        'use_fixed_translation': True,
        'reused_object_nouns_max_factor': 0.0,
        'translation_no_transitive_object': True,


        'split_sizes': {
            'test': 1000,
            'train': 150000,
        }
    },








    '2024-09-16.FLD.fix_negation': {

        'reference_tree_prob': 0.20,
        'argument_configs': [
            './configs/arguments/predicate/specified/axioms/',
            './configs/arguments/propositional/axioms/',

            './configs/arguments/predicate/specified/references/',
            './configs/arguments/propositional/references/',
            './configs/arguments/predicate/quantified/references/',
        ],
        'quantifier_axioms': [
            'universal_quantifier_elim',
            'universal_quantifier_intro',
            'existential_quantifier_intro',
            'existential_quantifier_elim',
        ],
        'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.5,
        'negation_arguments_weight': 0.1,


        'generate_stem_steps_range': (1, 3),
        'generate_stem_steps_distrib': 'flat',
        'extend_branches_steps_range': (0, 5),


        'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': False,
        'limit_vocab_size_per_type': 5000,


        'translation_volume_to_weight': 'log10',
        'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 1000,
            # 'valid': 1000,
            # 'train': 300000,
        }

    },






}










_DATASET_NAME_TO_DEFAULT = {

    # =================================- 20230701.finalize ====================================
    '20230701.D3.default': '20230626.many_bugs_fixed',
    '20230701.D3.debug': '20230626.many_bugs_fixed',
    '20230701.D3.wo_transl_dist': '20230626.many_bugs_fixed',
    '20230701.D3.brnch-small': '20230626.many_bugs_fixed',
    '20230701.D3.dist-small': '20230626.many_bugs_fixed',
    '20230701.D3.default.refactor_test': '20230626.many_bugs_fixed',
    '20230701.D3.default.dist-tree-triple': '20230626.many_bugs_fixed',
    '20230701.D3.default.dist-tree-quadruple': '20230626.many_bugs_fixed',

    '20230701.D8.default': '20230626.many_bugs_fixed',


    # =================================- 20230706.finalize ====================================
    '20230706.finalize.D3.dist-double': '20230626.many_bugs_fixed', 
    '20230706.finalize.D3.dist-quadruple': '20230626.many_bugs_fixed', 
    '20230706.finalize.D8.dist-double': '20230626.many_bugs_fixed', 
    '20230706.finalize.D8.dist-quadruple': '20230626.many_bugs_fixed', 


    # =================================- 20230707.finalize ====================================
    '20230707.finalize.D3.dist-double': '20230626.many_bugs_fixed', 
    '20230707.finalize.D3.dist-triple': '20230626.many_bugs_fixed', 
    '20230707.finalize.D3.dist-quadruple': '20230626.many_bugs_fixed', 

    '20230707.finalize.D8.dist-double': '20230626.many_bugs_fixed', 
    '20230707.finalize.D8.dist-triple': '20230626.many_bugs_fixed', 
    '20230707.finalize.D8.dist-quadruple': '20230626.many_bugs_fixed', 

    # =================================- 20230711.finalize ====================================
    '20230711.dist-fallback': '20230626.many_bugs_fixed',
    '20230711.finalize.D3': '20230626.many_bugs_fixed',
    '20230711.finalize.D8': '20230626.many_bugs_fixed',

    # =================================- 20230718.case_study ====================================
    '20230718.case_study.D3.dist-mixture': '20230626.many_bugs_fixed',
    '20230718.case_study.D3.num_dist-wide': '20230626.many_bugs_fixed',
    '20230718.case_study.D3.dist-mixture.num_dist-wide': '20230626.many_bugs_fixed',
    '20230718.case_study.D3.dist-mixture.num_dist-wide.transl_vol_logE': '20230626.many_bugs_fixed',
    '20230718.case_study.D3.dist-mixture.num_dist-wide.transl_vol_log10': '20230626.many_bugs_fixed',
    '20230718.case_study.D3.dist-mixture.num_dist-wide.transl_vol_log10.adj_verb_noun_equal': '20230626.many_bugs_fixed',
    '20230718.case_study.D8.dist-mixture.num_dist-wide': '20230626.many_bugs_fixed',

    # =================================- 20230729.case_study_finalize ====================================
    '20230729.case_study_finalize.D3': '20230626.many_bugs_fixed',
    '20230729.case_study_finalize.D8': '20230626.many_bugs_fixed',

    # =================================- 20230826.jpn ====================================
    '20230826.jpn.D3': '20230626.many_bugs_fixed',
    '20230826.jpn.D8': '20230626.many_bugs_fixed',

    # =================================- 20230901.random_transitive_verbs ====================================
    '20230901.random_transitive_verbs.D3': '20230626.many_bugs_fixed',
    '20230901.random_transitive_verbs.D8': '20230626.many_bugs_fixed',

    # =================================- 20230904.jpn ====================================
    '20230904.jpn.D1.wo_brnch.wo_dstrct': '20230626.many_bugs_fixed', 
    '20230904.jpn.D1.wo_brnch': '20230626.many_bugs_fixed', 
    '20230904.jpn.D1': '20230626.many_bugs_fixed', 
    '20230904.jpn.D3': '20230626.many_bugs_fixed', 

    # =================================- 20230912.jpn ====================================
    '20230912.jpn.D3': '20230626.many_bugs_fixed',

    # =================================- 20230914.jpn ====================================
    '20230914.jpn.D3': '20230626.many_bugs_fixed',

    # =================================- 20230916.jpn ====================================
    '20230916.jpn.D1_wo_dist': '20230626.many_bugs_fixed',
    '20230916.jpn.D1': '20230626.many_bugs_fixed',
    '20230916.jpn.D3': '20230626.many_bugs_fixed',
    '20230916.jpn.D5': '20230626.many_bugs_fixed',

    # =================================- 20231203.jpn ====================================
    '20231203.jpn.D1_wo_dist': '20231018.thing_person_config_translation',
    '20231203.jpn.D1': '20231018.thing_person_config_translation',
    '20231203.jpn.D3': '20231018.thing_person_config_translation',
    '20231203.jpn.D5': '20231018.thing_person_config_translation',
    '20231203.jpn.D8': '20231018.thing_person_config_translation',

    # =================================- 20231213.jpn ====================================
    '20231213.jpn.D1_wo_dist': '20231018.thing_person_config_translation',
    '20231213.jpn.D1': '20231018.thing_person_config_translation',
    '20231213.jpn.D3': '20231018.thing_person_config_translation',
    '20231213.jpn.D5': '20231018.thing_person_config_translation',
    '20231213.jpn.D8': '20231018.thing_person_config_translation',

    # =================================- 20230115.jpn ====================================
    '20230115.jpn.BCCWJ.D3': '20231018.thing_person_config_translation',
    '20230115.jpn.punipuni.D3': '20231018.thing_person_config_translation',

    # =================================- 20230116.jpn ====================================
    '20230116.jpn.wordnet.D3': '20231018.thing_person_config_translation',
    '20230116.jpn.BCCWJ.D3.argument_pred_arg_only': '20231018.thing_person_config_translation',
    '20230116.jpn.punipuni.D3.argument_pred_arg_only': '20231018.thing_person_config_translation',

    # =================================- 20230116.jpn ====================================
    '20230118.jpn.wordnet.D3': '20231018.thing_person_config_translation',
    '20230118.jpn.wordnet.D3.argument_pred_arg_only': '20231018.thing_person_config_translation',
    '20230118.jpn.wordnet.D3.argument_pred_arg_only.no_kaku': '20231018.thing_person_config_translation',
    '20230118.jpn.BCCWJ.D3': '20231018.thing_person_config_translation',
    '20230118.jpn.punipuni.D3': '20231018.thing_person_config_translation',

    # =================================- 20230118.jpn.ICL ====================================
    '20230118.jpn.wordnet.D3.extension-3.distractor-10': '20231018.thing_person_config_translation',
    '20230118.jpn.wordnet.D3.extension-3.distractor-5': '20231018.thing_person_config_translation',
    '20230118.jpn.wordnet.D3.extension-3.distractor-3': '20231018.thing_person_config_translation',
    '20230118.jpn.wordnet.D3.extension-2.distractor-5': '20231018.thing_person_config_translation',
    '20230118.jpn.wordnet.D3.extension-2.distractor-3': '20231018.thing_person_config_translation',
    '20230118.jpn.wordnet.D3.extension-1.distractor-5': '20231018.thing_person_config_translation',
    '20230118.jpn.wordnet.D3.extension-1.distractor-3': '20231018.thing_person_config_translation',

    # =================================- 20230120.jpn.punipuni ====================================
    '20230120.jpn.wordnet.D3': '20231018.thing_person_config_translation',

    '20230120.jpn.wordnet_repro_w_proposition.D1_wo_dist': '20231018.thing_person_config_translation',
    '20230120.jpn.wordnet_repro_w_proposition.D1': '20231018.thing_person_config_translation',
    '20230120.jpn.wordnet_repro_w_proposition.D3': '20231018.thing_person_config_translation',
    '20230120.jpn.wordnet_repro_w_proposition.D8': '20231018.thing_person_config_translation',

    '20230120.jpn.wordnet_repro_wo_proposition.D1_wo_dist': '20231018.thing_person_config_translation',
    '20230120.jpn.wordnet_repro_wo_proposition.D1': '20231018.thing_person_config_translation',
    '20230120.jpn.wordnet_repro_wo_proposition.D3': '20231018.thing_person_config_translation',
    '20230120.jpn.wordnet_repro_wo_proposition.D8': '20231018.thing_person_config_translation',

    '20230120.jpn.BCCWJ.D1_wo_dist': '20231018.thing_person_config_translation',
    '20230120.jpn.BCCWJ.D1': '20231018.thing_person_config_translation',
    '20230120.jpn.BCCWJ.D3': '20231018.thing_person_config_translation',
    '20230120.jpn.BCCWJ.D8': '20231018.thing_person_config_translation',

    '20230120.jpn.punipuni.D1_wo_dist': '20231018.thing_person_config_translation',
    '20230120.jpn.punipuni.D1': '20231018.thing_person_config_translation',
    '20230120.jpn.punipuni.D3': '20231018.thing_person_config_translation',
    '20230120.jpn.punipuni.D8': '20231018.thing_person_config_translation',


    # =================================- 20230122.jpn.ICL ====================================
    '20230122.jpn.ICL.punipuni.D1_wo_dist': '20231018.thing_person_config_translation',
    '20230122.jpn.ICL.punipuni.D1': '20231018.thing_person_config_translation',
    '20230122.jpn.ICL.punipuni.D3_wo_dist': '20231018.thing_person_config_translation',
    '20230122.jpn.ICL.punipuni.D3': '20231018.thing_person_config_translation',



    # ==============================- production ==============================--
    '2024-03-29.FLD_v2.D8': '20230626.many_bugs_fixed',


    '2024-03-29.FLD_v2': '20230626.many_bugs_fixed',
    '2024-03-29.FLD_v2.theorems-0.03': '20230626.many_bugs_fixed',
    '2024-03-29.FLD_v2.theorems-0.3.fix': '20230626.many_bugs_fixed',
    '2024-03-29.FLD_v2.theorems-0.1.fix': '20230626.many_bugs_fixed',
    '2024-03-29.FLD_v2.theorems-0.03.fix': '20230626.many_bugs_fixed',

    '2024-03-29.JSAI_best.no_aug.trnsl-thing': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems-0.3': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems-0.1': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems-0.03': '20231018.thing_person_config_translation',

    '2024-03-29.JSAI_best.no_aug.trnsl-v2': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-v2.theorems-0.3': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-v2.theorems-0.1': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-v2.theorems-0.03': '20231018.thing_person_config_translation',

    '2024-03-29.JSAI_best.no_aug': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.theorems-0.3': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.theorems-0.1': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.theorems-0.03': '20231018.thing_person_config_translation',


    # ==============================- 2024-05-03.ablation ==============================--
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.voc-100': '20231018.thing_person_config_translation',

    '2024-03-29.JSAI_best.no_aug.trnsl-thing.dstrct-0': '20231018.thing_person_config_translation',

    '2024-03-29.JSAI_best.no_aug.trnsl-thing.stps-3': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.stps-5-3': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.stps-8-0': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.stps-1-2': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.stps-1-1': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.stps-1-0': '20231018.thing_person_config_translation',

    '2024-03-29.JSAI_best.no_aug.trnsl-thing.rule-G_MP': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.rule-G_MP.stps-3': '20231018.thing_person_config_translation',

    '2024-03-29.JSAI_best.no_aug.trnsl-thing.transl_sttng-0': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.transl_sttng-1': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.transl-small': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.transl-small.trnsl-old': '20231018.thing_person_config_translation',


    # =================================-- ./outputs/00.create_corpus/2024-05-08.ref_prob ========================--
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10.stps-3-0': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10.stps-1-2': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10.stps-3-3': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10.stps-5-5': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10.theorems-0.1': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10.theorems-0.2': '20231018.thing_person_config_translation',

    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.stps-3-0': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.stps-1-2': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.stps-3-3': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.stps-5-3': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.stps-5-5': '20231018.thing_person_config_translation',

    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.05': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.1': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.2': '20231018.thing_person_config_translation',

    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.30': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.40': '20231018.thing_person_config_translation',

    # ====================================- ./outputs/00.create_corpus/2024-05-19.ablation_with_theorems ========================--
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.1.voc-100': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.1.dstrct-0': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.1.rule-G_MP': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.1.stps-3-0': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.1.transl_sttng-1': '20231018.thing_person_config_translation',


    # ====================================- ./outputs/00.create_corpus/2024-06-08.LPT ========================--
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.large': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.steps': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.steps-5': '20231018.thing_person_config_translation',

    # ====================================-- transfer ================================================--
    '20240419.20230120.jpn.wordnet_repro_w_proposition.reimpl.D3': '20231018.thing_person_config_translation',


    # ====================================-- 2024-07-02.debug_punipuni =============================================-
    '2024-07-02.debug_punipuni.0': '20231018.thing_person_config_translation',
    '2024-07-02.debug_punipuni.1': '20231018.thing_person_config_translation',
    '2024-07-02.debug_punipuni.2': '20231018.thing_person_config_translation',
    '2024-07-02.debug_punipuni.3': '20231018.thing_person_config_translation',
    '2024-07-02.debug_punipuni.4': '20231018.thing_person_config_translation',


    # ====================================-- 2024-07-08.JFLD =============================================-
    '2024-07-08.JFLD.step-1': '20231018.thing_person_config_translation',
    '2024-07-08.JFLD.step-3': '20231018.thing_person_config_translation',
    '2024-07-08.JFLD.step-5': '20231018.thing_person_config_translation',
    '2024-07-08.JFLD.cmpl-0.2.step-1': '20231018.thing_person_config_translation',
    '2024-07-08.JFLD.cmpl-0.2.step-3': '20231018.thing_person_config_translation',
    '2024-07-08.JFLD.cmpl-0.2.step-5': '20231018.thing_person_config_translation',
    '2024-07-08.JFLD.dstrct-5.step-1': '20231018.thing_person_config_translation',
    '2024-07-08.JFLD.dstrct-5.step-3': '20231018.thing_person_config_translation',
    '2024-07-08.JFLD.dstrct-5.step-5': '20231018.thing_person_config_translation',

    '2024-07-08.JFLD.cmpl-0.2.dstrct-5.step-1': '20231018.thing_person_config_translation',
    '2024-07-08.JFLD.cmpl-0.2.dstrct-5.step-2': '20231018.thing_person_config_translation',
    '2024-07-08.JFLD.cmpl-0.2.dstrct-5.step-3': '20231018.thing_person_config_translation',
    '2024-07-08.JFLD.cmpl-0.2.dstrct-5.step-5': '20231018.thing_person_config_translation',


    # =================================== 2024-07-21.neurips_additional ========================================
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.voc-100.fixed': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.voc-50.fixed': '20231018.thing_person_config_translation',

    '2024-03-29.JSAI_best.no_aug.trnsl-thing.voc-50.fixed.ref_prob=0.20.theorems-0.1': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.transl_sttng-1.ref_prob=0.20.theorems-0.1': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.transl-small.ref_prob=0.20.theorems-0.1': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.transl-small.trnsl-old.ref_prob=0.20.theorems-0.1': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.rule-G_MP.ref_prob=0.20.theorems-0.1': '20231018.thing_person_config_translation',

    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.1': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.1.theorems=0.1': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.1.theorems=0.2': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.2': '20231018.thing_person_config_translation',

    '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems=0.01': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems=0.03': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems=0.05': '20231018.thing_person_config_translation',

    '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems=0.01.adjust_theorems': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems=0.03.adjust_theorems': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems=0.05.adjust_theorems': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems=0.10.adjust_theorems': '20231018.thing_person_config_translation',

    '2024-03-29.JSAI_best.no_aug.trnsl-thing.4-4': '20231018.thing_person_config_translation',
    '2024-03-29.JSAI_best.no_aug.trnsl-thing.5-3': '20231018.thing_person_config_translation',

    '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.1.debug': '20231018.thing_person_config_translation',



    # =================================== 2024-08-09.fix_depth_problem ========================================
    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-v2': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-v3': '20231018.thing_person_config_translation',

    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.05': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15': '20231018.thing_person_config_translation',

    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15.steps-3-4': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15.steps-4-4': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15.steps-4-5': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15.steps-5-3': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.r2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10ef_prob=0.15.steps-5': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15.steps-8': '20231018.thing_person_config_translation',

    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob_in_1=0.10': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob_in_1=0.25': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob_in_1=0.5': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob_in_1=0.5.theorems=0.01': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob_in_1=0.5.theorems=0.03': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob_in_1=0.5.theorems=0.03.adjust_theorems': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.FLD_v2': '20230626.many_bugs_fixed',


    # =================================== 2024-08-12.neurips_camera_ready.towards_best_corpora ========================================
    '2024-08-12.neurips_camera_ready.towards_best_corpora': '20231018.thing_person_config_translation',
    '2024-08-12.neurips_camera_ready.towards_best_corpora.wo_trnsl-v2': '20231018.thing_person_config_translation',
    '2024-08-12.neurips_camera_ready.towards_best_corpora.wo_theorems': '20231018.thing_person_config_translation',
    '2024-08-12.neurips_camera_ready.towards_best_corpora.suppress_dilemma': '20231018.thing_person_config_translation',
    '2024-08-12.neurips_camera_ready.towards_best_corpora.suppress_dilemma.theorems-0.003': '20231018.thing_person_config_translation',
    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorems-0.0001': '20231018.thing_person_config_translation',

    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem_tree_prob-0.1': '20231018.thing_person_config_translation',

    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--1.0--0.1': '20231018.thing_person_config_translation',
    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--0.5--0.1': '20231018.thing_person_config_translation',
    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--0.25--0.1': '20231018.thing_person_config_translation',
    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--0.25--0.1.G_MP-3': '20231018.thing_person_config_translation',
    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--0.25--0.1.G_MP-10': '20231018.thing_person_config_translation',
    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--0.10--0.1': '20231018.thing_person_config_translation',

    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--1.0--0.01': '20231018.thing_person_config_translation',
    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--0.5--0.01': '20231018.thing_person_config_translation',
    '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--0.25--0.01': '20231018.thing_person_config_translation',

    # =================================== ./outputs/01.train.py/2024-08-16.neurips_camera_ready ========================================
    '2024-08-09.depth_fix.2024-03-29.FLD_v2': '20230626.many_bugs_fixed',
    '2024-08-16.neurips_camera_ready.FLD.small_vocab': '20230626.many_bugs_fixed',

    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0': '20231018.thing_person_config_translation',

    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.ref_prob-0.05': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.ref_prob-0.20': '20231018.thing_person_config_translation',

    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.15': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.05': '20231018.thing_person_config_translation',

    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.15.w_flag': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.15.w_flag.super_theorems': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.15.w_flag.super_theorems.ref_prob=0.20': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.15.w_flag.super_theorems.syllogism': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.15.w_flag.super_theorems.syllogism.contraposition': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.15.w_flag.super_theorems.syllogism.contraposition.and_interchangeability': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.05.w_flag': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.25.w_flag': '20231018.thing_person_config_translation',


    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.wo_suppress_if': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.wo_phrase': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.wo_clause': '20231018.thing_person_config_translation',


    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v2': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v2.ref_prob-0.1': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v2.ref_prob-0.126': '20231018.thing_person_config_translation',
    '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v2.ref_prob-0.1.theorems-0.25': '20231018.thing_person_config_translation',



    # =================================== 2024-08-30.fix_ref_prob ========================================
    '2024-08-30.FLD.ref_prob-0.20': '20230626.many_bugs_fixed',
    '2024-08-30.trnsl-thing_person-v0.ref_prob-0.20': '20231018.thing_person_config_translation',
    '2024-08-30.trnsl-thing_person-v0.ref_prob-0.20.theorem-G_MP': '20231018.thing_person_config_translation',
    '2024-08-30.trnsl-thing_person-v0.ref_prob-0.20.theorem-G_MP.syllogism': '20231018.thing_person_config_translation',
    '2024-08-30.trnsl-thing_person-v0.ref_prob-0.20.theorem-G_MP.syllogism.contraposition': '20231018.thing_person_config_translation',
    '2024-08-30.trnsl-thing_person-v0.ref_prob-0.20.theorem-G_MP.syllogism.contraposition.interchangeability': '20231018.thing_person_config_translation',
    '2024-08-30.trnsl-thing_person-v0.ref_prob-0.13.theorem-G_MP.syllogism.contraposition.interchangeability': '20231018.thing_person_config_translation',
    '2024-08-30.trnsl-thing_person-v0.ref_prob-0.05.theorem-G_MP.syllogism.contraposition.interchangeability': '20231018.thing_person_config_translation',
    '2024-08-30.trnsl-thing_person-v0.ref_prob-0.20.theorem-all': '20231018.thing_person_config_translation',

    '2024-08-30.trnsl-thing_person-v0.ref_prob-0.066.theorem-G_MP': '20231018.thing_person_config_translation',


    # ================================== 2024-09-03.toward_camera_ready ========================================
    '2024-08-30.FLD.ref_prob-0.20': '20230626.many_bugs_fixed',

    '2024-09-03.trnsl-thing_person-v2': '20231018.thing_person_config_translation',
    '2024-09-03.trnsl-thing_person-v2.voc-100': '20231018.thing_person_config_translation',
    '2024-09-03.trnsl-thing_person-v2.dstrct-0': '20231018.thing_person_config_translation',
    '2024-09-03.trnsl-thing_person-v2.rule-G_MP': '20231018.thing_person_config_translation',
    '2024-09-03.trnsl-thing_person-v2.stps-3-0': '20231018.thing_person_config_translation',
    '2024-09-03.trnsl-thing_person-v2.trnsl-small': '20231018.thing_person_config_translation',

    '2024-09-03.trnsl-thing_person-v0': '20231018.thing_person_config_translation',
    '2024-09-03.trnsl-thing_person-v0.voc-100': '20231018.thing_person_config_translation',
    '2024-09-03.trnsl-thing_person-v0.dstrct-0': '20231018.thing_person_config_translation',
    '2024-09-03.trnsl-thing_person-v0.rule-G_MP': '20231018.thing_person_config_translation',
    '2024-09-03.trnsl-thing_person-v0.stps-3-0': '20231018.thing_person_config_translation',
    '2024-09-03.trnsl-thing_person-v0.trnsl-small': '20231018.thing_person_config_translation',


    # ================================== 2024-09-16.fix_negation ========================================
    '2024-09-16.FLD.fix_negation': '20230626.many_bugs_fixed',

}



def get_dataset_setting(name: str) -> Dict:
    setting = copy.deepcopy(_DEFAULT_DATASET_SETTINGS[_DATASET_NAME_TO_DEFAULT[name]])
    setting.update(copy.deepcopy(_DATASET_SETTINGS[name]))
    return setting


def maybe_option(option: str, value: Any) -> str:
    if value is None:
        return ''
    else:
        return f'{option} {value}'
