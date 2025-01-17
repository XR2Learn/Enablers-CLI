# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
## [1.0.0] - 2024 - 10 - 28
### Added
- support for `body-tracking` modality
- support for multimodality for XRoom dataset (body tracking + bio-measurements) modalities.
- training benchmarks for body-tracking and bio-measurements
- issues template.

### Changed 
- update services names
- config format to match the new versions of Training/Inference tools. 
- Refactoring

### Removed
- Evaluation services - it has been removed from Inference Tools. 
- Non-applicable benchmarks (according to the current repositories versions - check version compatibility on README)
- multimodal click command - multimodal fusion only supports Pub/Sub now. 

## [0.6.0] - 2024 - 07 - 25
### Added
- Support for running DemoUI with Inference Pub/Sub.

### Known Issues
- Does not include support for `body-tracking`. 

## [0.5.1] - 2024 - 04 - 10
### Added 
- Support for new output format of Training and Inference Tools.

### Changed
- Dataset name format from "BM" to "XRoom" for data generated by [Magic XRoom](https://github.com/XR2Learn/magic-xroom).

### Known Issues
- Does not include support for `body-tracking`. 

## [0.5.0] - 2024 - 03 - 12
### Added 
- Support for BM modality 
- Benchmarks for BM modality
- License Update to Apache 2.0.

## [0.4.1] - 2024 - 02 - 15
### Added

- License
- More documentation

## [0.4.0] - 2024 - 01 - 19

### Added

- Integration with DemoUI can now call Inference as a publisher and integration with Unity App

## [0.3.0] - 2024 - 01 - 11

### Added

- Integration with DemoUI for Personalisation Tool (to start and stop DemoUI for personalisation tool)

### Changed

- Refactoring logging tool

### Fixed

- Some links from README.md

## [0.2.0] - 2024 - 01 - 09

### Added

- Wav2vec + Linear Classifier configurations and benchmarks
- Benchmark logger to collect summaries for `call_docker`

### Changed

- Inference benchmarks exploiting config file paths defined in bash scripts
- Updated configs to use inference with two modes: SSL features and end2end

## [0.1.2] - 2023 - 12 - 07

### Added

- Unit Tests for training and inference components.

## [0.1.1] - 2023 - 11 - 28

### Added

- More documentation.

## [0.1.0] - 2023 - 11 - 14

### Added

- Provides an interface for accessing functionalities from Enablers 2-5 and their components.
    - Includes support for GPU.
- Changelog

<!-- 
Example of Categories to use in each release

### Added
- Just an example of how to use changelog.

### Changed
- Just an example of how to use changelog.

### Fixed
- Just an example of how to use changelog.

### Removed
- Just an example of how to use changelog.

### Deprecated
- Just an example of how to use changelog. -->


[unreleased]: https://github.com/XR2Learn/Enablers-CLI/compare/v0.6.0...master

[0.1.0]: https://github.com/XR2Learn/Enablers-CLI/releases/tag/v0.1.0

[0.1.1]: https://github.com/XR2Learn/Enablers-CLI/releases/tag/v0.1.1

[0.1.2]: https://github.com/XR2Learn/Enablers-CLI/releases/tag/v0.1.2

[0.2.0]: https://github.com/XR2Learn/Enablers-CLI/releases/tag/v0.2.0

[0.3.0]: https://github.com/XR2Learn/Enablers-CLI/releases/tag/v0.3.0

[0.4.0]: https://github.com/XR2Learn/Enablers-CLI/releases/tag/v0.4.0

[0.4.1]: https://github.com/XR2Learn/Enablers-CLI/releases/tag/v0.4.1

[0.5.0]: https://github.com/XR2Learn/Enablers-CLI/releases/tag/v0.5.0

[0.5.1]: https://github.com/XR2Learn/Enablers-CLI/releases/tag/v0.5.1

[0.6.0]: https://github.com/XR2Learn/Enablers-CLI/releases/tag/v0.6.0

[1.0.0]: https://github.com/XR2Learn/Enablers-CLI/releases/tag/v1.0.0