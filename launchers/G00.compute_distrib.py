#!/usr/bin/env python
import logging
import re
from pathlib import Path
import shutil
import json
from script_engine import QsubEngine, SubprocessEngine
import os
from joblib import Parallel, delayed
from typing import Optional

from logger_setup import setup as setup_logger

logger = logging.getLogger(__name__)


def compute_distrib(input_dir: str, output_dir: str, max_examples: Optional[int] = None) -> None:
    engine = SubprocessEngine()
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)

    for input_path in input_dir.glob('**/*.jsonl'):
        # if str(input_path).find('job-') >= 0 or not str(input_path).find('train') >= 0:
        if str(input_path).find('job-') >= 0:
            continue
        lab_prams_path = input_path.parent.parent / 'lab.params.json'
        split = re.sub(r'\.jsonl$', '', input_path.name)
        output_path = output_dir / f'distrib.{split}.txt'
        engine.run(
            f'python ./scripts/compute_distrib.py {str(input_path)} {str(output_path)}',
            f'--max-examples {max_examples}' if max_examples else '',
            wait_until_finish=False,
        )

    for stats_path in input_dir.glob('**/*jsonl.stats.json'):
        if str(stats_path).find('job-') >= 0:
            continue
        split = re.sub(r'.*\/(.*).jsonl.stats.json$', '\g<1>', str(stats_path))

        engine.run(
            f'ack cum.argument_stats {str(stats_path)} | gawk \'{{print $2 $1}}\' | sort -n -r >{str(output_dir / f"rules.{split}.txt")}',
            wait_until_finish=False,
        )
        # engine.run(
        #     f'ack cum.argument_stats {str(stats_path)} | ack -v \'theorem\' | gawk \'{{print $2 $1}}\' | sort -n -r >{str(output_dir / f"rules-axioms.{split}.txt")}',
        #     wait_until_finish=False,
        # )
        # engine.run(
        #     f'ack cum.argument_stats {str(stats_path)} | ack \'theorem\' | gawk \'{{print $2 $1}}\' | sort -n -r >{str(output_dir / f"rules-theorems.{split}.txt")}',
        #     wait_until_finish=False,
        # )


def main():
    setup_logger(level=logging.INFO)


    # TOP_DIR = './outputs/00.create_corpus/2024-08-09.depth_fix'
    # OUTPUT_TOP_DIR = './outputs/G00.compute_distrib.py/2024-08-09.depth_fix'

    # TOP_DIR = './outputs/00.create_corpus/2024-03-29'
    # OUTPUT_TOP_DIR = './outputs/G00.compute_distrib.py/2024-03-29'

    TOP_DIR = './outputs/00.create_corpus/2024-08-12.neurips_camera_ready.towards_best_corpora'
    OUTPUT_TOP_DIR = './outputs/G00.compute_distrib.py/2024-08-12.neurips_camera_ready.towards_best_corpora'






    jobs = []
    for dataset_dir in os.listdir(TOP_DIR):
        input_dir = str(Path(TOP_DIR) / dataset_dir)
        output_dir = str(Path(OUTPUT_TOP_DIR) / dataset_dir)
        jobs.append(delayed(compute_distrib)(input_dir, output_dir, max_examples=100000))
    Parallel(n_jobs=len(jobs))(jobs)


if __name__ == '__main__':
    main()
