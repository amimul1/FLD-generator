
_DATASET_SETTINGS = {


    '20221203.first_exp__arg-RT__frml-smpl__dist-0__transl-nrrw__tree-3__dataset_size-30000': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            # './configs/arguments/propositional/axioms/and_or.json',
            # './configs/arguments/predicate/axioms/and_or.json',

            # './configs/arguments/propositional/axioms/implication_intro.json',
            # './configs/arguments/predicate/axioms/implication_intro.json',

            # './configs/arguments/propositional/axioms/negation.json',
            # './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        'complex_formula_arguments_weight': 0.0,


        'distractors_range': (0, 0),
        'reused_object_nouns_max_factor': 0.0,
        'disallow_subj_obj_swapped_distractor': True,

        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': True,
        'limit_vocab_size_per_type': 100,


        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            'test': 1000,
            'train': 30000,
        }
    },



    '20221203.first_exp__arg-RT__frml-cmpl__dist-0__transl-nrrw__tree-3__dataset_size-30000': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            # './configs/arguments/propositional/axioms/and_or.json',
            # './configs/arguments/predicate/axioms/and_or.json',

            # './configs/arguments/propositional/axioms/implication_intro.json',
            # './configs/arguments/predicate/axioms/implication_intro.json',

            # './configs/arguments/propositional/axioms/negation.json',
            # './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 0),
        'reused_object_nouns_max_factor': 0.0,
        'disallow_subj_obj_swapped_distractor': True,

        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': True,
        'limit_vocab_size_per_type': 100,


        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            'test': 1000,
            'train': 30000,
        }
    },



    '20221203.first_exp__arg-RT__frml-cmpl__dist-20__transl-nrrw__tree-3__dataset_size-30000': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            # './configs/arguments/propositional/axioms/and_or.json',
            # './configs/arguments/predicate/axioms/and_or.json',

            # './configs/arguments/propositional/axioms/implication_intro.json',
            # './configs/arguments/predicate/axioms/implication_intro.json',

            # './configs/arguments/propositional/axioms/negation.json',
            # './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': True,
        'limit_vocab_size_per_type': 100,


        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            'test': 1000,
            'train': 30000,
        }
    },



    '20221203.first_exp__arg-AA__frml-cmpl__dist-20__transl-nrrw__tree-1__dataset_size-30000': {

        'argument_configs': [
            './configs/arguments/predicate/others/AACorpus.json',

            # './configs/arguments/propositional/axioms/implication_elim.json',
            # './configs/arguments/predicate/axioms/implication_elim.json',

            # './configs/arguments/propositional/axioms/and_or.json',
            # './configs/arguments/predicate/axioms/and_or.json',

            # './configs/arguments/propositional/axioms/implication_intro.json',
            # './configs/arguments/predicate/axioms/implication_intro.json',

            # './configs/arguments/propositional/axioms/negation.json',
            # './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',
        ],
        'quantifier_axiom_arguments_weight': 0.0,  # can not be used with AACorpus


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': True,
        'limit_vocab_size_per_type': 100,


        'depth_range': (1, 1),
        'branch_extensions_range': (0, 0),


        'split_sizes': {
            'test': 1000,
            'train': 30000,
        }
    },







    '20221203.first_exp__arg-FLNL__frml-cmpl__dist-20__transl-nrrw__tree-3__dataset_size-30000': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            './configs/arguments/propositional/theorems/implication_elim.json',
            './configs/arguments/predicate/theorems/implication_elim.json',

            './configs/arguments/propositional/theorems/and_or.json',
            './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': True,
        'limit_vocab_size_per_type': 100,


        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            'test': 1000,
            'train': 30000,
        }
    },




    '20221203.first_exp__arg-FLNL__frml-cmpl__dist-20__transl-wide__tree-3__dataset_size-30000': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            './configs/arguments/propositional/theorems/implication_elim.json',
            './configs/arguments/predicate/theorems/implication_elim.json',

            './configs/arguments/propositional/theorems/and_or.json',
            './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),


        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            'test': 1000,
            'train': 30000,
        }
    },



    '20221203.first_exp__arg-FLNL__frml-cmpl__dist-20__transl-wide__tree-8__dataset_size-30000': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            './configs/arguments/propositional/theorems/implication_elim.json',
            './configs/arguments/predicate/theorems/implication_elim.json',

            './configs/arguments/propositional/theorems/and_or.json',
            './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_range': (1, 8),
        'branch_extensions_range': (0, 5),


        'split_sizes': {
            'test': 1000,
            'train': 30000,
        }
    },



    '20221203.first_exp__arg-FLNL__frml-cmpl__dist-20__transl-wide__tree-8__dataset_size-100000': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            './configs/arguments/propositional/theorems/implication_elim.json',
            './configs/arguments/predicate/theorems/implication_elim.json',

            './configs/arguments/propositional/theorems/and_or.json',
            './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_range': (1, 8),
        'branch_extensions_range': (0, 5),


        'split_sizes': {
            'test': 1000,
            'train': 100000,
        }
    },












    # ---------------------------------- 20221215 additional experiments ------------------------------------


    '20221203.first_exp__arg-RT__frml-smpl__dist-20__transl-nrrw__tree-3__dataset_size-30000': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            # './configs/arguments/propositional/axioms/and_or.json',
            # './configs/arguments/predicate/axioms/and_or.json',

            # './configs/arguments/propositional/axioms/implication_intro.json',
            # './configs/arguments/predicate/axioms/implication_intro.json',

            # './configs/arguments/propositional/axioms/negation.json',
            # './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        'complex_formula_arguments_weight': 0.0,

        # ---- since complex_formula_arguments_weight = 0.0
        'distractor': 'various_form',
        'disallow_simplified_tree_formulas_as_distractor_prototype': True,
        'sample_distractor_prototype_formulas_from_all_possible_formulas': True,
        'disallow_hard_negative_distractors': True,
        'fallback_from_formula_to_translation_distractor': True,

        'distractors_range': (0, 15),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': True,
        'limit_vocab_size_per_type': 100,


        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            # 'test': 1000,
            'train': 30000,
        }
    },



    # ---------------------------------- 20221216 additional experiments ------------------------------------


    '20221203.first_exp__arg-FLNL__frml-cmpl__dist-0__transl-nrrw__tree-3__dataset_size-30000': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            './configs/arguments/propositional/theorems/implication_elim.json',
            './configs/arguments/predicate/theorems/implication_elim.json',

            './configs/arguments/propositional/theorems/and_or.json',
            './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 0),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': True,
        'limit_vocab_size_per_type': 100,


        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            # 'test': 1000,
            'train': 30000,
        }
    },


    '20221203.first_exp__arg-FLNL__frml-smpl__dist-20__transl-nrrw__tree-3__dataset_size-30000': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            # './configs/arguments/propositional/axioms/and_or.json',
            # './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            # './configs/arguments/propositional/axioms/negation.json',
            # './configs/arguments/predicate/axioms/negation.json',

            './configs/arguments/propositional/theorems/implication_elim.json',
            './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        'complex_formula_arguments_weight': 0.0,

        # ---- since complex_formula_arguments_weight = 0.0
        'distractor': 'various_form',
        'disallow_simplified_tree_formulas_as_distractor_prototype': True,
        'sample_distractor_prototype_formulas_from_all_possible_formulas': True,
        'disallow_hard_negative_distractors': True,
        'fallback_from_formula_to_translation_distractor': True,

        'distractors_range': (0, 20),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': True,
        'limit_vocab_size_per_type': 100,


        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            # 'test': 1000,
            'train': 30000,
        }
    },


    '20221203.first_exp__arg-FLNL__frml-cmpl__dist-20__transl-wide__tree-5__dataset_size-30000': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            './configs/arguments/propositional/theorems/implication_elim.json',
            './configs/arguments/predicate/theorems/implication_elim.json',

            './configs/arguments/propositional/theorems/and_or.json',
            './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_range': (1, 5),
        'branch_extensions_range': (0, 4),


        'split_sizes': {
            # 'test': 1000,
            'train': 30000,
        }
    },


    '20221203.first_exp__arg-RT__frml-cmpl__dist-20__transl-nrrw__tree-3__dataset_size-30000.G_MP': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            # './configs/arguments/propositional/axioms/and_or.json',
            # './configs/arguments/predicate/axioms/and_or.json',

            # './configs/arguments/propositional/axioms/implication_intro.json',
            # './configs/arguments/predicate/axioms/implication_intro.json',

            # './configs/arguments/propositional/axioms/negation.json',
            # './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',

            './configs/arguments/predicate/theorems/G_MP.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': True,
        'limit_vocab_size_per_type': 100,


        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            # 'test': 1000,
            'train': 30000,
        }
    },


    '20221203.first_exp__arg-RT__frml-cmpl__dist-20__transl-nrrw__tree-8__dataset_size-30000.G_MP': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            # './configs/arguments/propositional/axioms/and_or.json',
            # './configs/arguments/predicate/axioms/and_or.json',

            # './configs/arguments/propositional/axioms/implication_intro.json',
            # './configs/arguments/predicate/axioms/implication_intro.json',

            # './configs/arguments/propositional/axioms/negation.json',
            # './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',

            './configs/arguments/predicate/theorems/G_MP.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': True,
        'limit_vocab_size_per_type': 100,


        'depth_range': (1, 8),
        'branch_extensions_range': (0, 5),


        'split_sizes': {
            'test': 1000,
            'train': 30000,
        }
    },


    '20221203.first_exp__arg-RT__frml-cmpl__dist-20__transl-nrrw__tree-3__dataset_size-30000__dpth-RT.G_MP': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            # './configs/arguments/propositional/axioms/and_or.json',
            # './configs/arguments/predicate/axioms/and_or.json',

            # './configs/arguments/propositional/axioms/implication_intro.json',
            # './configs/arguments/predicate/axioms/implication_intro.json',

            # './configs/arguments/propositional/axioms/negation.json',
            # './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',

            './configs/arguments/predicate/theorems/G_MP.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': True,
        'limit_vocab_size_per_type': 100,


        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),
        'depth_distrib': 'ruletaker.ours.20221202',


        'split_sizes': {
            'test': 1000,
            # 'train': 30000,
        }
    },


    '20221203.first_exp__arg-FLNL__frml-cmpl__dist-20__transl-nrrw__tree-3__dataset_size-30000__dpth-RT': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            './configs/arguments/propositional/theorems/implication_elim.json',
            './configs/arguments/predicate/theorems/implication_elim.json',

            './configs/arguments/propositional/theorems/and_or.json',
            './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': True,
        'limit_vocab_size_per_type': 100,


        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),
        'depth_distrib': 'ruletaker.ours.20221202',


        'split_sizes': {
            # 'test': 1000,
            'train': 30000,
        }
    },



    '20221203.first_exp__arg-RT__frml-cmpl__dist-20__transl-wide__tree-3__dataset_size-30000.G_MP': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            # './configs/arguments/propositional/axioms/and_or.json',
            # './configs/arguments/predicate/axioms/and_or.json',

            # './configs/arguments/propositional/axioms/implication_intro.json',
            # './configs/arguments/predicate/axioms/implication_intro.json',

            # './configs/arguments/propositional/axioms/negation.json',
            # './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',

            './configs/arguments/predicate/theorems/G_MP.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),


        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            'test': 1000,
            'train': 30000,
        }
    },


    '20221203.first_exp__arg-RT__frml-cmpl__dist-20__transl-wide__tree-5__dataset_size-30000.G_MP': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            # './configs/arguments/propositional/axioms/and_or.json',
            # './configs/arguments/predicate/axioms/and_or.json',

            # './configs/arguments/propositional/axioms/implication_intro.json',
            # './configs/arguments/predicate/axioms/implication_intro.json',

            # './configs/arguments/propositional/axioms/negation.json',
            # './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',

            './configs/arguments/predicate/theorems/G_MP.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_range': (1, 5),
        'branch_extensions_range': (0, 4),


        'split_sizes': {
            'test': 1000,
            'train': 30000,
        }
    },





    '20221203.first_exp__arg-RT__frml-cmpl__dist-20__transl-wide__tree-8__dataset_size-100000.G_MP': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            # './configs/arguments/propositional/axioms/and_or.json',
            # './configs/arguments/predicate/axioms/and_or.json',

            # './configs/arguments/propositional/axioms/implication_intro.json',
            # './configs/arguments/predicate/axioms/implication_intro.json',

            # './configs/arguments/propositional/axioms/negation.json',
            # './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',

            './configs/arguments/predicate/theorems/G_MP.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_range': (1, 8),
        'branch_extensions_range': (0, 5),


        'split_sizes': {
            'test': 1000,
            'train': 100000,
        }
    },





    # ---------------------------------- 20221217.back_to_the_past ------------------------------------

    '20221217.back_to_the_past__arg-FLNL__frml-cmpl__dist-10__transl-wide__tree-10__dataset_size-100000': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            './configs/arguments/propositional/theorems/implication_elim.json',
            './configs/arguments/predicate/theorems/implication_elim.json',

            './configs/arguments/propositional/theorems/and_or.json',
            './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        'complex_formula_arguments_weight': 0.3,


        'distractor': 'fallback(various_form.negative_tree)',
        'disallow_simplified_tree_formulas_as_distractor_prototype': True,
        'sample_distractor_prototype_formulas_from_all_possible_formulas': True,
        'disallow_hard_negative_distractors': True,
        'fallback_from_formula_to_translation_distractor': False,


        'distractors_range': (0, 10),
        'disallow_subj_obj_swapped_distractor': True,


        # 'translation_distractors_range': (0, 0),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_range': (1, 10),
        'branch_extensions_range': (1, 5),


        'split_sizes': {
            # 'test': 1000,
            'train': 100000,
        }
    },


    '20230529.use_fixed_translation_for_LLM.20221203.first_exp__arg-FLNL__frml-cmpl__dist-20__transl-wide__tree-3__dataset_size-30000': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            './configs/arguments/propositional/theorems/implication_elim.json',
            './configs/arguments/predicate/theorems/implication_elim.json',

            './configs/arguments/propositional/theorems/and_or.json',
            './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),


        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': True,
        'limit_vocab_size_per_type': None,


        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            'test': 1000,
            # 'train': 30000,
        }
    },


    '20230529.use_fixed_translation_for_LLM.20221203.first_exp__arg-FLNL__frml-cmpl__dist-20__transl-wide__tree-8__dataset_size-30000': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            './configs/arguments/propositional/theorems/implication_elim.json',
            './configs/arguments/predicate/theorems/implication_elim.json',

            './configs/arguments/propositional/theorems/and_or.json',
            './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': True,
        'limit_vocab_size_per_type': None,


        'depth_range': (1, 8),
        'branch_extensions_range': (0, 5),


        'split_sizes': {
            'test': 1000,
            # 'train': 30000,
        }
    },


    '20230615.formula_checkers.20221203.first_exp__arg-FLNL__frml-cmpl__dist-20__transl-wide__tree-3__dataset_size-30000': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            './configs/arguments/propositional/theorems/implication_elim.json',
            './configs/arguments/predicate/theorems/implication_elim.json',

            './configs/arguments/propositional/theorems/and_or.json',
            './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),


        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': True,
        'limit_vocab_size_per_type': None,


        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            'test': 100,
            # 'train': 30000,
        }
    },


    '20230615.formula_checkers.20221203.first_exp__arg-FLNL__frml-cmpl__dist-20__transl-wide__tree-3__dataset_size-30000.wo_theorems': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),


        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': True,
        'limit_vocab_size_per_type': None,


        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            'test': 100,
            # 'train': 30000,
        }
    },



    '20230616.formula_checkers.20221203.first_exp__arg-FLNL__frml-cmpl__dist-20__transl-wide__tree-3__dataset_size-30000.wo_theorems': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': True,
        'limit_vocab_size_per_type': None,


        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            'test': 100,
            # 'train': 30000,
        }
    },


    '20230621.formula_checkers.20221203.first_exp__arg-FLNL__frml-cmpl__dist-20__transl-wide__tree-3__dataset_size-30000.wo_theorems': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': True,
        'limit_vocab_size_per_type': None,


        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            'test': 1000,
            # 'train': 30000,
        }
    },


    '20230621.formula_checkers.20221203.first_exp__arg-FLNL__frml-cmpl__dist-20__transl-wide__tree-3__dataset_size-30000.wo_theorems.wo_translation_dist': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),
        'fallback_from_formula_to_translation_distractor': False,

        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': True,
        'limit_vocab_size_per_type': None,


        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            'test': 100,
            # 'train': 30000,
        }
    },



    '20230626.many_bugs_fixed.20221203.first_exp__arg-RT__frml-cmpl__dist-20__transl-nrrw__tree-3__dataset_size-30000.G_MP': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            # './configs/arguments/propositional/axioms/and_or.json',
            # './configs/arguments/predicate/axioms/and_or.json',

            # './configs/arguments/propositional/axioms/implication_intro.json',
            # './configs/arguments/predicate/axioms/implication_intro.json',

            # './configs/arguments/propositional/axioms/negation.json',
            # './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',

            './configs/arguments/predicate/theorems/G_MP.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,

        # 'quantifier_axioms': [
        #     'universal_quantifier_elim',
        #     # 'universal_quantifier_intro',

        #     # we do not use existential_quantifier_intro since it has no linkable_args without existential_quantifier_elim, which is not implemented yet.
        #     # 'existential_quantifier_intro',
        # ],
        'quantifier_axioms': 'universal_quantifier_elim',

        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 15),


        'use_fixed_translation': True,
        'limit_vocab_size_per_type': 100,


        'depth_distrib': 'flat',
        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            # 'test': 1000,
            'train': 30000,
        }
    },



    '20230626.many_bugs_fixed.20221203.first_exp__arg-FLNL__frml-cmpl__dist-20__transl-wide__tree-3__dataset_size-30000.plus_quantifiers': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'quantifier_axioms': 'all',,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (0, 20),


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_distrib': 'flat',
        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            # 'test': 1000,
            'train': 30000,
        }
    },




    '20230626.many_bugs_fixed.D3.hard': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'quantifier_axioms': 'all',,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (15, 20),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_distrib': 'flat.no_reference',
        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            'test': 500,
            'train': 15000,
        }
    },




    '20230626.many_bugs_fixed.D3.hard.dist-trees': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'quantifier_axioms': 'all',,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (15, 20),
        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_distrib': 'flat.no_reference',
        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            'test': 500,
            'train': 15000,
        }
    },
    



    '20230626.many_bugs_fixed.D3.hard.unk-0.1': {
        'unknown_ratio': 0.1,

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'quantifier_axioms': 'all',,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (15, 20),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_distrib': 'flat.no_reference',
        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            'test': 500,
            'train': 15000,
        }
    },




    '20230626.many_bugs_fixed.D3.hard.brnch-high': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'quantifier_axioms': 'all',,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (15, 20),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_distrib': 'flat.no_reference',
        'depth_range': (1, 3),
        'branch_extensions_range': (2, 5),


        'split_sizes': {
            'test': 500,
            'train': 15000,
        }
    },



    '20230626.many_bugs_fixed.D3.hard.dist-neg-1.0': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'quantifier_axioms': 'all',,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (15, 20),
        'distractor': 'negative_tree-1.0',

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_distrib': 'flat.no_reference',
        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            'test': 500,
            'train': 15000,
        }
    },



    '20230626.many_bugs_fixed.D3.hard.dist-neg-0.5': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'quantifier_axioms': 'all',,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (15, 20),
        # 'negative_tree_negated_hypothesis_ratio': 0.5,
        'distractor': 'negative_tree-0.5',

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_distrib': 'flat.no_reference',
        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            'test': 500,
            'train': 15000,
        }
    },


    '20230626.many_bugs_fixed.D3.hard.dist-neg-0.0': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'quantifier_axioms': 'all',,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (15, 20),
        # 'negative_tree_negated_hypothesis_ratio': 0.0,
        'distractor': 'negative_tree-0.0',

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_distrib': 'flat.no_reference',
        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            'test': 500,
            'train': 15000,
        }
    },




    '20230626.many_bugs_fixed.D3.hard.dist-trees-only': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'quantifier_axioms': 'all',,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (15, 20),
        'distractor': 'mixture(negative_tree_double)',

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_distrib': 'flat.no_reference',
        'depth_range': (1, 3),
        'branch_extensions_range': (0, 3),


        'split_sizes': {
            # 'test': 500,
            'train': 15000,
        }
    },





    '20230626.many_bugs_fixed.D8.hard': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'quantifier_axioms': 'all',,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (15, 20),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_distrib': 'flat.no_reference',
        'depth_range': (1, 8),
        'branch_extensions_range': (0, 5),


        'split_sizes': {
            'test': 500,
            'train': 15000,
        }
    },







    '20230626.many_bugs_fixed.D8.hard.dist-trees': {

        'argument_configs': [
            # './configs/arguments/predicate/others/AACorpus.json',

            './configs/arguments/propositional/axioms/implication_elim.json',
            './configs/arguments/predicate/axioms/implication_elim.json',

            './configs/arguments/propositional/axioms/and_or.json',
            './configs/arguments/predicate/axioms/and_or.json',

            './configs/arguments/propositional/axioms/implication_intro.json',
            './configs/arguments/predicate/axioms/implication_intro.json',

            './configs/arguments/propositional/axioms/negation.json',
            './configs/arguments/predicate/axioms/negation.json',

            # './configs/arguments/propositional/theorems/implication_elim.json',
            # './configs/arguments/predicate/theorems/implication_elim.json',

            # './configs/arguments/propositional/theorems/and_or.json',
            # './configs/arguments/predicate/theorems/and_or.json',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'quantifier_axioms': 'all',,


        # 'complex_formula_arguments_weight': 0.5,


        'distractors_range': (15, 20),
        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,
        'translation_vocab': None,


        'depth_distrib': 'flat.no_reference',
        'depth_range': (1, 8),
        'branch_extensions_range': (0, 5),


        'split_sizes': {
            'test': 500,
            'train': 15000,
        }
    },




    '20230701.D3.default': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'quantifier_axioms': 'all',,


        # 'complex_formula_arguments_weight': 0.5,


        'distractor': 'mixture(negative_tree_double)',
        'distractors_range': (15, 20),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,
        'translation_vocab': None,


        'depth_distrib': 'flat.no_reference',
        'depth_range': (1, 3),
        'branch_extensions_range': (2, 5),

        'split_sizes': {
            'test': 500,
            'train': 15000,
        }
    },





    '20230701.D3.wo_transl_dist': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'quantifier_axioms': 'all',,


        # 'complex_formula_arguments_weight': 0.5,


        'distractor': 'mixture(negative_tree_double)',
        'distractors_range': (15, 20),

        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,
        'translation_vocab': None,


        'depth_distrib': 'flat.no_reference',
        'depth_range': (1, 3),
        'branch_extensions_range': (2, 5),


        'split_sizes': {
            'test': 500,
            'train': 15000,
        }
    },



    '20230701.D3.brnch-small': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'quantifier_axioms': 'all',,


        # 'complex_formula_arguments_weight': 0.5,


        'distractor': 'mixture(negative_tree_double)',
        'distractors_range': (15, 20),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_distrib': 'flat.no_reference',
        'depth_range': (1, 3),
        'branch_extensions_range': (0, 5),


        'split_sizes': {
            'test': 500,
            'train': 15000,
        }
    },




    '20230701.D3.dist-small': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'quantifier_axioms': 'all',,


        # 'complex_formula_arguments_weight': 0.5,


        'distractor': 'mixture(negative_tree_double)',
        'distractors_range': (0, 20),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_distrib': 'flat.no_reference',
        'depth_range': (1, 3),
        'branch_extensions_range': (2, 5),


        'split_sizes': {
            'test': 500,
            'train': 15000,
        }
    },



    '20230701.D3.default.refactor_test': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'quantifier_axioms': 'all',,


        # 'complex_formula_arguments_weight': 0.5,


        'distractor': 'mixture(negative_tree_double)',
        'distractors_range': (15, 20),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_distrib': 'flat.no_reference',
        'depth_range': (1, 3),
        'branch_extensions_range': (2, 5),


        'split_sizes': {
            # 'test': 50,
            'test': 300,
            # 'test': 1000,
        }
    },



    '20230701.D3.default.dist-tree-triple': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'quantifier_axioms': 'all',,


        # 'complex_formula_arguments_weight': 0.5,


        'distractor': 'mixture(negative_tree_triple)',
        'distractors_range': (15, 20),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_distrib': 'flat.no_reference',
        'depth_range': (1, 3),
        'branch_extensions_range': (2, 5),


        'split_sizes': {
            # 'test': 50,
            'test': 300,
            # 'test': 1000,
        }
    },



    '20230701.D3.default.dist-tree-quadruple': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'quantifier_axioms': 'all',,


        # 'complex_formula_arguments_weight': 0.5,


        'distractor': 'mixture(negative_tree_quadruple)',
        'distractors_range': (15, 20),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_distrib': 'flat.no_reference',
        'depth_range': (1, 3),
        'branch_extensions_range': (2, 5),


        'split_sizes': {
            # 'test': 50,
            'test': 300,
            # 'test': 1000,
        }
    },




    '20230701.D8.default': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'quantifier_axioms': 'all',,


        # 'complex_formula_arguments_weight': 0.5,


        'distractor': 'mixture(negative_tree_double)',
        'distractors_range': (15, 20),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_distrib': 'flat.no_reference',
        'depth_range': (1, 8),
        'branch_extensions_range': (2, 5),


        'split_sizes': {
            'test': 500,
            'train': 15000,
        }
    },





    '20230701.D3.debug': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axiom_arguments_weight': 0.2,


        # 'quantifier_axioms': 'all',,


        # 'complex_formula_arguments_weight': 0.5,


        'distractor': 'mixture(negative_tree_double)',
        'distractors_range': (15, 20),

        'translation_distractors_range': (0, 5),
        'use_collapsed_translation_nodes_for_unknown_tree': True,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'depth_distrib': 'flat.no_reference',
        'depth_range': (1, 3),
        'branch_extensions_range': (2, 5),


        'split_sizes': {
            'test': 100,
            # 'train': 15000,
        }
    },












    '20230706.finalize.D3.dist-double': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat.no_reference',
        'branch_extensions_range': (0, 5),


        'distractor': 'mixture(negative_tree_double)',
        'distractors_range': (15, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'split_sizes': {
            'test': 500,
            # 'train': 15000,
        }

    },



    '20230706.finalize.D3.dist-quadruple': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat.no_reference',
        'branch_extensions_range': (0, 5),


        'distractor': 'mixture(negative_tree_quadruple)',
        'distractors_range': (15, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'split_sizes': {
            'test': 500,
            # 'train': 15000,
        }

    },



    '20230706.finalize.D8.dist-double': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 8),
        'depth_distrib': 'flat.no_reference',
        'branch_extensions_range': (0, 5),


        'distractor': 'mixture(negative_tree_double)',
        'distractors_range': (15, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'split_sizes': {
            'test': 500,
            # 'train': 15000,
        }

    },




    '20230706.finalize.D8.dist-quadruple': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 8),
        'depth_distrib': 'flat.no_reference',
        'branch_extensions_range': (0, 5),


        'distractor': 'mixture(negative_tree_quadruple)',
        'distractors_range': (15, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'split_sizes': {
            'test': 500,
            # 'train': 15000,
        }

    },











    '20230707.finalize.D3.dist-double': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat.no_reference',
        'branch_extensions_range': (0, 5),


        'distractor': 'mixture(negative_tree_double)',
        'distractors_range': (15, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'split_sizes': {
            'test': 100,
            # 'train': 30000,
        }

    },



    '20230707.finalize.D3.dist-triple': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat.no_reference',
        'branch_extensions_range': (0, 5),


        'distractor': 'mixture(negative_tree_triple)',
        'distractors_range': (15, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'split_sizes': {
            # 'test': 500,
            'train': 30000,
        }

    },



    '20230707.finalize.D3.dist-quadruple': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat.no_reference',
        'branch_extensions_range': (0, 5),


        'distractor': 'mixture(negative_tree_quadruple)',
        'distractors_range': (15, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'split_sizes': {
            # 'test': 500,
            'train': 30000,
        }

    },



    '20230711.dist-fallback': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat.no_reference',
        'branch_extensions_range': (0, 5),


        'distractor': 'fallback(mixture(negative_tree_double).simplified_formula.various_form)',
        'distractors_range': (15, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'split_sizes': {
            'test': 100,
            # 'train': 30000,
        }

    },





    '20230707.finalize.D8.dist-double': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 8),
        'depth_distrib': 'flat.no_reference',
        'branch_extensions_range': (0, 5),


        'distractor': 'mixture(negative_tree_double)',
        'distractors_range': (15, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'split_sizes': {
            'test': 500,
            'train': 30000,
        }

    },




    '20230707.finalize.D8.dist-triple': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 8),
        'depth_distrib': 'flat.no_reference',
        'branch_extensions_range': (0, 5),


        'distractor': 'mixture(negative_tree_triple)',
        'distractors_range': (15, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'split_sizes': {
            'test': 500,
            'train': 30000,
        }

    },




    '20230707.finalize.D8.dist-quadruple': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 8),
        'depth_distrib': 'flat.no_reference',
        'branch_extensions_range': (0, 5),


        'distractor': 'mixture(negative_tree_quadruple)',
        'distractors_range': (15, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'split_sizes': {
            'test': 500,
            'train': 30000,
        }

    },





    '20230711.finalize.D3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat.no_reference',
        'branch_extensions_range': (0, 5),


        'distractor': 'fallback(mixture(negative_tree_double).simplified_formula.various_form)',
        'distractors_range': (15, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'split_sizes': {
            'test': 5000,
            'valid': 5000,
            # 'train': 30000,
        }

    },



    '20230711.finalize.D8': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 8),
        'depth_distrib': 'flat.no_reference',
        'branch_extensions_range': (0, 5),


        'distractor': 'fallback(mixture(negative_tree_double).simplified_formula.various_form)',
        'distractors_range': (15, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'split_sizes': {
            'test': 5000,
            'valid': 5000,
            # 'train': 30000,
        }

    },








    '20230718.case_study.D3.dist-mixture': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat.no_reference',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (15, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            'train': 15000,
        }

    },


    '20230718.case_study.D3.num_dist-wide': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat.no_reference',
        'branch_extensions_range': (0, 5),


        'distractor': 'fallback(mixture(negative_tree_double).simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            'train': 15000,
        }

    },


    '20230718.case_study.D3.dist-mixture.num_dist-wide': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat.no_reference',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            'train': 15000,
        }

    },



    '20230718.case_study.D3.dist-mixture.num_dist-wide.transl_vol_logE': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat.no_reference',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,
        'translation_volume_to_weight': 'logE',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            'train': 15000,
        }

    },



    '20230718.case_study.D3.dist-mixture.num_dist-wide.transl_vol_log10': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat.no_reference',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,
        # 'translation_volume_to_weight': 'log10',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            'train': 15000,
        }

    },




    '20230718.case_study.D3.dist-mixture.num_dist-wide.transl_vol_log10.adj_verb_noun_equal': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat.no_reference',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,
        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            'train': 15000,
        }

    },



    '20230718.case_study.D8.dist-mixture.num_dist-wide': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 8),
        'depth_distrib': 'flat.no_reference',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'use_fixed_translation': False,
        'limit_vocab_size_per_type': None,


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            'train': 15000,
        }

    },







    '20230729.case_study_finalize.D3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 5000,
            'valid': 5000,
            # 'train': 30000,
        }

    },



    '20230729.case_study_finalize.D8': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 8),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 5000,
            'valid': 5000,
            # 'train': 30000,
        }

    },




    '20230826.jpn.D3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': _TRANSLATION_THING_CONFIGS_JPN_V1,
        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            # 'test': 500,
            # 'valid': 5000,
            'train': 15000,
        }

    },

    '20230826.jpn.D8': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 8),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': _TRANSLATION_THING_CONFIGS_JPN_V1,
        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            # 'test': 500,
            # 'valid': 5000,
            'train': 15000,
        }
    },



    '20230901.random_transitive_verbs.D3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            # 'test': 500,
            # 'valid': 500,
            'train': 15000,
        }

    },



    '20230901.random_transitive_verbs.D8': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 8),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 5000,
            'valid': 5000,
            # 'train': 30000,
        }

    },



    '20230904.jpn.D1.wo_brnch.wo_dstrct': {
        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 1),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 0),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 0),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': _TRANSLATION_THING_CONFIGS_JPN_V1,
        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 100,
            # 'valid': 5000,
            'train': 1000,
        }
    },


    '20230904.jpn.D1.wo_brnch': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 1),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 0),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': _TRANSLATION_THING_CONFIGS_JPN_V1,
        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 100,
            # 'valid': 5000,
            'train': 1000,
        }

    },



    '20230904.jpn.D1': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 1),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': _TRANSLATION_THING_CONFIGS_JPN_V1,
        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 100,
            # 'valid': 5000,
            'train': 1000,
        }

    },



    '20230904.jpn.D3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': _TRANSLATION_THING_CONFIGS_JPN_V1,
        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 100,
            # 'valid': 5000,
            'train': 10000,
        }

    },



    '20230912.jpn.D3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': _TRANSLATION_THING_CONFIGS_JPN_V1,
        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 500,
            # 'valid': 5000,
            'train': 20000,
        }

    },



    '20230914.jpn.D3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': _TRANSLATION_THING_CONFIGS_JPN_V1,
        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 500,
            # 'train': 20000,
            'train': 1000,
        }

    },



    '20230916.jpn.D1_wo_dist': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 1),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 0),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 0),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': _TRANSLATION_THING_CONFIGS_JPN_V1,
        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 500,
            'train': 30000,
        }

    },


    '20230916.jpn.D1': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 1),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 0),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': _TRANSLATION_THING_CONFIGS_JPN_V1,
        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 500,
            'train': 30000,
        }

    },


    '20230916.jpn.D3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': _TRANSLATION_THING_CONFIGS_JPN_V1,
        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 500,
            'train': 30000,
        }

    },



    '20230916.jpn.D5': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 5),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        'translation_lang': 'jpn',
        'translation_configs': _TRANSLATION_THING_CONFIGS_JPN_V1,
        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_sizes': {
            'test': 500,
            'train': 30000,
        }

    },




    '20231010.D3.large_vocab': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': False,
                # 'context_shuffles_per_instance': 1,
                # 'translation_variants_per_logic': 1,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 500,
            # 'valid': 500,
            'train': 30000,
        },

    },


    '20231012.D3.large_vocab': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': False,
                # 'context_shuffles_per_instance': 1,
                # 'translation_variants_per_logic': 1,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 500,
            # 'valid': 500,
            'train': 15000,
        },

    },


    '20231012.D3.large_vocab.smpl_stncs': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 1,
                # 'translation_variants_per_logic': 1,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 500,
            # 'valid': 500,
            'train': 45000,
        },

    },


    '20231012.D3.large_vocab.smpl_stncs.cntx_shffls-3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 1,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 500,
            # 'valid': 500,
            'train': 135000,
        },

    },


    '20231012.D3.large_vocab.smpl_stncs.cntx_shffls-3.trnsl_vrnts-3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


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
            'train': 405000,
        },

    },









    '20231018.knowledge.D3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': False,
                # 'context_shuffles_per_instance': 1,
                # 'translation_variants_per_logic': 1,
            },
            'valid': {
            },
            'test': {
            },
        },
        'split_sizes': {
            'test': 500,
            # 'valid': 500,
            'train': 15000,
        },

    },



    '20231018.knowledge.D3.w_knowledge': {

        'knowledge_range': [0.49, 0.5],
        'collapsed_knowledge_range': None,
        # 'knowledge_argument_factor': 1.0,

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,

        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': False,
                # 'context_shuffles_per_instance': 1,
                # 'translation_variants_per_logic': 1,
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/train.txt',
            },
            'valid': {
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/valid.txt',
            },
            'test': {
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/test.txt',
            },
        },
        'split_sizes': {
            # 'test': 500,
            # 'valid': 500,
            'train': 3000,
        },

    },



    '20231018.knowledge.D3.w_knowledge.complex-0.3': {

        'knowledge_range': [0.49, 0.5],
        'collapsed_knowledge_range': None,
        # 'knowledge_argument_factor': 1.0,

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.3,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,

        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': False,
                # 'context_shuffles_per_instance': 1,
                # 'translation_variants_per_logic': 1,
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/train.txt',
            },
            'valid': {
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/valid.txt',
            },
            'test': {
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/test.txt',
            },
        },
        'split_sizes': {
            'test': 500,
            # 'valid': 500,
            'train': 3000,
        },

    },




    '20231021.knowledge.D3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,


        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


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



    '20231021.knowledge.D3.complex-0.3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.3,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,

        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',


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



    '20231021.knowledge.D3.complex-0.3.w_knowledge': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.3,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,

        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',

        'knowledge_range': [0.49, 0.5],
        'collapsed_knowledge_range': None,
        # 'knowledge_argument_factor': 1.0,

        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/train.txt',
                'knowledge_no_shuffle': False,
            },
            'valid': {
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/valid.txt',
                'knowledge_no_shuffle': True,
            },
            'test': {
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/test.txt',
                'knowledge_no_shuffle': True,
            },
        },
        'split_sizes': {
            # 'test': 500,
            # 'valid': 500,
            'train': 300000,
        },

    },




    '20231028.knowledge.D3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.3,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,

        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',

        'knowledge_range': [0.0, 1.0],
        'collapsed_knowledge_range': None,
        # 'knowledge_argument_factor': 1.0,

        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/train.txt',
                'concept_net_100k_filepath': './res/knowledge_banks/commonsense-kg-completion/data/ConceptNet/train.txt',
            },
            'valid': {
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/valid.txt',
                'concept_net_100k_filepath': './res/knowledge_banks/commonsense-kg-completion/data/ConceptNet/valid.txt',
            },
            'test': {
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/test.txt',
                'concept_net_100k_filepath': './res/knowledge_banks/commonsense-kg-completion/data/ConceptNet/test.txt',
            },
        },
        'split_sizes': {
            # 'test': 500,
            # 'valid': 500,
            # 'train': 300000,
            'train': 3000,
        },

    },



    '20231029.knowledge.D3': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.3,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,

        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',

        'knowledge_range': [0.0, 1.0],
        'collapsed_knowledge_range': None,
        # 'knowledge_argument_factor': 1.0,

        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/train.txt',
                'concept_net_100k_filepath': './res/knowledge_banks/commonsense-kg-completion/data/ConceptNet/train.txt',
                'dbpedia_filepath': './res/knowledge_banks/DBpedia500/train1.txt',
            },
            'valid': {
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/valid.txt',
                'concept_net_100k_filepath': './res/knowledge_banks/commonsense-kg-completion/data/ConceptNet/valid.txt',
                'dbpedia_filepath': './res/knowledge_banks/DBpedia500/valid.txt',
            },
            'test': {
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/test.txt',
                'concept_net_100k_filepath': './res/knowledge_banks/commonsense-kg-completion/data/ConceptNet/test.txt',
                'dbpedia_filepath': './res/knowledge_banks/DBpedia500/test.txt',
            },
        },
        'split_sizes': {
            # 'test': 500,
            # 'valid': 500,
            # 'train': 300000,
            # 'train': 3000,
            'train': 500,
        },

    },


    '20231029.knowledge.D3.wo_knowledge': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.3,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,

        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',

        'knowledge_range': [0.0, 1.0],
        'collapsed_knowledge_range': None,
        # 'knowledge_argument_factor': 1.0,

        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
                # 'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/train.txt',
                # 'concept_net_100k_filepath': './res/knowledge_banks/commonsense-kg-completion/data/ConceptNet/train.txt',
                # 'dbpedia_filepath': './res/knowledge_banks/DBpedia500/train1.txt',
            },
            'valid': {
                # 'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/valid.txt',
                # 'concept_net_100k_filepath': './res/knowledge_banks/commonsense-kg-completion/data/ConceptNet/valid.txt',
                # 'dbpedia_filepath': './res/knowledge_banks/DBpedia500/valid.txt',
            },
            'test': {
                # 'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/test.txt',
                # 'concept_net_100k_filepath': './res/knowledge_banks/commonsense-kg-completion/data/ConceptNet/test.txt',
                # 'dbpedia_filepath': './res/knowledge_banks/DBpedia500/test.txt',
            },
        },
        'split_sizes': {
            # 'test': 500,
            # 'valid': 500,
            # 'train': 300000,
            # 'train': 3000,
            'train': 500,
        },

    },


    '20231029.knowledge.D3.wo_knowledge.cmplx-0.5': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        # 'complex_formula_arguments_weight': 0.5,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,

        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',

        'knowledge_range': [0.0, 1.0],
        'collapsed_knowledge_range': None,
        # 'knowledge_argument_factor': 1.0,

        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
                # 'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/train.txt',
                # 'concept_net_100k_filepath': './res/knowledge_banks/commonsense-kg-completion/data/ConceptNet/train.txt',
                # 'dbpedia_filepath': './res/knowledge_banks/DBpedia500/train1.txt',
            },
            'valid': {
                # 'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/valid.txt',
                # 'concept_net_100k_filepath': './res/knowledge_banks/commonsense-kg-completion/data/ConceptNet/valid.txt',
                # 'dbpedia_filepath': './res/knowledge_banks/DBpedia500/valid.txt',
            },
            'test': {
                # 'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/test.txt',
                # 'concept_net_100k_filepath': './res/knowledge_banks/commonsense-kg-completion/data/ConceptNet/test.txt',
                # 'dbpedia_filepath': './res/knowledge_banks/DBpedia500/test.txt',
            },
        },
        'split_sizes': {
            # 'test': 500,
            # 'valid': 500,
            # 'train': 300000,
            # 'train': 3000,
            'train': 500,
        },

    },






    '20231030.knowledge.D3.knowledge_factor-1.0': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.3,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,

        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',

        'knowledge_range': [0.0, 1.0],
        'collapsed_knowledge_range': [0.0, 1.0],
        # 'knowledge_argument_factor': 1.0,

        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/train.txt',
                'concept_net_100k_filepath': './res/knowledge_banks/commonsense-kg-completion/data/ConceptNet/train.txt',
                'dbpedia_filepath': './res/knowledge_banks/DBpedia500/train1.txt',
            },
            'valid': {
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/valid.txt',
                'concept_net_100k_filepath': './res/knowledge_banks/commonsense-kg-completion/data/ConceptNet/valid.txt',
                'dbpedia_filepath': './res/knowledge_banks/DBpedia500/valid.txt',
            },
            'test': {
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/test.txt',
                'concept_net_100k_filepath': './res/knowledge_banks/commonsense-kg-completion/data/ConceptNet/test.txt',
                'dbpedia_filepath': './res/knowledge_banks/DBpedia500/test.txt',
            },
        },
        'split_sizes': {
            # 'test': 500,
            # 'valid': 500,
            # 'train': 300000,
            'train': 3000,
            # 'train': 500,
        },

    },




    '20231030.knowledge.D3.knowledge_factor-5.0': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.3,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,

        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',

        'knowledge_range': [0.0, 1.0],
        'collapsed_knowledge_range': [0.0, 1.0],
        'knowledge_argument_factor': 5.0,

        'split_wise_settings': {
            'train': {
                # 'sample_all_stances_per_logic': True,
                # 'context_shuffles_per_instance': 3,
                # 'translation_variants_per_logic': 3,
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/train.txt',
                'concept_net_100k_filepath': './res/knowledge_banks/commonsense-kg-completion/data/ConceptNet/train.txt',
                'dbpedia_filepath': './res/knowledge_banks/DBpedia500/train1.txt',
            },
            'valid': {
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/valid.txt',
                'concept_net_100k_filepath': './res/knowledge_banks/commonsense-kg-completion/data/ConceptNet/valid.txt',
                'dbpedia_filepath': './res/knowledge_banks/DBpedia500/valid.txt',
            },
            'test': {
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/test.txt',
                'concept_net_100k_filepath': './res/knowledge_banks/commonsense-kg-completion/data/ConceptNet/test.txt',
                'dbpedia_filepath': './res/knowledge_banks/DBpedia500/test.txt',
            },
        },
        'split_sizes': {
            # 'test': 500,
            # 'valid': 500,
            # 'train': 300000,
            'train': 3000,
            # 'train': 500,
        },

    },





    '20231103.knowledge.D3.knowledge_factor-5.0': {

        'argument_configs': [
            './configs/arguments/axioms/',
            './configs/arguments/references/',
        ],
        # 'quantifier_axioms': 'all',,
        # 'quantifier_axiom_arguments_weight': 0.2,
        'complex_formula_arguments_weight': 0.3,


        'depth_range': (1, 3),
        'depth_distrib': 'flat',
        'branch_extensions_range': (0, 5),


        # 'distractor': 'mixture(negative_tree_double.simplified_formula.various_form)',
        'distractors_range': (0, 20),
        # 'translation_distractors_range': (0, 0),
        # 'use_collapsed_translation_nodes_for_unknown_tree': False,

        # 'translation_volume_to_weight': 'log10',
        # 'translation_adj_verb_noun_ratio': '1-1-1',

        'knowledge_range': [0.0, 1.0],
        'collapsed_knowledge_range': [0.0, 1.0],
        'knowledge_argument_factor': 5.0,

        'split_wise_settings': {
            'train': {
                'sample_all_stances_per_logic': True,
                'context_shuffles_per_instance': 3,
                'translation_variants_per_logic': 3,
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/train.txt',
                'concept_net_100k_filepath': './res/knowledge_banks/commonsense-kg-completion/data/ConceptNet/train.txt',
                'dbpedia_filepath': './res/knowledge_banks/DBpedia500/train1.txt',
            },
            'valid': {
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/valid.txt',
                'concept_net_100k_filepath': './res/knowledge_banks/commonsense-kg-completion/data/ConceptNet/valid.txt',
                'dbpedia_filepath': './res/knowledge_banks/DBpedia500/valid.txt',
            },
            'test': {
                'atomic_filepath': './res/knowledge_banks/commonsense-kg-completion/data/atomic/test.txt',
                'concept_net_100k_filepath': './res/knowledge_banks/commonsense-kg-completion/data/ConceptNet/test.txt',
                'dbpedia_filepath': './res/knowledge_banks/DBpedia500/test.txt',
            },
        },
        'split_sizes': {
            # 'test': 1000,
            # 'valid': 500,
            'train': 300000,
        },

    },






}





