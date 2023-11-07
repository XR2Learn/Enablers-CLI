#!/bin/bash

# With Frozen Encoder (i.e., pre-train encoder + fine-tuning train)

echo "--------------------"
echo "FULL PIPELINE WITH STANDARDIZE INPUT"
echo "--------------------"

FILE_NAME=configuration_input_standardize.json
PATH_JSON="./benchmarks/benchmarks_configs/$FILE_NAME"
EXPERIMENT_ID=standardize_full_pipeline

# Dockers called during this use-case:
# Pre-processing
# SSL training
# Sup training

python ./xr2learn_enablers_cli/xr2learn_enablers.py --experiment_id $EXPERIMENT_ID --config_file $PATH_JSON train --dataset RAVDESS --features_type ssl --ssl_pre_train encoder_only --ed_training true


#echo "--------------------"
#echo "Pre-processing-audio"
#echo "--------------------"
#CONFIG_FILE_PATH=$PATH_JSON docker compose run --rm pre-processing-audio
#echo "--------------------"
#echo "SSL-training-audio"
#echo "--------------------"
#CONFIG_FILE_PATH=$PATH_JSON docker compose run --rm ssl-audio
#echo "--------------------"
#echo "SSL-features-extraction-audio"
#echo "--------------------"
#CONFIG_FILE_PATH=$PATH_JSON docker compose run --rm ssl-features-generation-audio
#echo "--------------------"
#echo "Supervised-training-audio"s
#echo "--------------------"
#CONFIG_FILE_PATH=$PATH_JSON docker compose run --rm ed-training-audio
#echo "--------------------"