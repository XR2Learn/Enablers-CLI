import subprocess

# import os

# import json
SUPPORTED_DATASETS = {
    'RAVDESS': 'audio'}


def call_docker(docker_service_name):
    """
    Function to call a docker subprocess. And wait until it is processed.

    Parameters
    ----------
    docker_service_name: str
        docker service name (from docker-compose.yml).

    Returns
    -------
    bool
        Representing if docker call finished with success.

    """
    # In case needed to pass ENVVARS
    # Passing the ENVVARS I want to pass to docker container

    # my_vars = os.environ.copy()
    # my_vars['PATH_CUSTOM_SETTINGS'] = 'CUSTOM_SETTINGS'
    print("\n.")
    print(f"Calling Docker {docker_service_name} \n.\n")
    docker_cmd = f'docker compose run --rm {docker_service_name}'
    # p1 = subprocess.Popen(docker_cmd.split(' '), env=my_vars)
    p1 = subprocess.Popen(docker_cmd.split(' '))
    exit_code = p1.wait()
    success = exit_code == 0
    return success


def training_pipeline(modality, ssl_pre_train, ed_training, features_type, dataset, experiment_id):
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
    experiment_id: str
        A custom experiment identification for the run.
    Returns
    -------
    None

    Raises
    ------
    TypeError
        If the requested dataset is not yet supported.
    """

    if dataset in SUPPORTED_DATASETS:
        if not modality:
            modality = SUPPORTED_DATASETS[dataset]

        if call_docker(f'pre-processing-{modality}'):
            pass

        if features_type == 'handcrafted':
            if call_docker(f'handcrafted-features-generation-{modality}'):
                pass

        if ssl_pre_train != 'none':
            ssl_pipeline(ssl_pre_train, modality)

        if bool(ed_training):
            if call_docker(f'ed-training-{modality}'):
                pass
    else:
        raise TypeError("Requested Dataset not yet support.")


def ssl_pipeline(ssl_pre_train, modality):
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

    Returns
    -------
    None
    """
    if ssl_pre_train != 'fe_only':
        if call_docker(f'ssl-{modality}'):
            pass

    if ssl_pre_train == "encoder_only":
        return

    if call_docker(f'ssl-features-generation-{modality}'):
        pass
