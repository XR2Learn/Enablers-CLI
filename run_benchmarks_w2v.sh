[ -e ./logs ] && rm -r ./logs

export GPU=true;

sudo rm -R outputs/RAVDESS
./benchmarks/full_pipeline_w2v_finetuning_end2end.sh
./benchmarks/predict_ravdess_w2v_finetuning_end2end.sh