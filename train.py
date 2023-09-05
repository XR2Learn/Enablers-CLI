import click


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")


def call_docker(docker_service_name, arguments):
    pass


@click.command()
@click.option('--dataset', default='RAVDESS', help='Dataset supported by XR2Learn Enablers')
@click.option('--pre_train', default=True, help='Indicates if SSL is part of the training pipeline')
@click.option('--fine_tune', default=False, help='Indicates if Supervised Learning is part of the training pipeline')
def pipeline(dataset, pre_train, fine_tune):
    """Pipeline entry point"""
    click.echo(dataset)
    click.echo(pre_train)
    click.echo(fine_tune)


if __name__ == '__main__':
    pipeline()
