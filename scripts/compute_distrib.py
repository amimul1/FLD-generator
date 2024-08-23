#!/usr/bin/env python
import math
import random
import json
from typing import List, Dict, Optional
from pathlib import Path
from pprint import pformat
import logging
from collections import defaultdict

import click
from tqdm import tqdm
import dill


@click.command()
@click.argument('input_path', type=str)
@click.argument('output_path', type=str)
@click.option('--max-examples', type=int, default=None)
def main(input_path, output_path, max_examples):
    input_path = Path(input_path)
    output_path = Path(output_path)
    output_path.parent.mkdir(exist_ok=True, parents=True)

    # ./outputs/10.create_FLD_corpus/20230626.many_bugs_fixed/dataset_name=20230626.many_bugs_fixed.20221203.first_exp__arg-RT__frml-cmpl__dist-20__transl-nrrw__tree-3__dataset_size-30000.G_MP/rsd_objct_nns_mx_fctr=1.0/smpl_hrd_ngtvs=True/try_ngtd_hypthss_frst=True/us_fxd_trnsltn=True/us_smplfd_tr_frmls_as_dstrctr_prttyp=True/test/test.jsonl
    attr_names = [
        'proof_label',
        'world_assump_label',
        'original_tree_depth',
        'depth',
        'total_proof_steps',

        'negative_original_tree_depth',
        'negative_world_assump_label',

        'num_formula_distractors',
        'num_translation_distractors',
        'num_all_distractors',

        # 'op_conjunction',
        # 'op_disjunction',
        # 'op_implication',
        # 'op_negation',
        # 'op_universal',
        # 'op_existential',
        'op_&',
        'op_v',
        'op_->',
        'op_¬',
        'op_(x)',
        'op_(Ex)',
    ]

    counts = defaultdict(lambda: defaultdict(int))
    tot = 0
    for line in open(input_path):
        if max_examples is not None and tot >= max_examples:
            break
        instance = json.loads(line.rstrip('\n'))

        for attr_name in attr_names:

            if attr_name == 'total_proof_steps':
                proofs = instance['proofs']
                if len(proofs) == 0:
                    val = None
                    # counts['total_proof_steps'][None] += 1
                else:
                    proof = proofs[0]
                    total_proof_steps = proof.count(';')
                    val = total_proof_steps
                    # counts['total_proof_steps'][total_proof_steps] += 1

            elif attr_name.startswith('op_'):
                symbol = attr_name[3:]
                val = instance['facts_formula'].count(symbol)
                val += instance['hypothesis_formula'].count(symbol)
                if len(instance['proofs_formula']) > 0:
                    val += instance['proofs_formula'][0].count(symbol)
            else:
                val = instance[attr_name]

            counts[attr_name][val] += 1

        tot += 1

    with open(output_path, 'w') as f_out:
        for attr_name in attr_names:
            print('\n\n\n', file=f_out)
            print(f'------------------ {attr_name} ------------------', file=f_out)
            print(f'{"attr":<10}    {"count":<20}    ratio', file=f_out)
            print('', file=f_out)
            for val, count in sorted(item for item in counts[attr_name].items() if item[0] is not None):
                print(f'{str(val):<10}    [{count:<6,} / {tot:,}]    {count/tot:.2f}', file=f_out)
            for val, count in sorted(item for item in counts[attr_name].items() if item[0] is None):
                print(f'{str(val):<10}    [{count:<6,} / {tot:,}]    {count/tot:.2f}', file=f_out)

            if len(counts[attr_name]) > 0:
                if type(list(counts[attr_name].keys())[0]) == int:
                    sum_count = sum(key * count for key, count in counts[attr_name].items()
                                    if key is not None)
                    print('', file=f_out)
                    print('-- sum --', file=f_out)
                    print(f'sum(attr * counts)   -> {sum_count:<10,}', file=f_out)



if __name__ == '__main__':
    main()
