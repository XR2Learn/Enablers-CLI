#!/bin/bash

# With Frozen Encoder (i.e., pre-train encoder + fine-tuning train)

echo "--------------------"
echo "MULTIMODAL RAVDESS AND STANDARDIZE"
echo "--------------------"

FILE_NAME=configuration_input_standardize_end2end.json
PATH_JSON="./benchmarks/benchmarks_configs/$FILE_NAME"
EXPERIMENT_ID=standardize_full_pipeline

# Dockers called during this use-case:
# Pre-processing
# SSL training
# Sup training

python ./xr2learn_enablers_cli/xr2learn_enablers.py --experiment_id $EXPERIMENT_ID --config_file $PATH_JSON multimodal --dataset ravdess
