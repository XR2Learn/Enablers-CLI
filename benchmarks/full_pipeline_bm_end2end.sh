#!/bin/bash

echo "--------------------"
echo "FULL PIPELINE WITH BM"
echo "--------------------"
FILE_NAME=configuration_bm_end2end.json
PATH_JSON="./benchmarks/benchmarks_configs/$FILE_NAME"
EXPERIMENT_ID=bm_full_pipeline_end2end

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
