#!/bin/bash


sudo rm -R outputs/*
./benchmarks/full_pipeline_eGeMAPs.sh
./benchmarks/predict_ravdess_eGeMAPs.sh
./benchmarks/multimodal_ravdess_eGeMAPs.sh
./benchmarks/evaluate_ravdess_eGeMAPs.sh
#sudo rm -R outputs/*
#./benchmarks/full_pipeline_standardize.sh
