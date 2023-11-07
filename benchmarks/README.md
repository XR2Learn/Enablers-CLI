# Benchmarks

Benchmarks implement automatic runs of CLI for different use-cases with
the objective of quickly and easily verify if the components are communicating and running as
expected according to the Enablers functionalities and the requested CLI command.

## How to run all benchmarks

1. From the root directory of the project:
    1. For Unix based OS:

       `./run_benchmarks.sh`

    2. For Windows (not yet supported):

       `./run_benchmarks.ps1`

## Implemented Use-cases

### 1. Train: Full Pipeline with eGeMAPS

This use-case means that the user is requiring the whole pipeline (SSL + SL) train using eGeMAPS as input
to the SSL encoder pre-training.

The workflow is highlighted and depicted in this
figure: [Full pipeline eGeMAPS use-case](https://drive.google.com/file/d/1iTOdJddkOl4iTV5bUyCbA6k5jd9is8_V/view?usp=sharing).

### 2. Train: Full Pipeline with Standardize

This use-case means that the user is requiring the whole pipeline (SSL + SL) train using Standardize as input
to the SSL encoder pre-training.

The workflow is highlighted and depicted in this
figure: [Full pipeline Standardize use-case](https://drive.google.com/file/d/1kjIc40OYaEnROqut8yu2opeD66iP6deQ/view?usp=sharing).

## How to add a new benchmark

1. Create the `configuration_my_use_case.json` file with the desired configuration for the given use-case inside the
   folder `./benchmarks/benchmarks_configs`;
2. Create the script to call the CLI command with options for the desired use-case inside the folder `./benchmarks`
3. Add a new line with the new benchmark script into the `./run_benchmarks.sh` script file in the root folder. 