# output_top_dir = Path('./outputs/00.create_corpus/20230826.jpn')

# output_top_dir = Path('./outputs/00.create_corpus/20230901.random_transitive_verbs')

# output_top_dir = Path('./outputs/00.create_corpus/20230904.jpn')
# output_top_dir = Path('./outputs/00.create_corpus/20230912.jpn')
# output_top_dir = Path('./outputs/00.create_corpus/20230914.jpn')
# output_top_dir = Path('./outputs/00.create_corpus/20230916.jpn')




# ==================================================== transfer ====================================================
# '20240419.20230120.jpn.wordnet_repro_w_proposition.reimpl.D3',


# ============================================================================== 2024-07-02.debug_punipuni ==============================================================================
# '2024-07-02.debug_punipuni.0',
# '2024-07-02.debug_punipuni.1',
# '2024-07-02.debug_punipuni.2',
# '2024-07-02.debug_punipuni.3',
# '2024-07-02.debug_punipuni.4',







# =================================================================== ICML ===================================================================
# output_top_dir = Path('./outputs/00.create_corpus/20230729.case_study_finalize')
# output_top_dir = Path('./outputs/00.create_corpus/20230729.case_study_finalize.debug')
# output_top_dir = Path('./outputs/00.create_corpus/20230801.case_study_finalize.fix')

