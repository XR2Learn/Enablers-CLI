from xr2learn_enablers_cli.call_docker import prepare_env_vars, call_docker
from xr2learn_enablers_cli.conf import SUPPORTED_DATASETS


def inference_pipeline(modality, dataset, docker_env_vars):
    # print(docker_env_vars)
    env_vars = prepare_env_vars(docker_env_vars)

    if dataset in SUPPORTED_DATASETS:
        if not modality:
            modality = SUPPORTED_DATASETS[dataset]
    # implement the case dataset is not supported (not a big problem for now bc it is dealt with before on click
    if call_docker(f'emotion-classification-{modality}', env_vars=env_vars):
        pass


def evaluation_pipeline(dataset, docker_env_vars):
    # print(docker_env_vars)
    env_vars = prepare_env_vars(docker_env_vars)

    if dataset in SUPPORTED_DATASETS:
        if call_docker(f'ed-evaluation', env_vars=env_vars):
            pass


def fusion_pipeline(dataset, docker_env_vars):
    # print(docker_env_vars)
    env_vars = prepare_env_vars(docker_env_vars)

    if dataset in SUPPORTED_DATASETS:
        if call_docker(f'fusion-layer', env_vars=env_vars):
            pass
