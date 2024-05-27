#!/bin/bash

echo "--------------------"
echo "INFERENCE WITH BM PUB/SUB"
echo "--------------------"
FILE_NAME=configuration_bm_pubsub.json
PATH_JSON="./benchmarks/benchmarks_configs/$FILE_NAME"
EXPERIMENT_ID=bm_full_pipeline

if [ -z "$GPU" ]
then
   GPU=false
fi

# Dockers called during this use-case:
# Pre-processing
# Handcrafted features
# SSL training
# Sup training


### TODO to be implemented!!!
python ./xr2learn_enablers_cli/xr2learn_enablers.py --experiment_id $EXPERIMENT_ID --config_file $PATH_JSON predict --dataset bm
python ./xr2learn_enablers_cli/xr2learn_enablers.py --experiment_id $EXPERIMENT_ID --config_file $PATH_JSON multimodal --dataset bm --publisher true
