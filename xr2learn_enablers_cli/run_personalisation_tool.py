from xr2learn_enablers_cli.call_docker import up_services_demo_ui, down_services_demo_ui


def run_demo_ui_pipeline(env_vars, publisher, modality):
    up_services_demo_ui(env_vars=env_vars, publisher=publisher, modality=modality)


def stop_demo_ui_pipeline():
    down_services_demo_ui()


def run_personalisation_pipeline():
    pass
