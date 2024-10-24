#!/bin/bash

echo "--------------------"
echo "TRAIN PIPELINE WITH BM"
echo "--------------------"
FILE_NAME=configuration_bm_body-tracking.json
PATH_JSON="./benchmarks/benchmarks_configs/$FILE_NAME"
EXPERIMENT_ID=bm_train_pipeline

if [ -z "$GPU" ]
then
   GPU=false
fi

python xr2learn_enablers_cli/xr2learn_enablers.py --experiment_id $EXPERIMENT_ID --config_file $PATH_JSON --gpu $GPU train --dataset Xroom --modality bm --features_type ssl --ssl_pre_train encoder_fe --ed_training true