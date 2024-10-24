from xr2learn_enablers_cli.call_docker import up_services_dashboard, down_services_dashboard, up_service_emotion_classification_modality


def run_dashboard_pipeline(env_vars, modality_list):
    up_services_dashboard(env_vars=env_vars)

    for modality in modality_list:
        up_service_emotion_classification_modality(env_vars=env_vars, modality=modality)


def stop_demo_ui_pipeline():
    down_services_dashboard()


def run_personalisation_pipeline():
    pass
