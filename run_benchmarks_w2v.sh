
export GPU=true;

sudo rm -R outputs/*
./benchmarks/full_pipeline_w2v_finetuning_end2end.sh
./benchmarks/predict_ravdess_w2v_finetuning_end2end.sh
./benchmarks/multimodal_ravdess_w2v_finetuning_end2end.sh
./benchmarks/evaluate_ravdess_w2v_finetuning_end2end.sh
