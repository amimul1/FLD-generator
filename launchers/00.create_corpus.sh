#!/bin/bash

REGION=$1
RESOURCE=$2

if [ -z $REGION ]; then
  echo "Usage: $0 <REGION>"
  exit 1
fi

if [ -z $RESOURCE ]; then
  echo "Usage: $0 <REGION> <RESOURCE>"
  exit 1
fi

launch-qsub\
  "./launchers/run_create_corpus.py 1>log.run_create_corpus.txt 2>&1"\
  $REGION\
  $RESOURCE
