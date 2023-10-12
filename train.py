import subprocess
# import os
import click

SUPPORTED_DATASETS = {
    'RAVDESS': 'audio'}


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    # click.echo(count)
    # click.echo(name)
    for x in range(count):
        click.echo(f"Hello {name}!")


def call_docker(docker_service_name):
    """
    Function to call a docker subprocess. And wait until it is processed.
    :param docker_service_name: STRING - docker service name (from docker-compose.yml)
    :return: bool if finished with success
    """
    # In case needed to pass ENVVARS
    # Passing the ENVVARS I want to pass to docker container
    # my_vars = os.environ.copy()
    # my_vars['KEY'] = 'Great Key'
    print("\n.")
    print(f"Calling Docker {docker_service_name} \n.\n")
    docker_cmd = f'docker compose run --rm {docker_service_name}'
    # p1 = subprocess.Popen(docker_cmd.split(' '), env=my_vars)
    p1 = subprocess.Popen(docker_cmd.split(' '))
    exit_code = p1.wait()
    success = exit_code == 0
    return success


@click.command()
@click.option('--dataset', type=click.Choice(['RAVDESS'], case_sensitive=False), required=True, help='Dataset to use')
@click.option('--modality', type=click.Choice(['audio', 'bm', 'body-tracking'], case_sensitive=False), required=False,
              help='Modality')
@click.option('--features_type', type=click.Choice(['ssl', 'handcrafted'], case_sensitive=False), required=True,
              help='Type of Features')
@click.option('--ssl_pre_train',
              type=click.Choice(['encoder_fe', 'encoder_only', 'fe_only', 'none'], case_sensitive=False),
              required=True,
              help='Indicates which elements of SSL pipeline is included, encoder + features extraction, '
                   'or encoder only '
                   'or features extraction only')
@click.option('--ed_training', required=True, type=bool,
              help='Indicates if Supervised Learning is part of the training pipeline')
def pipeline(modality, ssl_pre_train, ed_training, features_type, dataset):
    """
    Pipeline entry point
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
        raise TypeError("Custom Dataset not yet support.")


def ssl_pipeline(ssl_pre_train, modality):
    if ssl_pre_train != 'fe_only':
        if call_docker(f'ssl-{modality}'):
            pass

    if ssl_pre_train == "encoder_only":
        return

    if call_docker(f'ssl-features-generation-{modality}'):
        pass


if __name__ == '__main__':
    pipeline()
