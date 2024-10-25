#!/bin/bash

echo "--------------------"
echo "TRAIN PIPELINE WITH BODY TRACKING"
echo "--------------------"
FILE_NAME=configuration_bm_body-tracking.json
PATH_JSON="./benchmarks/benchmarks_configs/$FILE_NAME"
EXPERIMENT_ID=body_tracking_train_pipeline

if [ -z "$GPU" ]
then
   GPU=false
fi

# Dockers called during this use-case:
# Pre-processing
# Sup training

python xr2learn_enablers_cli/xr2learn_enablers.py --experiment_id $EXPERIMENT_ID --config_file $PATH_JSON --gpu $GPU train --dataset Xroom --modality body-tracking --features_type none --ssl_pre_train none --ed_training true