from xr2learn_enablers_cli.call_docker import call_docker, prepare_env_vars
from xr2learn_enablers_cli.conf import SUPPORTED_DATASETS


# import json


def training_pipeline(modality, ssl_pre_train, ed_training, features_type, dataset, docker_env_vars, is_gpu):
    """
    Pipeline entry point

    Parameters
    ----------
    modality: str
        Input data modality supported by the system
    ssl_pre_train: str
        Indicates which elements of SSL pipeline is included,
        encoder + features extraction (encoder_fe),
        encoder only (encoder_only)
        features extraction only (fe_only),
        or not using SSL in the training pipeline: (none)
    ed_training: bool
        Indicates if Supervised Learning is part of the training pipeline.
    features_type: str
        Type of features to include in the training pipeline: ssl or handcrafted
    dataset: str
        Supported dataset to use.
    docker_env_vars: dict
        A dict with the env vars to pass to dockers.
    Returns
    -------
    None

    Raises
    ------
    TypeError
        If the requested dataset is not yet supported.
    """

    # print(docker_env_vars)
    # is_gpu = docker_env_vars.get('GPU', False)
    env_vars = prepare_env_vars(docker_env_vars)
    # print(env_vars)

    if dataset in SUPPORTED_DATASETS:
        if not modality:
            modality = SUPPORTED_DATASETS[dataset]

        if call_docker(f'pre-processing-{modality}', env_vars=env_vars):
            pass

        if features_type == 'handcrafted':
            if call_docker(f'handcrafted-features-generation-{modality}', env_vars=env_vars):
                pass

        if ssl_pre_train != 'none':
            ssl_pipeline(ssl_pre_train, modality, env_vars, is_gpu)

        if bool(ed_training):
            if call_docker(f'ed-training-{modality}', env_vars=env_vars, gpu=is_gpu):
                pass
    else:
        raise TypeError("Requested Dataset not yet support.")


def ssl_pipeline(ssl_pre_train, modality, env_vars, gpu):
    """
    Function to deal with ssl pipeline flow logic.

    Parameters
    ----------
    ssl_pre_train: str
        Indicates which elements of SSL pipeline is included,
        encoder + features extraction (encoder_fe),
        encoder only (encoder_only)
        features extraction only (fe_only),
        or not using SSL in the training pipeline: (none)
    modality: str
        Input data modality supported by the system
    env_vars: dict
        A dict with the env vars to pass to dockers.
    gpu: bool
        If True: Indicates components should use CUDA
        If False: Indicates components should use CPU

    Returns
    -------
    None
    """
    if ssl_pre_train != 'fe_only':
        # The most correct is using the encoder passed on config file. And only train if no encoder has been passed.
        if call_docker(f'ssl-{modality}', env_vars=env_vars, gpu=gpu):
            pass

    if ssl_pre_train == "encoder_only":
        return

    if call_docker(f'ssl-features-generation-{modality}', env_vars=env_vars, gpu=gpu):
        pass
