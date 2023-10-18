#!/bin/bash

echo "--------------------"
echo "FULL PIPELINE WITH eGeMAPS INPUT"
echo "--------------------"
FILE_NAME=configuration_input_egmaps.json
PATH_JSON="./benchmarks_configs/$FILE_NAME"

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