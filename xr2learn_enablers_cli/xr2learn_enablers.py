import click

from xr2learn_enablers_cli.predict import inference_pipeline, fusion_pipeline, evaluation_pipeline
from xr2learn_enablers_cli.train import training_pipeline


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.option('--experiment_id', required=False, help='Custom identification for the data experiment run')
@click.option('--config_file', required=False, default=None,
              help='Path to the JSON configuration file.')
@click.option('--gpu', required=False, default=False, type=bool,
              help='Run components using CUDA')
@click.pass_context
def cli_general_options(ctx, debug, experiment_id, config_file, gpu):
    ctx.ensure_object(dict)
    if experiment_id:
        ctx.obj['EXPERIMENT_ID'] = experiment_id
    if config_file:
        ctx.obj['CONFIG_FILE_PATH'] = config_file
    if gpu:
        ctx.obj['GPU'] = gpu
    click.echo(f"Debug mode is {'on' if debug else 'off'}")
    device_running = 'GPU' if gpu else 'CPU'
    click.echo(f"Running with {device_running}\n")
    click.echo(f"Experiment ID: {experiment_id}")


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
@click.pass_context
def train(ctx, modality, ssl_pre_train, ed_training, features_type, dataset):
    click.echo('Training Domain')

    vars_dict = {}
    for key in ctx.obj.keys():
        # Think of a better way to do this later!!
        if key != 'GPU':
            vars_dict[key] = ctx.obj[key]

    is_gpu = ctx.obj.get('GPU', False)

    training_pipeline(modality, ssl_pre_train, ed_training, features_type, dataset, vars_dict, is_gpu)


@cli_general_options.command()
@click.option('--dataset', type=click.Choice(['RAVDESS'], case_sensitive=False), required=True, help='Dataset to use')
@click.option('--modality', type=click.Choice(['audio', 'bm', 'body-tracking'], case_sensitive=False), required=False,
              help='Modality')
@click.pass_context
def predict(ctx, modality, dataset):
    vars_dict = {}
    for key in ctx.obj.keys():
        if key != 'GPU':
            vars_dict[key] = ctx.obj[key]

    inference_pipeline(modality, dataset, vars_dict)


@cli_general_options.command()
@click.option('--dataset', type=click.Choice(['RAVDESS'], case_sensitive=False), required=True, help='Dataset to use')
@click.pass_context
def multimodal(ctx, dataset):
    vars_dict = {}
    for key in ctx.obj.keys():
        if key != 'GPU':
            vars_dict[key] = ctx.obj[key]

    fusion_pipeline(dataset, vars_dict)


@cli_general_options.command()
@click.option('--dataset', type=click.Choice(['RAVDESS'], case_sensitive=False), required=True, help='Dataset to use')
@click.pass_context
def evaluate(ctx, dataset):
    vars_dict = {}
    for key in ctx.obj.keys():
        if key != 'GPU':
            vars_dict[key] = ctx.obj[key]

    evaluation_pipeline(dataset, vars_dict)


if __name__ == '__main__':
    cli_general_options()
