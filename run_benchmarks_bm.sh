#!/bin/bash
[ -e ./logs ] && rm -r ./logs/bm_full_pipeline*

sudo rm -R outputs/XRoom/shimmer

./benchmarks/train_pipeline_bm.sh
