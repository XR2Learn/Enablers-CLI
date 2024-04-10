#!/bin/bash
[ -e ./logs ] && rm -r ./logs/egemaps_full_pipeline* ./logs/standardize_full_pipeline*

sudo rm -R outputs/RAVDESS

./benchmarks/full_pipeline_eGeMAPs.sh
./benchmarks/predict_ravdess_eGeMAPs.sh
./benchmarks/multimodal_ravdess_eGeMAPs.sh
./benchmarks/evaluate_ravdess_eGeMAPs.sh


./benchmarks/full_pipeline_eGeMAPs_end2end.sh
./benchmarks/predict_ravdess_eGeMAPs_end2end.sh
./benchmarks/multimodal_ravdess_eGeMAPs_end2end.sh
./benchmarks/evaluate_ravdess_eGeMAPs_end2end.sh


./benchmarks/full_pipeline_standardize.sh
./benchmarks/predict_ravdess_standardize.sh
./benchmarks/multimodal_ravdess_standardize.sh
./benchmarks/evaluate_ravdess_standardize.sh


./benchmarks/full_pipeline_standardize_end2end.sh
./benchmarks/predict_ravdess_standardize_end2end.sh
./benchmarks/multimodal_ravdess_standardize_end2end.sh
./benchmarks/evaluate_ravdess_standardize_end2end.sh