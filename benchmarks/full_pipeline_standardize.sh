#!/bin/bash

# With Frozen Encoder (i.e., pre-train encoder + fine-tuning train)

echo "--------------------"
echo "FULL PIPELINE WITH STANDARDIZE INPUT"
echo "--------------------"
PATH_JSON="./benchmarks_configs/configuration_input_standardize.json"

echo "--------------------"
echo "Pre-processing-audio"
echo "--------------------"
CONFIG_FILE_PATH=$PATH_JSON docker compose run --rm pre-processing-audio
echo "--------------------"
echo "SSL-training-audio"
echo "--------------------"
CONFIG_FILE_PATH=$PATH_JSON docker compose run --rm ssl-audio
echo "--------------------"
echo "SSL-features-extraction-audio"
echo "--------------------"
CONFIG_FILE_PATH=$PATH_JSON docker compose run --rm ssl-features-generation-audio
echo "--------------------"
echo "Supervised-training-audio"s
echo "--------------------"
CONFIG_FILE_PATH=$PATH_JSON docker compose run --rm ed-training-audio
echo "--------------------"