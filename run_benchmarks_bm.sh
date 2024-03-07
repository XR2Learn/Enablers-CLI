#!/bin/bash
[ -e ./logs ] && rm -r ./logs

sudo rm -R outputs/*
./benchmarks/full_pipeline_bm.sh
./benchmarks/predict_bm.sh
./benchmarks/multimodal_bm.sh
./benchmarks/evaluate_bm.sh

sudo rm -R outputs/*
./benchmarks/full_pipeline_bm_end2end.sh
./benchmarks/predict_bm_end2end.sh
./benchmarks/multimodal_bm_end2end.sh
./benchmarks/evaluate_bm_end2end.sh
