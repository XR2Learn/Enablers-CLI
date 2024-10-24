#!/bin/bash

echo "--------------------"
echo "TRAIN PIPELINE WITH BODY TRACKING"
echo "--------------------"
FILE_NAME=configuration_bm.json
PATH_JSON="./benchmarks/benchmarks_configs/$FILE_NAME"
EXPERIMENT_ID=bm_train_pipeline

if [ -z "$GPU" ]
then
   GPU=false
fi

# Dockers called during this use-case:
# Pre-processing
# Handcrafted features
# SSL training
# Sup training

python xr2learn_enablers_cli/xr2learn_enablers.py --experiment_id $EXPERIMENT_ID --config_file $PATH_JSON --gpu $GPU train --dataset BM --features_type ssl --ssl_pre_train encoder_fe --ed_training true
