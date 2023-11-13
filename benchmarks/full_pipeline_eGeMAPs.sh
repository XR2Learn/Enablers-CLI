#!/bin/bash

echo "--------------------"
echo "FULL PIPELINE WITH eGeMAPS INPUT"
echo "--------------------"
FILE_NAME=configuration_input_egmaps.json
PATH_JSON="./benchmarks/benchmarks_configs/$FILE_NAME"
EXPERIMENT_ID=egemaps_full_pipeline

if [ -z "$GPU" ]
then
   GPU=false
fi

# Dockers called during this use-case:
# Pre-processing
# Handcrafted features
# SSL training
# Sup training

python ./xr2learn_enablers_cli/xr2learn_enablers.py --experiment_id $EXPERIMENT_ID --config_file $PATH_JSON --gpu $GPU train --dataset RAVDESS --features_type handcrafted --ssl_pre_train encoder_fe --ed_training true
