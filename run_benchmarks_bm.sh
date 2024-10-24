#!/bin/bash
[ -e ./logs ] && rm -r ./logs/bm_*

sudo rm -R outputs/XRoom/shimmer

./benchmarks/train_pipeline_bm.sh
