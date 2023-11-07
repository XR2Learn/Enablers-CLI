#!/bin/bash

# Actually this benchmarks are not the best because they are not testing CLI as well.
# This need to be changed: refactor the benchmarks to run them through CLI

./benchmarks/full_pipeline_eGeMAPs.sh
./benchmarks/full_pipeline_standardize.sh
