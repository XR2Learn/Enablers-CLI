#!/bin/bash
[ -e ./logs ] && rm -r ./logs/inference_bm_pubsub*

#sudo rm -R outputs/XRoom/shimmer

./benchmarks/inference_bm_pubsub.sh


