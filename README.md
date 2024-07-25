# [XR2Learn Personalization Enablers]  Command Line Interface (CLI)

Command-line interface (CLI) is an automated interface that facilitates access to the XR2Learn Personalization Enablers
training, inference and
personalization Tools' functionalities. It
allows users to quickly and easily access the XR2Learn Personalization Enablers use cases. CLI includes simplified installation and commands,
pre-configured scripts for common use cases, and benchmarks to evaluate the end-to-end workings of the whole pipeline,
working as an integration test for the system.

To run CLI, you need two elements:

1. CLI commands and options
2. A `configuration.json` file (you can provide a JSON configuration file path as an option to the CLI command, if you
   do
   not provide a JSON configuration file path, the default file is `./configuration.json`).

A default configuration.json file is provided and it can be changed according to the use-case.

### Pre-requisites

- Docker installed (or Nvidia-Docker for CUDA)
- Python 3.10 installed

### Installing

**Virtual Environment**

1. Create virtual environment
2. Navigate to the XR2Learn-CLI directory
3. Install XR2Learn-CLI

   `pip install -e .`

### Basic User Manual:

The general command format to use XR2Learn-CLI is:

`python xr2learn_enablers_cli/xr2learn_enablers.py [OPTIONS] [COMMAND] [OPTIONS]`

For help with the options and commands, access a list of arguments and their description with:

`python xr2learn_enablers_cli/xr2learn_enablers.py --help`

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

`python xr2learn_enablers_cli/xr2learn_enablers.py run_personalisation`

DemoUI can be accessed by [http://127.0.0.1:8000/demo_enabler_six]( http://127.0.0.1:8000/demo_enabler_six)

- Stop Web-based DemoUI (for personalisation tool user interface)

`python xr2learn_enablers_cli/xr2learn_enablers.py stop-demo-ui`

To run with Inference as publisher set option `--publisher true` when `running the run-demo-ui` command:

`python xr2learn_enablers_cli/xr2learn_enablers.py run-demo-ui --publisher true`

(**Note**: Inference as publisher is set as `false` by default and this option overwrites the configuration
form `configuration.json` for Inference as publisher.)

### GPU

To use GPU, include an option with value true `--gpu true` before the command.

**Example**:

`python xr2learn_enablers_cli/xr2learn_enablers.py --experiment_id model_001 --gpu true train --dataset ravdess --features_type ssl --ssl_pre_train encoder_fe --ed_training true`

### Benchmarks

XR2Learn-CLI also includes pre-configured benchmarks, which represent use cases on the enablers functionalities and
serve as integration tests for the end-to-end system formed by CLI and Enablers 2-5.

Some use cases included in the benchmarks are end-to-end system for the audio modality using different representations
of speech, for example spectrals, paralinguistic and transformer-based features.

1. Run benchmarks on Unix based OS:
   `./run_benchmarks.sh`

2. Run benchmarks using GPU
   `GPU=true ./run_benchmarks.sh`

## Compatibility

CLI `v0.1.0` is compatible with:

- XR2Learn Training `v.0.1.0`, `v0.2.0`, `v0.3.0`
- XR2Learn Inference `v.0.1.X`

CLI `v0.2.0` is compatible with:

- XR2Learn Training `v.0.1.0`, `v0.2.0`, `v0.3.0`
- XR2Learn Inference `v.0.2.X`

CLI `v0.3.0` is compatible with:

- XR2Learn Training `v.0.1.0`, `v0.2.0`, `v0.3.0`
- XR2Learn Inference `v.0.2.X`
- XR2Learn Personalisation `v.0.1.X`

CLI `v0.4.X` is compatible with:

- XR2Learn Training `v.0.1.0`, `v0.2.0`, `v0.3.0`
- XR2Learn Inference `v.0.2.X`, `v.0.3.0`
- XR2Learn Personalisation `v.0.1.X`, `v.0.2.0`

CLI `v0.5.X` is compatible with:

- XR2Learn Training `v.0.1.0`, `v0.2.0`, `v0.3.X`, `v0.4.0`, `v0.5.0`
- XR2Learn Inference `v.0.2.X`, `v.0.3.X`, `v0.4.0`, `v0.5.0`
- XR2Learn Personalisation `v.0.1.X`, `v.0.2.X`

CLI `v0.6.0` is compatible with:
- XR2Learn Training `v.0.1.0`, `v0.2.0`, `v0.3.X`, `v0.4.0`, `v0.5.0`
- XR2Learn Inference `v.0.2.X`, `v.0.3.X`, `v0.4.0`, `v0.5.0`, `v0.6.0`
- XR2Learn Personalisation `v.0.1.X`, `v.0.2.X`

### Changelog

A description of the main changes in the project’s versions can be found at [CHANGELOG.md].

To check which is your current version, go to the file [setup.cfg](setup.cfg).

## License

Copyright © 2024, Maastricht University

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Pre-trained and fine-tuned models created using the RAVDESS dataset are shared under
the [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en) license to
comply with the RAVDESS license, as the models are derivative works from this dataset.

Please refer to [LICENSE.md](LICENSE.md) document for more details.

## Links:

[CLI Workflow Decision Tree](/images/CLI_workflow_decision_Tree_v2.png)

[Diagram with Architecture Overview](/images/CLI-Enablers-orverview-DemoUI.png)

[CHANGELOG.md]: CHANGELOG.md