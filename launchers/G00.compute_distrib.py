#!/usr/bin/env python
import logging
import re
from pathlib import Path
import shutil
import json
from script_engine import QsubEngine, SubprocessEngine

from logger_setup import setup as setup_logger

logger = logging.getLogger(__name__)


def compute_distrib(input_dir: Path, output_dir: Path, max_examples: int):
    engine = SubprocessEngine()
    for input_path in input_dir.glob('**/*.jsonl'):
        # if str(input_path).find('job-') >= 0 or not str(input_path).find('train') >= 0:
        if str(input_path).find('job-') >= 0:
            continue
        lab_prams_path = input_path.parent.parent / 'lab.params.json'
        dataset_name = json.load(open(lab_prams_path))['dataset_name']
        split = re.sub(r'\.jsonl$', '', input_path.name)
        output_path = output_dir / f'dataset_name={dataset_name}.{split}.distrib.txt'
        engine.run(
            f'python ./scripts/compute_distrib.py {str(input_path)} {str(output_path)}',
            f'--max-examples {max_examples}',
            wait_until_finish=True,
        )


def main():
    setup_logger(level=logging.INFO)

    # input_dir = Path('./outputs/00.create_corpus/2024-03-29')
    # output_dir = Path('./outputs/G00.compute_distrib.py/2024-03-29')

    # input_dir = Path('./outputs/00.create_corpus/2024-03-29/dataset_name=2024-03-29.JSAI_best.no_aug.trnsl-thing')
    # output_dir = Path('./outputs/G00.compute_distrib.py/2024-03-29/dataset_name=2024-03-29.JSAI_best.no_aug.trnsl-thing')

    input_dir = Path('./outputs/00.create_corpus/2024-06-08.LPT/dataset_name=2024-03-29.JSAI_best.no_aug.trnsl-thing.large')
    output_dir = Path('./outputs/G00.compute_distrib.py/2024-07-21.neurips_additional/dataset_name=2024-03-29.JSAI_best.no_aug.trnsl-thing.large')

    # input_dir = Path('./outputs/00.create_corpus/2024-07-21.neurips_additional/dataset_name=2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.1')
    # output_dir = Path('./outputs/G00.compute_distrib.py/2024-07-21.neurips_additional/dataset_name=2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.1')

    # input_dir = Path('./outputs/00.create_corpus/2024-07-21.neurips_additional/dataset_name=2024-03-29.JSAI_best.no_aug.trnsl-thing.voc-50.fixed')
    # output_dir = Path('./outputs/G00.compute_distrib.py/2024-07-21.neurips_additional/dataset_name=2024-03-29.JSAI_best.no_aug.trnsl-thing.voc-50.fixed')



    max_examples = 100000
    compute_distrib(input_dir, output_dir, max_examples)


if __name__ == '__main__':
    main()
