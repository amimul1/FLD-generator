#!/usr/bin/env python
import json
import random
import math
import logging
from typing import List, Union, Dict
from pathlib import Path
import copy
from collections import defaultdict
import statistics
import time

import click
from script_engine import QsubEngine, SubprocessEngine
from script_engine.base import EngineBase
from logger_setup import setup as setup_logger, create_file_handler
from lab import build_dir, save_params
from experimental_settings import get_dataset_setting, maybe_option

logger = logging.getLogger(__name__)


@click.command()
def main():
    setup_logger(level=logging.INFO)

    # =================================== 2024-08-12.neurips_camera_ready.towards_best_corpora ========================================
    # output_top_dir = Path('./outputs/00.create_corpus/2024-08-12.neurips_camera_ready.towards_best_corpora')


    # =================================== 2024-08-30.fix_ref_prob ========================================
    # output_top_dir = Path('./outputs/00.create_corpus/2024-08-30.fix_ref_prob')


    # =================================== 2024-09-03.toward_camera_ready ========================================
    output_top_dir = Path('./outputs/00.create_corpus/2024-09-03.toward_camera_ready')




    dataset_names = [

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

        # '2024-09-03.trnsl-thing_person-v0.rule-G_MP',
        # '2024-09-03.trnsl-thing_person-v0.voc-100',
        # '2024-09-03.trnsl-thing_person-v0.dstrct-0',
        # '2024-09-03.trnsl-thing_person-v0.stps-3-0',
        # '2024-09-03.trnsl-thing_person-v0.trnsl-small',
        # '2024-09-03.trnsl-thing_person-v0',

    ]



    # only_gather = False
    only_gather = True


    # job_engines = [SubprocessEngine()]
    # job_engines = [QsubEngine('ABCI', 'rt_C.small')]
    # job_engines = [QsubEngine('haic', 'xcl_s.small'), QsubEngine('haic', 'xcs_s.small')]

    job_engines = [
        # QsubEngine('haic', 'xhn_s.middle'),
        QsubEngine('haic', 'xcs_s.middle'),
        QsubEngine('haic', 'xcl_s.middle'),
    ]























    # ---------------------------- fixed settings --------------------------
    dry_run = False
    # dry_run = True

    # skip_if_exists = False
    skip_if_exists = True

    # for the case some jobs hangs
    timeout_per_job = 3600 * 3

    delete_logs_when_done = True

    num_jobs_for_datasets = None  # we do not need this value.

    if len(job_engines) == 1:
        job_engine = job_engines[0]

        if job_engine.resource in ['xcs_s.small', 'xcl_s.small', 'xhn_s.small']:
            raise ValueError('small resource leads to many jobs running concurrently. Then, when they finishes, many new jobs races to start, which leads to zombies')

        if job_engine.resource == 'rt_C.small':
            num_workers_per_job = 5
        elif job_engine.resource in ['xcs_s.small', 'xcl_s.small', 'xhn_s.middle']:
            num_workers_per_job = 14
        elif job_engine.resource in ['xcs_s.middle', 'xcl_s.middle', 'xhn_s.middle2']:
            num_workers_per_job = 30
        else:
            raise NotImplementedError()

    else:
        num_workers_per_job = 14

    # -- large value can save ABCI points because it avoids that the data loading becomes the bottleneck.
    min_dataset_size_per_job = 30 * num_workers_per_job

    make_dataset_args = [
        output_top_dir,
        job_engines,
        timeout_per_job,
        delete_logs_when_done,
        num_workers_per_job,
        min_dataset_size_per_job,
        skip_if_exists,
        only_gather,
        dry_run,
    ]

    for dataset_name in dataset_names:
        make_dataset(dataset_name, *make_dataset_args)

    logger.info('============================== [00.run_create_corpus.py] done! ============================')


def _make_multiple_value_option(option: str, values: List[str]) -> str:
    return ' '.join([
        f'{option} {value}'
        for value in values
    ])


