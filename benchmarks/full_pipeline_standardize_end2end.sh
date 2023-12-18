#!/bin/bash

# With Frozen Encoder (i.e., pre-train encoder + fine-tuning train)

echo "--------------------"
echo "FULL PIPELINE WITH STANDARDIZE INPUT"
echo "--------------------"

FILE_NAME=configuration_input_standardize_end2end.json
PATH_JSON="./benchmarks/benchmarks_configs/$FILE_NAME"
EXPERIMENT_ID=standardize_full_pipeline

# Dockers called during this use-case:
# Pre-processing
# SSL training
# Sup training

if [ -z "$GPU" ]
then
   GPU=false
fi

python ./xr2learn_enablers_cli/xr2learn_enablers.py --experiment_id $EXPERIMENT_ID --config_file $PATH_JSON --gpu $GPU train --dataset RAVDESS --features_type ssl --ssl_pre_train encoder_fe --ed_training true
