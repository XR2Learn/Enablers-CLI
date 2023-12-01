import unittest
from unittest.mock import patch, call

from xr2learn_enablers_cli.train import ssl_pipeline


class CliTrainTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch('xr2learn_enablers_cli.train.call_docker')
    def test_ssl_pipeline_call_docker_ssl_training_with_correct_parameters_if_not_fe_only(self, mock_call_docker):
        gpu = False
        env_vars = {'env': 'value'}
        modality = 'audio'
        ssl_pre_train = 'none'
        ssl_pipeline(ssl_pre_train, modality, env_vars, gpu)
        expected_docker_img_name = f'ssl-features-generation-{modality}'
        mock_call_docker.assert_called_with(expected_docker_img_name, env_vars=env_vars, gpu=gpu)
        self.assertEqual(mock_call_docker.call_count, 2)

    @patch('xr2learn_enablers_cli.train.call_docker')
    def test_ssl_pipeline_call_docker_fe_with_correct_parameters_if_not_encoder_only(self, mock_call_docker):
        # The logic is likely wrong, revise it later.
        gpu = False
        env_vars = {'env': 'value'}
        modality = 'audio'
        # ssl_pre_train is always str type
        ssl_pre_train = 'none'
        ssl_pipeline(ssl_pre_train, modality, env_vars, gpu)
        calls = [call(f'ssl-{modality}', env_vars=env_vars, gpu=gpu),
                 call(f'ssl-features-generation-{modality}', env_vars=env_vars, gpu=gpu)]
        # mock_call_docker.assert_called_with(expected_docker_img_name, env_vars=env_vars, gpu=gpu)
        mock_call_docker.assert_has_calls(calls, any_order=True)
        self.assertEqual(mock_call_docker.call_count, 2)
