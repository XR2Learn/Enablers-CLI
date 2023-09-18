import subprocess
# import os
import click


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
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

    docker_cmd = f'docker compose run --rm {docker_service_name}'
    # p1 = subprocess.Popen(docker_cmd.split(' '), env=my_vars)
    p1 = subprocess.Popen(docker_cmd.split(' '))
    exit_code = p1.wait()
    success = exit_code == 0
    return success


def fine_tune_pipeline():
    pass


@click.command()
@click.option('--modality', type=click.Choice(['audio', 'bm'], case_sensitive=False), required=True, help='Modality')
@click.option('--features_type', type=click.Choice(['ssl', 'handcrafted', 'none'], case_sensitive=False), required=True,
              help='Type of Features')
@click.option('--ssl_pre_train', type=click.Choice(['encoder_fe', 'encoder_only', 'fe_only'], case_sensitive=False),
              required=True,
              help='Indicates which elements of SSL pipeline is included, encoder + features extraction, '
                   'or encoder only '
                   'or features extraction only')
@click.option('--ed_training', required=True, type=bool,
              help='Indicates if Supervised Learning is part of the training pipeline')
def pipeline(modality, ssl_pre_train, ed_training, features_type):
    """Pipeline entry point"""
    # click.echo(modality)
    # click.echo(ssl_pre_train)
    # click.echo(ed_training)
    if call_docker(f'pre-processing-{modality}'):
        if ssl_pre_train:
            call_docker(f'ssl-{modality}')
        else:
            if call_docker(f'handcrafted-features-generation-{modality}'):
                if ed_training:
                    # print(f'call docker ed-training-{modality}')
                    call_docker(f'ed-training-{modality}')


if __name__ == '__main__':
    pipeline()
