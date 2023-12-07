import unittest
from unittest.mock import patch, call

from xr2learn_enablers_cli.predict import inference_pipeline, evaluation_pipeline, fusion_pipeline


class CliPredictTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch('xr2learn_enablers_cli.predict.prepare_env_vars')
    @patch('xr2learn_enablers_cli.predict.call_docker')
    def test_inference_pipeline_call_docker_with_correct_parameters_with_supported_dataset(self, mock_call_docker,
                                                                                           mock_prep_envs):
        modality = 'audio'
        dataset = 'RAVDESS'
        docker_env_vars = {'env': 'value'}
        mock_prep_envs.return_value = docker_env_vars
        mock_call_docker.return_value = True
        inference_pipeline(modality, dataset, docker_env_vars)
        calls = [call(f'emotion-classification-{modality}', env_vars=docker_env_vars)]
        mock_call_docker.assert_has_calls(calls)
        self.assertEqual(mock_prep_envs.call_count, 1)
        self.assertEqual(mock_call_docker.call_count, 1)

    @patch('xr2learn_enablers_cli.predict.prepare_env_vars')
    @patch('xr2learn_enablers_cli.predict.call_docker')
    def test_evaluate_pipeline_call_docker_with_correct_parameters_with_supported_dataset(self, mock_call_docker,
                                                                                          mock_prep_envs):
        dataset = 'RAVDESS'
        docker_env_vars = {'env': 'value'}
        mock_prep_envs.return_value = docker_env_vars
        mock_call_docker.return_value = True
        evaluation_pipeline(dataset, docker_env_vars)
        calls = [call(f'ed-evaluation', env_vars=docker_env_vars)]
        mock_call_docker.assert_has_calls(calls)
        self.assertEqual(mock_prep_envs.call_count, 1)
        self.assertEqual(mock_call_docker.call_count, 1)

    @patch('xr2learn_enablers_cli.predict.prepare_env_vars')
    @patch('xr2learn_enablers_cli.predict.call_docker')
    def test_fusion_pipeline_call_docker_with_correct_parameters_with_supported_dataset(self, mock_call_docker,
                                                                                        mock_prep_envs):
        dataset = 'RAVDESS'
        docker_env_vars = {'env': 'value'}
        mock_prep_envs.return_value = docker_env_vars
        mock_call_docker.return_value = True
        fusion_pipeline(dataset, docker_env_vars)
        calls = [call(f'fusion-layer', env_vars=docker_env_vars)]
        mock_call_docker.assert_has_calls(calls)
        self.assertEqual(mock_prep_envs.call_count, 1)
        self.assertEqual(mock_call_docker.call_count, 1)
