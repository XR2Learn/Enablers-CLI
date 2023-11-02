import click

from xr2learn_enablers_cli.train import pipeline


@click.group()
@click.option('--debug/--no-debug', default=False)
def cli_general_options(debug):
    click.echo(f"Debug mode is {'on' if debug else 'off'}")


@cli_general_options.command()
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
def train(modality, ssl_pre_train, ed_training, features_type, dataset):
    click.echo('Training Domain')
    pipeline(modality, ssl_pre_train, ed_training, features_type, dataset)


if __name__ == '__main__':
    cli_general_options()