def make_dataset(dataset_name: str,
                 output_top_dir: Union[str, Path],
                 engines: List[EngineBase],
                 timeout_per_job: int,
                 delete_logs_when_done: bool,
                 num_workers_per_job: int,
                 min_dataset_size_per_job: int,
                 skip_if_exists: bool,
                 only_gather: bool,
                 dry_run: bool) -> None:
    output_top_dir = Path(output_top_dir)


    # ----------------- fixed ------------------
    settings = {
        'dataset_name': dataset_name,
        'num_workers_per_job': num_workers_per_job,
    }
    settings.update(get_dataset_setting(dataset_name))
    if settings['translation_configs'] in ['thing_person.v2']:
        logger.warning('thing_person.v2 is very slow. We recommend to use thing_person.v0 for tuning parameters, then use thing_person.v2 only finally.')

    output_dir = build_dir(
        settings,
        top_dir=str(output_top_dir / f'dataset_name={dataset_name}'),
        short=True,
        dirname_ignore_params=[
            'dataset_name',
            'proof_stances',
            'unknown_ratio',
            'reference_tree_prob',
            'reference_argument_prob_in_depth_1',

            'argument_configs',

            'complex_formula_arguments_weight',
            'quantifier_axiom_arguments_weight',
            'quantify_implication_premise_conclusion_at_once',
            'quantify_all_at_once',

            'generate_stem_steps_range',
            'generate_stem_steps_distrib',
            'distractor_variants_per_tree',
            'translation_variants_per_logic',
            'extend_branches_steps_range',

            'distractor',
            # 'distractor_factor',
            'distractors_range',
            'sample_distractor_prototype_formulas_from_all_possible_formulas',
            'disallow_hard_negative_distractors',
            # 'negative_tree_negated_hypothesis_ratio',
            'disallow_subj_obj_swapped_distractor',
            'use_collapsed_translation_nodes_for_unknown_tree',
            'fallback_from_formula_to_translation_distractor',
            'swap_ng_words_config',

            'translation_distractor',
            'translation_distractors_range',
            'use_fixed_translation',

            'split_sizes',
            'split_wise_settings',

            'translation_lang',
            'translation_configs',
            'limit_vocab_size_per_type',
            'translation_volume_to_weight',
            'trnsltn_adj_vrb_nn_rt',

            'knowledge_range',
            'collapsed_knowledge_range',
            'knowledge_no_shuffle',
            'atomic_filepath',
            'concept_net_100k_filepath',
            'dbpedia_filepath',

            'num_workers_per_job',

            'quantifier_axioms',

            'allow_smaller_proofs',

            'world_assump',
        ],
        save_params=True
    )
    logger.addHandler(create_file_handler(output_dir / 'log.txt'))

    n_engine = 0
    for split, size in settings['split_sizes'].items():
        num_jobs = get_num_jobs(size)

        size_with_margin = int(size * 1.1)   # for the case some jobs fail or hang

        split_output_dir = output_dir / split
        split_output_dir.mkdir(exist_ok=True, parents=True)

        if size_with_margin / num_jobs < min_dataset_size_per_job:
            _num_jobs = max(math.ceil(size_with_margin / min_dataset_size_per_job), 1)
        else:
            _num_jobs = num_jobs
        size_per_job = math.ceil(size_with_margin / _num_jobs)

        # logger.info('============================== [launch_create_FLD_corpus.py] Generating dataset for %s split ============================', split)
        # logger.info('size: %d', size)
        # logger.info('size_with_margin: %d', size_with_margin)
        # logger.info('num_jobs: %d', _num_jobs)
        # logger.info('size_per_job: %d', size_per_job)

        if not only_gather:
            jobs = []
            for i_job in range(_num_jobs):
                job_output_dir = split_output_dir / f'job-{str(i_job).zfill(6)}'
                job_output_dir.mkdir(exist_ok=True, parents=True)

                job_output_path = job_output_dir / f'{split}.jsonl'
                job_log_path = job_output_dir / 'log.txt'

                # if skip_if_exists and job_output_path.exists() and len(open(job_output_path).readlines()) >= 1:
                if skip_if_exists and job_output_path.exists():
                    logger.info('skip %s because', job_output_path)
                    continue

                job_settings = copy.deepcopy(settings)
                job_settings.update(settings.get('split_wise_settings', {}).get(split, {}))
                job_settings['split'] = split
                job_settings['seed'] = i_job

                save_params(job_settings, job_output_dir)

                command = ' '.join([
                    # 'source $HOME/.bashrc &&'
                    # 'echo $PATH > log.path.txt &&'
                    'export LD_LIBRARY_PATH=$HOME/.local/lib:$HOME/.local/lib64:$LD_LIBRARY_PATH &&',
                    # 'echo $LD_LIBRARY_PATH',

                    'python ./scripts/create_corpus.py',

                    f'{job_output_path}',
                    str(int(size_per_job)),

                    f'--generate-stem-steps-range \'{json.dumps(job_settings["generate_stem_steps_range"])}\'',
                    maybe_option('--generate-stem-steps-distrib', job_settings.get("generate_stem_steps_distrib", None)),
                    f'--extend-branches-steps-range \'{json.dumps(job_settings["extend_branches_steps_range"])}\'',
                    maybe_option('--steps-limit', job_settings.get("steps_limit", None)),
                    maybe_option('--depth-limit', job_settings.get("depth_limit", None)),
                    '--increase-depth-by-extend-branches' if job_settings.get('increase_depth_by_extend_branches', False) else '',

                    _make_multiple_value_option('--argument-config', job_settings['argument_configs']),
                    f'--complex-formula-arguments-weight {job_settings["complex_formula_arguments_weight"]}',
                    f'--quantifier-axiom-arguments-weight {job_settings["quantifier_axiom_arguments_weight"]}',
                    _make_multiple_value_option('--quantifier-axiom', job_settings['quantifier_axioms']),
                    maybe_option('--quantification-degree', job_settings.get('quantification_degree', None)),
                    maybe_option('--propositional-arguments-factor', job_settings.get('propositional_arguments_factor', None)),
                    maybe_option('--theorem-tree-prob', job_settings.get('theorem_tree_prob', None)),
                    maybe_option('--theorem-arguments-factor', job_settings.get('theorem_arguments_factor', None)),
                    '--adjust-theorem-argument-weight' if job_settings.get('adjust_theorem_argument_weight', False) else '',
                    maybe_option('--theorem-subset', job_settings.get('theorem_subset', None)),

                    maybe_option('--translation-lang', job_settings.get('translation_lang', None)),
                    _make_multiple_value_option('--translation-config', job_settings['translation_configs']),
                    '--translation-no-transitive-object' if job_settings.get("translation_no_transitive_object", False) else '',
                    '--use-fixed-translation' if job_settings.get("use_fixed_translation", False) else '',
                    maybe_option('--reused-object-nouns-max-factor', job_settings.get("reused_object_nouns_max_factor", None)),
                    f'--limit-vocab-size-per-type {job_settings["limit_vocab_size_per_type"]}' if job_settings.get("limit_vocab_size_per_type", None) is not None else '',
                    maybe_option('--translation-volume-to-weight', job_settings.get("translation_volume_to_weight", None)),
                    maybe_option('--translation-adj-verb-noun-ratio', job_settings.get("translation_adj_verb_noun_ratio", None)),
                    maybe_option('--translation-vocab', job_settings.get("translation_vocab", None)),


                    f'--distractor "{job_settings["distractor"]}"',
                    f'--distractors-range \'{json.dumps(job_settings["distractors_range"])}\'',
                    # maybe_option('--negative-tree-negated-hypothesis-ratio', job_settings.get('negative_tree_negated_hypothesis_ratio', None)),
                    '--sample-distractor-prototype-formulas-from-all-possible-formulas' if job_settings.get('sample_distractor_prototype_formulas_from_all_possible_formulas', False) else '',
                    '--disallow-simplified-tree-formulas-as-distractor-prototype' if job_settings.get('disallow_simplified_tree_formulas_as_distractor_prototype', False) else '',
                    '--disallow-subj-obj-swapped-distractor' if job_settings.get('disallow_subj_obj_swapped_distractor', False) else '',
                    maybe_option('--swap-ng-words-config', job_settings.get("swap_ng_words_config", None)),
                    maybe_option('--translation-distractor', job_settings.get("translation_distractor", None)),
                    f'--translation-distractors-range \'{json.dumps(job_settings["translation_distractors_range"])}\'',
                    '--fallback-from-formula-to-translation-distractor' if job_settings.get('fallback_from_formula_to_translation_distractor', False) else '',

                    f'--knowledge-range \'{json.dumps(job_settings["knowledge_range"])}\'' if job_settings.get('knowledge_range', None) is not None else '',
                    f'--collapsed-knowledge-range \'{json.dumps(job_settings["collapsed_knowledge_range"])}\'' if job_settings.get('collapsed_knowledge_range', None) is not None else '',
                    '--knowledge-no-shuffle' if job_settings.get('knowledge_no_shuffle', False) else '',
                    maybe_option('--knowledge-argument-factor', job_settings.get('knowledge_argument_factor', None)),
                    maybe_option('--atomic-filepath', job_settings.get("atomic_filepath", None)),
                    maybe_option('--concept-net-100k-filepath', job_settings.get("concept_net_100k_filepath", None)),
                    maybe_option('--dbpedia-filepath', job_settings.get("dbpedia_filepath", None)),

                    f'--proof-stances \'{json.dumps(job_settings["proof_stances"])}\'' if "proof_stances" in job_settings else '',
                    f'--world-assump {job_settings["world_assump"]}' if "world_assump" in job_settings else '',
                    maybe_option('--unknown-ratio', job_settings.get("unknown_ratio", None)),
                    maybe_option('--reference-tree-prob', job_settings.get("reference_tree_prob", None)),
                    maybe_option('--reference-argument-prob-in-depth-1', job_settings.get("reference_argument_prob_in_depth_1", None)),
                    '--sample-all-stances-per-logic' if job_settings.get('sample_all_stances_per_logic', False) else '',
                    maybe_option('--context-shuffles-per-instance', job_settings.get("context_shuffles_per_instance", None)),
                    '--use-collapsed-translation-nodes-for-unknown-tree' if job_settings.get('use_collapsed_translation_nodes_for_unknown_tree', False) else '',

                    maybe_option('--distractor-variants-per-tree', job_settings.get("distractor_variants_per_tree", None)),
                    maybe_option('--translation-variants-per-logic', job_settings.get("translation_variants_per_logic", None)),

                    '--allow-smaller-proofs' if job_settings.get('allow_smaller_proofs', False) else '',

                    f'--num-workers {job_settings["num_workers_per_job"]}',
                    f'--seed {job_settings["seed"]}',

                ])

                engine = engines[n_engine]
                n_engine = (n_engine + 1) % len(engines)

                if isinstance(engine, SubprocessEngine):
                    command += f' 2>&1 | tee {str(job_log_path)}'
                    stdout = None
                    stderr = None
                else:
                    command += f' 1>{str(job_log_path)} 2>&1'
                    stdout = job_output_dir / 'stdout.txt'
                    stderr = job_output_dir / 'stderr.txt'

                if delete_logs_when_done and i_job >= 20:
                    # remove large log files.
                    command += f'; rm {str(job_log_path)};'

                job_hours = math.floor(timeout_per_job / 3600)
                kwargs = {
                    'stdout': stdout,
                    'stderr': stderr,
                    'options': {
                        'walltime': f'{job_hours}:00:00',
                        'timeout_from_run': timeout_per_job,
                        # 'force': True,
                    },
                    'dry_run': dry_run,
                }
                engine.run(command, wait_until_finish=False, **kwargs)

            logger.warning('We now start gathering the results without waiting for the jobs to be finished. As the jobs may not be finished, the gathered results will also be incomplete.')

        # -- aggregate results --
        # logger.info('gathering results under %s', split_output_dir)
        cnt = 0
        is_done = False
        job_output_jsonls = sorted([
            path for path in split_output_dir.glob(f'**/*{split}.jsonl')
            if str(path).find('job-') >= 0
        ])
        lines: List[str] = []
        for jsonl in job_output_jsonls:
            # logger.info('loading %s', jsonl)
            if is_done:
                break
            for i_line, line in enumerate(open(jsonl)):
                if cnt >= size:
                    is_done = True
                    break
                try:
                    json.loads(line.rstrip('\n'))
                except json.JSONDecodeError:
                    logger.warning('failed to load json line %d, will be skipped', i_line)
                    continue
                lines.append(line)
                cnt += 1
        output_path = split_output_dir / f'{split}.jsonl'
        random.shuffle(lines)
        with open(output_path, 'w') as f_out:
            for line in lines:
                f_out.write(line)
        logger.info('%d samples are written into "%s"', len(lines), output_path)

        # -- aggregate statistics --
        job_stats_jsonls = sorted([
            path for path in split_output_dir.glob(f'**/*{split}.jsonl.stats.json')
            if str(path).find('job-') >= 0
        ])
        agg_stats: Dict[str, Union[int, List[int]]] = {}
        for stats_path in job_stats_jsonls:
            try:
                stats = json.load(open(stats_path))
            except json.JSONDecodeError:
                logger.warning('failed to load stats file, will be skipped: "%s"', stats_path)
                continue
            for name, cnt in stats.items():
                if name.startswith('cum'):
                    if name in agg_stats:
                        agg_stats[name] += cnt
                    else:
                        agg_stats[name]  = cnt
                elif name.startswith('avg'):
                    if name in agg_stats:
                        agg_stats[name].append(cnt)
                    else:
                        agg_stats[name]  = [cnt]
                elif name.startswith('std'):
                    # TODO: implement
                    pass
        for name, cnt in sorted(agg_stats.items()):
            if name.startswith('avg'):
                agg_stats[name] = statistics.mean(cnt)
        json.dump(dict(agg_stats), open(str(split_output_dir / f'{split}.jsonl.stats.json'), 'w'),
                  ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))


def get_num_jobs(num_examples: int) -> int:
    if num_examples < 100:
        return 1
    elif num_examples in [1_000, 100_000]:
        return 300
    elif num_examples in [150_000]:
        return 450
    elif num_examples in [200_000]:
        return 600
    elif num_examples in [300_000]:
        return 900
    elif num_examples in [1_000_000]:
        return 3000
    else:
        raise NotImplementedError()




if __name__ == '__main__':
    main()
