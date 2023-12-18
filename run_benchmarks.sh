#!/bin/bash

sudo rm -R outputs/*
./benchmarks/full_pipeline_eGeMAPs.sh
./benchmarks/predict_ravdess_eGeMAPs.sh
./benchmarks/multimodal_ravdess_eGeMAPs.sh
./benchmarks/evaluate_ravdess_eGeMAPs.sh

sudo rm -R outputs/*
./benchmarks/full_pipeline_eGeMAPs_end2end.sh
./benchmarks/predict_ravdess_eGeMAPs_end2end.sh
./benchmarks/multimodal_ravdess_eGeMAPs_end2end.sh
./benchmarks/evaluate_ravdess_eGeMAPs_end2end.sh

sudo rm -R outputs/*
./benchmarks/full_pipeline_standardize.sh
./benchmarks/predict_ravdess_standardize.sh
./benchmarks/multimodal_ravdess_standardize.sh
./benchmarks/evaluate_ravdess_standardize.sh

sudo rm -R outputs/*
./benchmarks/full_pipeline_standardize_end2end.sh
./benchmarks/predict_ravdess_standardize_end2end.sh
./benchmarks/multimodal_ravdess_standardize_end2end.sh
./benchmarks/evaluate_ravdess_standardize_end2end.sh