![XR2Learn](https://raw.githubusercontent.com/XR2Learn/.github/5c0fada6136915b389c1cd2151a0dd2cfc4a5aac/images/XR2Learn%20logo.png)

# Enablers CLI (Command Line Interface)

A Command Line Interface to use XR2Learn training and inference Enablers 2-6 and their components.
To access the Enablers' functionalities, you need two elements:

1. CLI commands and options
2. A `configuration.json` file (you can provide a JSON configuration file path as an option to the CLI command, if you
   do
   not do that, the default file is `./configuration.json`)

### Installing

**Virtual Environment**

1. Create virtual environment
2. Navigate to the XR2Learn-CLI directory
3. Install XR2Learn-CLI

   `pip install -e .`

**Dependencies**:

- Docker (or Nvidia-Docker for CUDA)
- Python 3.10

### Usage:

`python xr2learn_enablers_cli/xr2learn_enablers.py [OPTIONS] [COMMAND] [OPTIONS]`

Help:

`python xr2learn_enablers_cli/xr2learn_enablers.py --help` for a list of arguments and their description.

### Examples

- Training:

`python xr2learn_enablers_cli/xr2learn_enablers.py --experiment_id model_001 train --dataset ravdess --features_type ssl --ssl_pre_train encoder_fe --ed_training true`

- Inference (Predict):

`python xr2learn_enablers_cli/xr2learn_enablers.py --experiment_id model_001 predict --dataset ravdess`

- Inference (Multimodal Fusion):

`python xr2learn_enablers_cli/xr2learn_enablers.py --experiment_id model_001 multimodal --dataset ravdess`

- Inference (Evaluation):

`python xr2learn_enablers_cli/xr2learn_enablers.py --experiment_id model_001 evaluate --dataset ravdess`

- Start Web-based DemoUI (for personalisation tool user interface)
  
`python xr2learn_enablers_cli/xr2learn_enablers.py run-demo-ui`

DemoUI can be accessed by  [http://127.0.0.1:8000/demo_enabler_six]( http://127.0.0.1:8000/demo_enabler_six)

- Stop Web-based DemoUI (for personalisation tool user interface)
  
`python xr2learn_enablers_cli/xr2learn_enablers.py stop-demo-ui`

### GPU

To use GPU, include an option with value true `--gpu true` before the command.

Example:

`python xr2learn_enablers_cli/xr2learn_enablers.py --experiment_id model_001 --gpu true train --dataset ravdess --features_type ssl --ssl_pre_train encoder_fe --ed_training true`

### Pre-configured Scripts

`./pre-configured-scripts/audio_pre_train.sh`

`./pre-configured-scripts/audio_fine_tune.sh`

### Benchmarks

1. Run benchmarks on Unix based OS:
   `./run_benchmarks.sh`

2. Run benchmarks using GPU
   `GPU=true ./run_benchmarks.sh`

### Compatibility

CLI `v0.1.0` is compatible with:

- XR2Learn Training `v.0.1.0`, `v0.2.0`, `v0.3.0`
- XR2Learn Inference `v.0.1.X`

CLI `v0.2.0` is compatible with:

- XR2Learn Training `v.0.1.0`, `v0.2.0`, `v0.3.0`
- XR2Learn Inference `v.0.2.X`

### Changelog

[CHANGELOG.md]

### Links:

[CLI Workflow Decision Tree](https://drive.google.com/file/d/1a7m6omAY7VN22QZNpegj_fL_hcf_NEzq/view?usp=sharing)

[Diagram with Architecture Overview](https://drive.google.com/file/d/1k3yLi9Y8tasFMJFNxIwKY-nRJzPdKPLw/view?usp=sharing)


[CHANGELOG.md]: CHANGELOG.md