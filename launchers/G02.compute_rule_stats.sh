#!/bin/bash

# STATS_FILE=./outputs/00.create_corpus/2024-07-21.neurips_additional/dataset_name=2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.1.theorems=0.1/cntxt_shffls_pr_instnc=1/knwldg_argmnt_fctr=1.0/prpstnl_argmnts_fctr=1.0/smpl_all_stncs_pr_lgc=False/thrm_argmnts_fctr=0.1/trnsltn_adj_vrb_nn_rt=1-1-1/trnsltn_n_trnstv_objct=False/train/train.jsonl.stats.json
# OUTPUT_DIR=./outputs/G02.compute_rule_stats.sh/2024-08-08/


# STATS_FILE=./outputs/00.create_corpus/2024-07-21.neurips_additional/dataset_name=2024-03-29.JSAI_best.no_aug.trnsl-thing.ref_prob=0.1/cntxt_shffls_pr_instnc=1/knwldg_argmnt_fctr=1.0/prpstnl_argmnts_fctr=1.0/smpl_all_stncs_pr_lgc=False/trnsltn_adj_vrb_nn_rt=1-1-1/trnsltn_n_trnstv_objct=False/train/train.jsonl.stats.json
# OUTPUT_DIR=./outputs/G02.compute_rule_stats.sh/2024-08-08.ref_prob=0.1/


STATS_FILE=./outputs/00.create_corpus/2024-03-29/dataset_name=2024-03-29.JSAI_best.no_aug.trnsl-v2/cntxt_shffls_pr_instnc=1/knwldg_argmnt_fctr=1.0/prpstnl_argmnts_fctr=1.0/smpl_all_stncs_pr_lgc=False/trnsltn_adj_vrb_nn_rt=1-1-1/trnsltn_n_trnstv_objct=False/train/train.jsonl.stats.json
OUTPUT_DIR=./outputs/G02.compute_rule_stats.sh/2024-08-08.ref_prob=None/



if [ ! -d ${OUTPUT_DIR} ]; then
  mkdir -p ${OUTPUT_DIR}
fi

echo "Writing to \"${OUTPUT_DIR}\""

ack cum.argument_stats ${STATS_FILE} | ack -v 'theorem' | gawk '{print $2 $1}' | sort -n -r >$OUTPUT_DIR/axioms.txt
ack cum.argument_stats ${STATS_FILE} | ack 'theorem' | gawk '{print $2 $1}' | sort -n -r >$OUTPUT_DIR/theorems.txt
