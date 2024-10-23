import logging
import os
import subprocess

from xr2learn_enablers_cli.logger import logging_function_exit_status


@logging_function_exit_status(logger=logging.getLogger("cli_logger"))
def call_docker(docker_service_name, env_vars=None, gpu=False):
    """
    Function to call a docker subprocess. And wait until it is processed.

    Parameters
    ----------
    docker_service_name: str
        docker service name (from docker-compose.yml).
    env_vars: dict
        A dict with the env vars to pass to docker call.
    gpu : bool
        If True: Indicates components should use CUDA
        If False: Indicates components should use CPU

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

    if gpu:
        docker_cmd = f'docker compose -f docker-compose.yml -f docker-compose-gpu.yml run --rm {docker_service_name}'
    else:
        docker_cmd = f'docker compose run --rm {docker_service_name}'

    p1 = subprocess.Popen(docker_cmd.split(' '), env=env_vars)
    # p1 = subprocess.Popen(docker_cmd.split(' '))
    exit_code = p1.wait()
    success = exit_code == 0
    return success


def prepare_env_vars(dict_vars):
    my_vars = os.environ.copy()
    if dict_vars is not None:
        for key in dict_vars.keys():
            my_vars[key] = dict_vars[key]
    return my_vars


@logging_function_exit_status(logger=logging.getLogger("cli_logger"))
def up_services_dashboard(env_vars=None):
    env_vars = prepare_env_vars(env_vars)
    print("\n.")
    print(f"Starting Services to run Dashboard (Personalization Tool)\n.\n")
    docker_cmd = f'docker compose up redis personalization-tool dashboard fusion-layer -d'
    p1 = subprocess.Popen(docker_cmd.split(' '), env=env_vars)
    exit_code = p1.wait()
    success = exit_code == 0
    return success

def up_service_emotion_classification_modality(env_vars, modality):
    env_vars = prepare_env_vars(env_vars)
    docker_cmd = f'docker compose up emotion-classification-{modality} -d'
    p1 = subprocess.Popen(docker_cmd.split(' '), env=env_vars)
    exit_code = p1.wait()
    success = exit_code == 0
    return success

@logging_function_exit_status(logger=logging.getLogger("cli_logger"))
def down_services_demo_ui():
    print("\n.")
    print(f"Stopping Services to run DemoUI (Personalisation Tool)\n.\n")
    docker_cmd = 'docker compose down'
    p1 = subprocess.Popen(docker_cmd.split(' '))
    exit_code = p1.wait()
    success = exit_code == 0
    return success
