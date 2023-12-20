#!/bin/bash

# With Frozen W2V2

echo "--------------------"
echo "EVALUATE RAVDESS AND STANDARDIZE"
echo "--------------------"

FILE_NAME=configuration_w2v_finetuning_end2end.json
PATH_JSON="./benchmarks/benchmarks_configs/$FILE_NAME"
EXPERIMENT_ID=w2v_finetuning_end2end

python ./xr2learn_enablers_cli/xr2learn_enablers.py --experiment_id $EXPERIMENT_ID --config_file $PATH_JSON evaluate --dataset ravdess