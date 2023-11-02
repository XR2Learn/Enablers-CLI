# XR2Learn CLI (Command Line Interface)

A Command Line Interface to use XR2Learn training and inference (not implemented) components.

[CLI Workflow Decision Tree](https://drive.google.com/file/d/1a7m6omAY7VN22QZNpegj_fL_hcf_NEzq/view?usp=sharing)

[Diagram with Architecture Overview](https://drive.google.com/file/d/1k3yLi9Y8tasFMJFNxIwKY-nRJzPdKPLw/view?usp=sharing)

### Installing

**Virtual Environment**
1. Create virtual environment
2. Navigate to the XR2Learn-CLI directory 
3. Install XR2Learn-CLI 
   
    `pip install -e .`

**Dependencies**:

- Docker (or Nvidia-Docker for CUDA)
- Python 3.10

### Quick-Start

Usage: 

`python xr2learn_enablers_cli/xr2learn_enablers.py [COMMAND] [OPTIONS]`

`python xr2learn_enablers_cli/xr2learn_enablers.py --help` for a list of arguments and their description.

### Examples
`python xr2learn_enablers_cli/xr2learn_enablers.py --dataset ravdess --features_type ssl --ssl_pre_train encoder_fe --ed_training true`

### Pre-configured Scripts
`./pre-configured-scripts/audio_pre_train.sh`

`./pre-configured-scripts/audio_fine_tune.sh`

### List of Options
--dataset: 

--features_type: 