# =================================================================== JFLD ===================================================================

# output_top_dir = Path('./outputs/00.create_corpus/20231203.jpn')
# output_top_dir = Path('./outputs/00.create_corpus/20231205.postprocess_debug')
# output_top_dir = Path('./outputs/00.create_corpus/20231213.jpn')
# output_top_dir = Path('./outputs/00.create_corpus/20230115.jpn')
# output_top_dir = Path('./outputs/00.create_corpus/20230116.jpn.argument_pred_arg_only')
# output_top_dir = Path('./outputs/00.create_corpus/20230120.jpn/')
# output_top_dir = Path('./outputs/00.create_corpus/20230118.jpn.ICL')
# output_top_dir = Path('./outputs/00.create_corpus/20230120.jpn.punipuni')

# =================================================================== NeurIPS 2024 ===================================================================

# output_top_dir = Path('./outputs/00.create_corpus/2024-03-29')
# output_top_dir = Path('./outputs/00.create_corpus/2024-05-03.ablation')
# output_top_dir = Path('./outputs/00.create_corpus/2024-05-08.ref_prob')
# output_top_dir = Path('./outputs/00.create_corpus/2024-05-19.ablation_with_theorems')

# =================================================================== LPT ===================================================================
# output_top_dir = Path('./outputs/00.create_corpus/2024-06-08.LPT')

