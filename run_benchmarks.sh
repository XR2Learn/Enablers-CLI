#!/bin/bash

echo "--------------------"
echo "FULL PIPELINE WITH STANDARDIZE INPUT"
echo "--------------------"
PATH_JSON="./benchmarks_configs/configuration_input_standardize.json"

CONFIG_FILE_PATH=$PATH_JSON docker compose run --rm pre-processing-audio