# =================================================================== transfer ===================================================================
# output_top_dir = Path('./outputs/00.create_corpus/2024-06-19.transfer')

# =================================================================== JFLD ===================================================================
# output_top_dir = Path('./outputs/00.create_corpus/2024-07-02.debug_punipuni')
# output_top_dir = Path('./outputs/00.create_corpus/2024-07-08.JFLD')

# =================================== 2024-07-21.neurips_additional ========================================
# output_top_dir = Path('./outputs/00.create_corpus/2024-07-21.neurips_additional')

# =================================== 2024-08-09.fix_depth_problem ========================================
# output_top_dir = Path('./outputs/00.create_corpus/2024-08-09.depth_fix')

# =================================== 2024-08-12.neurips_camera_ready.towards_best_corpora ========================================
# output_top_dir = Path('./outputs/00.create_corpus/2024-08-12.neurips_camera_ready.towards_best_corpora')

# =================================== 2024-08-30.fix_ref_prob ========================================
# output_top_dir = Path('./outputs/00.create_corpus/2024-08-30.fix_ref_prob')



dataset_names = [
    # ============================================- 20230729.case_study_finalize (ICML-official-release-v2) ================================================
    # '20230729.case_study_finalize.D3',
    # '20230729.case_study_finalize.D8',

    # ============================================- 20231213.jpn ================================================
    # '20231213.jpn.D1_wo_dist',
    # '20231213.jpn.D1',
    # '20231213.jpn.D3',
    # '20231213.jpn.D5',
    # '20231213.jpn.D8',

    # ============================================- 20230120.jpn.punipuni ================================================

    # '20230120.jpn.wordnet_repro_w_proposition.D1_wo_dist',
    # '20230120.jpn.wordnet_repro_w_proposition.D1',
    # '20230120.jpn.wordnet_repro_w_proposition.D3',
    # '20230120.jpn.wordnet_repro_w_proposition.D5',

    # '20230120.jpn.wordnet_repro_wo_proposition.D1_wo_dist',
    # '20230120.jpn.wordnet_repro_wo_proposition.D1',
    # '20230120.jpn.wordnet_repro_wo_proposition.D3',
    # '20230120.jpn.wordnet_repro_wo_proposition.D5',

    # '20230120.jpn.BCCWJ.D1_wo_dist',
    # '20230120.jpn.BCCWJ.D1',
    # '20230120.jpn.BCCWJ.D3',
    # '20230120.jpn.BCCWJ.D8',

    # '20230120.jpn.punipuni.D1_wo_dist',
    # '20230120.jpn.punipuni.D1',
    # '20230120.jpn.punipuni.D3',
    # '20230120.jpn.punipuni.D8',


    # ========================================- NeurIPS production ==========================================-

    # '2024-03-29.FLD_v2',
    # '2024-03-29.FLD_v2.theorems-0.3.fix',
    # '2024-03-29.FLD_v2.theorems-0.1.fix',
    # '2024-03-29.FLD_v2.theorems-0.03.fix',

    # '2024-03-29.JSAI_best.no_aug.trnsl-thing',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems-0.3',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems-0.1',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems-0.03',

    # '2024-03-29.JSAI_best.no_aug.trnsl-v2',
    # '2024-03-29.JSAI_best.no_aug.trnsl-v2.theorems-0.3',
    # '2024-03-29.JSAI_best.no_aug.trnsl-v2.theorems-0.1',
    # '2024-03-29.JSAI_best.no_aug.trnsl-v2.theorems-0.03',


    # '2024-03-29.JSAI_best.no_aug',
    # '2024-03-29.JSAI_best.no_aug.theorems-0.3',
    # '2024-03-29.JSAI_best.no_aug.theorems-0.1',
    # '2024-03-29.JSAI_best.no_aug.theorems-0.03',




    # ========================================- 2024-05-03.ablation ==========================================-

    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.voc-100',

    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.dstrct-0',

    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.stps-3',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.stps-5-3',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.stps-8-0',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.stps-1-2',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.stps-1-1',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.stps-1-0',


    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.rule-G_MP',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.rule-G_MP.stps-3',

    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.transl_sttng-0',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.transl_sttng-1',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.transl-small',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.transl-small.trnsl-old',


    # ==============================================- ./outputs/00.create_corpus/2024-05-08.ref_prob ==================================-
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10.stps-3-0',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10.stps-1-2',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10.stps-3-3',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10.stps-5-5',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10.theorems-0.1',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10.theorems-0.2',

    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.stps-3-0',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.stps-1-2',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.stps-3-3',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.stps-5-3',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.stps-5-5',

    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.05',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.1',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.2',

    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.30',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.40',


    # ==================================- ./outputs/00.create_corpus/2024-05-19.ablation_with_theorems =====================
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.1',

    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.1.voc-100',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.1.dstrct-0',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.1.rule-G_MP',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.1.stps-3-0',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.20.theorems-0.1.transl_sttng-1',


    # ==================================================== LPT ====================================================
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.large',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.steps',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.steps-5',


    # ================================================ 2024-07-08.JFLD ===========================================
    # '2024-07-08.JFLD.step-1',
    # '2024-07-08.JFLD.step-3',
    # '2024-07-08.JFLD.step-5',
    # '2024-07-08.JFLD.cmpl-0.2.step-1',
    # '2024-07-08.JFLD.cmpl-0.2.step-3',
    # '2024-07-08.JFLD.cmpl-0.2.step-5',
    # '2024-07-08.JFLD.dstrct-5.step-1',
    # '2024-07-08.JFLD.dstrct-5.step-3',
    # '2024-07-08.JFLD.dstrct-5.step-5',

    # '2024-07-08.JFLD.cmpl-0.2.dstrct-5.step-1',
    # '2024-07-08.JFLD.cmpl-0.2.dstrct-5.step-2',
    # '2024-07-08.JFLD.cmpl-0.2.dstrct-5.step-3',
    # '2024-07-08.JFLD.cmpl-0.2.dstrct-5.step-5',


    # =================================== 2024-07-21.neurips_additional ========================================
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.voc-100.fixed',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.voc-50.fixed',


    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.voc-50.fixed.ref_prob=0.20.theorems-0.1',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.transl_sttng-1.ref_prob=0.20.theorems-0.1',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.rule-G_MP.ref_prob=0.20.theorems-0.1',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.transl-small.ref_prob=0.20.theorems-0.1',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.transl-small.trnsl-old.ref_prob=0.20.theorems-0.1',



    # =================================== 2024-07-21.neurips_additional ========================================

    # we should rename all.
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing'

    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.steps',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.steps-5',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.4-4',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.5-3',


    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.1',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.2',


    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems=0.01',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems=0.03',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems=0.05',


    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.1.theorems=0.1',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.1.theorems=0.2',


    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems=0.01.adjust_theorems',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems=0.03.adjust_theorems',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems=0.05.adjust_theorems',
    # '2024-03-29.JSAI_best.no_aug.trnsl-thing.theorems=0.10.adjust_theorems',



    # =================================== 2024-08-09.fix_depth_problem ========================================

    # '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing',

    # '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.05',
    # '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.10',
    # '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15',

    # '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15.steps-3-4',
    # '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15.steps-4-4',
    # '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15.steps-4-5',
    # '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15.steps-5-3',
    # '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15.steps-5',
    # '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.15.steps-8',

    # '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob_in_1=0.10',
    # '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob_in_1=0.25',
    # '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob_in_1=0.5',
    # '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob_in_1=0.5.theorems=0.01',
    # '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob_in_1=0.5.theorems=0.03',
    # '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob_in_1=0.5.theorems=0.03.adjust_theorems',

    # '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-v2',
    # '2024-08-09.depth_fix.2024-03-29.JSAI_best.no_aug.trnsl-v3',
    # '2024-08-09.depth_fix.2024-03-29.FLD_v2',


    # =================================== 2024-08-12.neurips_camera_ready.towards_best_corpora ========================================
    # '2024-08-12.neurips_camera_ready.towards_best_corpora',
    # '2024-08-12.neurips_camera_ready.towards_best_corpora.wo_trnsl-v2',
    # '2024-08-12.neurips_camera_ready.towards_best_corpora.wo_theorems',
    # '2024-08-12.neurips_camera_ready.towards_best_corpora.suppress_dilemma',
    # '2024-08-12.neurips_camera_ready.towards_best_corpora.suppress_dilemma.theorems-0.003',
    # '2024-08-12.neurips_camera_ready.towards_best_corpora.theorems-0.0001',

    # '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem_tree_prob-0.1',


    # '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--1.0--0.1',
    # '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--1.0--0.01',

    # '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--0.5--0.1',
    # '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--0.5--0.01',

    # '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--0.25--0.1',
    # '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--0.25--0.01',
    # '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--0.25--0.1.G_MP-3',
    # '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--0.25--0.1.G_MP-10',

    # '2024-08-12.neurips_camera_ready.towards_best_corpora.theorem--0.10--0.1',



    # =================================== ./outputs/01.train.py/2024-08-16.neurips_camera_ready ========================================


    # '2024-08-09.depth_fix.2024-03-29.FLD_v2',
    # '2024-08-16.neurips_camera_ready.FLD.small_vocab',


    # '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0',

    # '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.wo_suppress_if',
    # '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.wo_phrase',
    # '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.wo_clause',


    # '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.ref_prob-0.05',
    # '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.ref_prob-0.20',


    # '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.05',
    # '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.15',

    # '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.05.w_flag',
    # '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.15.w_flag',

    # '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.15.w_flag.super_theorems',
    # '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.15.w_flag.super_theorems.syllogism',
    # '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.15.w_flag.super_theorems.syllogism.contraposition',
    # '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.15.w_flag.super_theorems.syllogism.contraposition.and_interchangeability',

    # '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.15.w_flag.super_theorems.ref_prob=0.20',

    # '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v0.theorem--0.25.w_flag',


    # '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v2',
    # '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v2.ref_prob-0.1',
    # '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v2.ref_prob-0.126',
    # '2024-08-09.depth_fix.2024-03-29.FLD_v2.trnsl-thing_person-v2.ref_prob-0.1.theorems-0.25',




    # =================================== 2024-08-30.fix_ref_prob ========================================

    # '2024-08-30.FLD.ref_prob-0.20',
    # '2024-08-30.trnsl-thing_person-v0.ref_prob-0.20',
    # '2024-08-30.trnsl-thing_person-v0.ref_prob-0.20.theorem-G_MP',
    # '2024-08-30.trnsl-thing_person-v0.ref_prob-0.20.theorem-G_MP.syllogism',
    # '2024-08-30.trnsl-thing_person-v0.ref_prob-0.20.theorem-G_MP.syllogism.contraposition',
    # '2024-08-30.trnsl-thing_person-v0.ref_prob-0.20.theorem-G_MP.syllogism.contraposition.interchangeability',
    # '2024-08-30.trnsl-thing_person-v0.ref_prob-0.13.theorem-G_MP.syllogism.contraposition.interchangeability',
    # '2024-08-30.trnsl-thing_person-v0.ref_prob-0.05.theorem-G_MP.syllogism.contraposition.interchangeability',
    # '2024-08-30.trnsl-thing_person-v0.ref_prob-0.20.theorem-all',

    # '2024-08-30.trnsl-thing_person-v0.ref_prob-0.066.theorem-G_MP',


    # ================================== 2024-09-03.toward_camera_ready ========================================
    # '2024-08-30.FLD.ref_prob-0.20',

    # '2024-09-03.trnsl-thing_person-v2',
    # '2024-09-03.trnsl-thing_person-v2.voc-100',
    # '2024-09-03.trnsl-thing_person-v2.dstrct-0',
    # '2024-09-03.trnsl-thing_person-v2.rule-G_MP',
    # '2024-09-03.trnsl-thing_person-v2.stps-3-0',
    # '2024-09-03.trnsl-thing_person-v2.trnsl-small',


    # '2024-09-03.trnsl-thing_person-v0',
    # '2024-09-03.trnsl-thing_person-v0.rule-G_MP',
    # '2024-09-03.trnsl-thing_person-v0.voc-100',
    # '2024-09-03.trnsl-thing_person-v0.dstrct-0',
    # '2024-09-03.trnsl-thing_person-v0.stps-3-0',
    # '2024-09-03.trnsl-thing_person-v0.trnsl-small',


    # ================================== 2024-09-16.fix_negation ========================================
    # '2024-09-16.FLD.neg-0.10',
    # '2024-09-16.PLD.neg-0.10.theorems-0.00.trnsl-old.vocab-5000',
    # '2024-09-16.PLD.neg-0.10.theorems-0.00.trnsl-old',
    # '2024-09-16.PLD.neg-0.10.theorems-0.00',

    # '2024-09-16.PLD.neg-0.10',
    # '2024-09-16.PLD.neg-0.20',
    # '2024-09-16.PLD.neg-0.10.theorems-0.30',
    # '2024-09-16.PLD.neg-0.10.theorems-all',






    # ================================== 2024-09-18.fix_negation ========================================

    # '2024-09-18.FLD.neg-0.10',
    # '2024-09-18.PLD.neg-0.10.theorems-0.00.trnsl-old.vocab-5000',
    # '2024-09-18.PLD.neg-0.10.theorems-0.00.trnsl-old',
    # '2024-09-18.PLD.neg-0.10.theorems-0.00',

    # '2024-09-18.PLD.neg-0.10',

    # '2024-09-18.PLD.neg-0.10.theorems-0.30',
    # '2024-09-18.PLD.neg-0.20',
    # '2024-09-18.PLD.neg-0.10.theorems-all',
    # '2024-09-18.PLD.neg-0.10.ref_prob-0.10',

    # '2024-09-18.PLD.neg-0.10.theorems-0.30.theorems-all',
    # '2024-09-18.PLD.neg-0.15',
    # '2024-09-18.PLD.neg-0.15.theorems-0.30.theorems-all',

    # '2024-09-18.PLD.neg-0.20.trnsl-v2',


    # --------- ablation ---------

    # '2024-09-18.PLD.neg-0.20.voc-100',
    # '2024-09-18.PLD.neg-0.20.dstrct-0',
    # '2024-09-18.PLD.neg-0.20.stps-3-0',
    # '2024-09-18.PLD.neg-0.20.stps-1-0',
    # '2024-09-18.PLD.neg-0.20.rule-G_MP',
    # '2024-09-18.PLD.neg-0.20.trnsl-small',




    # ================================== 2024-09-30.hybrid ========================================

    # '2024-09-30.hybrid__2024-09-18.PLD.neg-0.20__2024-09-18.FLD.neg-0.10',
    # '2024-09-30.hybrid__2024-09-18.PLD.neg-0.20=0.25__2024-09-18.FLD.neg-0.10=0.75',
    # '2024-09-30.hybrid__2024-09-18.PLD.neg-0.20=0.75__2024-09-18.FLD.neg-0.10=0.25',

    # '2024-09-30.hybrid__PLD_v0.theorems-0.3=0.50__FLD=0.25',
    # '2024-09-30.hybrid__PLD_v0.theorems-0.3.theorems-all=0.50__FLD=0.25',
    # '2024-09-30.hybrid__PLD_v2=0.25__PLD_v0=0.50__FLD=0.25',
    # '2024-09-30.hybrid__PLD_v2=0.50__PLD_v0=0.25__FLD=0.25',


    # '2024-09-30.hybrid__PLD_v0.theorems-all=0.50__FLD=0.25',

    # '2024-09-30.hybrid__PLD_v2=0.50__PLD_v0=0.25__FLD=0.25.theorems-all',

    # '2024-09-30.hybrid__PLD_v2=0.37__PLD_v0=0.37__FLD=0.25',
    # '2024-09-30.hybrid__PLD_v2=0.37__PLD_v0=0.37__FLD=0.25.theorems-all',


    # '2024-09-18.FLD.neg-0.20',
    # '2024-09-30.hybrid__PLD_v2=0.25__FLD=0.75',
    # '2024-09-30.hybrid__PLD_v2=0.50__FLD=0.50',
    # '2024-09-30.hybrid__PLD_v2=0.75__FLD=0.25',

    # '2024-09-18.PLD.neg-0.20.trnsl-v2.theorems-all',
    # '2024-09-18.PLD.neg-0.20.trnsl-v2.theorems-all.theorems-0.3',

    # '2024-09-30.hybrid__PLD_v2=0.17__PLD_v0=0.33__FLD=0.50',



    # '2024-09-18.PLD.neg-0.10',
    # '2024-09-30.hybrid__PLD_v0.neg-0.10=0.50__FLD=0.50',


    # '2024-09-30.hybrid__PLD_v2.neg-0.10=0.50__FLD=0.50',


    # '2024-09-18.FLD.neg-0.10.theorems-all.theorems-0.3',
    # '2024-09-18.PLD.neg-0.20.trnsl-v2.theorems-all',
    # '2024-09-18.PLD.neg-0.20.trnsl-v2.theorems-all.theorems-0.3',

    # '2024-09-30.hybrid__PLD_v2=0.50__FLD=0.50',
    # '2024-09-30.hybrid__PLD_v2=0.45__PLD_v0=0.10__FLD=0.45',
    # '2024-09-30.hybrid__PLD_v2=0.40__PLD_v0=0.10__FLD=0.50',


    # '2024-09-30.hybrid__PLD_v2.neg-0.15=0.50__FLD=0.50',


    # '2024-09-18.FLD.neg-0.10.theorems',   # 2.4 hour
    # '2024-09-18.FLD.neg-0.10.theorems.theorems-0.3',

    # '2024-09-18.FLD.neg-0.10.theorems.theorems-all',
    # '2024-09-18.FLD.neg-0.10.theorems.theorems-all.theorems-0.3',
    # '2024-09-18.FLD.neg-0.10.theorems.theorems-all.theorems-0.3.voc-large',
    # '2024-09-18.PLD.neg-0.20.trnsl-v2',

    # '2024-09-18.FLD.neg-0.10.voc-large',





    # '2024-09-18.PLD.neg-0.10.trnsl-v2',
    # '2024-09-18.PLD.neg-0.10.trnsl-v2.theorems-all',
    # '2024-09-18.PLD.neg-0.10.trnsl-v2.theorems-all.theorems-0.3',

    # '2024-09-30.hybrid__PLD_v2.neg-0.10=0.25__FLD=0.75',
    # '2024-09-30.hybrid__PLD_v2.neg-0.10=0.50__FLD=0.50',
    # '2024-09-30.hybrid__PLD_v2.neg-0.10=0.75__FLD=0.25',

    # '2024-09-30.hybrid__PLD_v2.neg-0.10.theorems-all=0.25__FLD=0.75',
    # '2024-09-30.hybrid__PLD_v2.neg-0.10.theorems-all=0.50__FLD=0.50',
    # '2024-09-30.hybrid__PLD_v2.neg-0.10.theorems-all=0.75__FLD=0.25',

    # '2024-09-30.hybrid__PLD_v2.neg-0.10.theorems-all.thelrems-0.3=0.25__FLD=0.75',
    # '2024-09-30.hybrid__PLD_v2.neg-0.10.theorems-all.thelrems-0.3=0.50__FLD=0.50',
    # '2024-09-30.hybrid__PLD_v2.neg-0.10.theorems-all.thelrems-0.3=0.75__FLD=0.25',

    # '2024-09-30.hybrid__PLD_v0.neg-0.10=0.75__FLD=0.25.rule-G_MP',
    # '2024-09-30.hybrid__PLD_v0.neg-0.10=0.75__FLD=0.25.voc-100',
    # '2024-09-30.hybrid__PLD_v0.neg-0.10=0.75__FLD=0.25.dstrct-0',
    # '2024-09-30.hybrid__PLD_v0.neg-0.10=0.75__FLD=0.25.stps-3-0',
    # '2024-09-30.hybrid__PLD_v0.neg-0.10=0.75__FLD=0.25.trnsl-small',

    # '2024-09-18.PLD.neg-0.20.stps-1-0',
    # '2024-09-18.PLD.neg-0.20.stps-2-0',

    # '2024-09-18.PLD.neg-0.20.trnsl-small.trnsl-old',

    # '2024-09-30.hybrid__PLD_v2.neg-0.10=0.10__FLD=0.90',
    # '2024-10-20.hybrid__PLD_v2.neg-0.10=0.10__FLD_theorems=0.40__FLD=0.50',

    # '2024-09-18.FLD.neg-0.10.theorems.voc-large',
    # '2024-10-20.hybrid__PLD_v2.neg-0.10=0.25__FLD_theorems_voc-large=0.25__FLD=0.50',
    # '2024-10-20.hybrid__PLD_v2.neg-0.10=0.10__FLD_theorems_voc-large=0.40__FLD=0.50',

    # '2024-10-20.hybrid__PLD_v2.neg-0.10=0.10__FLD_theorems_voc-large=0.40__FLD_voc-large=0.50',
    # '2024-10-20.hybrid__PLD_v2.neg-0.10=0.10__FLD_theorems_voc-large=0.90',


    # '2024-09-18.FLD.neg-0.10.voc-large.theorems-0.15',
    # '2024-10-23.hybrid__PLD_v2.neg-0.10=0.10__2024-09-18.FLD.neg-0.10.voc-large.theorems-0.15=0.40__FLD_voc-large=0.50',


    # '2024-09-18.FLD.neg-0.10.voc-large.theorems-0.15.rules-G_MP',
    # '2024-09-18.FLD.neg-0.10.voc-large.theorems-0.15.voc-100',
    # '2024-09-18.FLD.neg-0.10.voc-large.theorems-0.15.dstrct-0',
    # '2024-09-18.FLD.neg-0.10.voc-large.theorems-0.15.stps-3-0',
    # '2024-09-18.FLD.neg-0.10.voc-large.theorems-0.15.stps-1-0',
    # '2024-09-18.FLD.neg-0.10.voc-large.theorems-0.15.trnsl-small.trnsl-old',





]

