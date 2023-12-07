import unittest
from unittest.mock import patch, call

from xr2learn_enablers_cli.train import ssl_pipeline, training_pipeline


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
        # ssl_pre_train is always str type
        ssl_pre_train = 'none'
        mock_call_docker.return_value = True
        # print(mock_call_docker.mock_calls)
        ssl_pipeline(ssl_pre_train, modality, env_vars, gpu)
        # print(mock_call_docker.mock_calls)

        calls = [call(f'ssl-{modality}', env_vars=env_vars, gpu=gpu),
                 call(f'ssl-features-generation-{modality}', env_vars=env_vars, gpu=gpu)]
        mock_call_docker.assert_has_calls(calls)
        self.assertEqual(mock_call_docker.call_count, 2)

    @patch('xr2learn_enablers_cli.train.call_docker')
    def test_ssl_pipeline_call_docker_fe_with_correct_parameters_if_encoder_only(self, mock_call_docker):
        # The logic is likely wrong, revise it later
        gpu = False
        env_vars = {'env': 'value'}
        modality = 'audio'
        # ssl_pre_train is always str type
        ssl_pre_train = 'encoder_only'
        mock_call_docker.return_value = True
        # print(mock_call_docker.mock_calls)
        ssl_pipeline(ssl_pre_train, modality, env_vars, gpu)
        # print(mock_call_docker.mock_calls)

        calls = [call(f'ssl-{modality}', env_vars=env_vars, gpu=gpu)]
        mock_call_docker.assert_has_calls(calls)
        self.assertEqual(mock_call_docker.call_count, 1)

    @patch('xr2learn_enablers_cli.train.prepare_env_vars')
    @patch('xr2learn_enablers_cli.train.call_docker')
    def test_training_pipeline_call_dockers_with_correct_parameters_with_full_pipeline_no_gpu(self, mock_call_docker,
                                                                                              mock_prep_envs):
        modality = 'audio'
        ssl_pre_train = 'encoder_fe'
        ed_training = True
        features_type = 'handcrafted'
        dataset = 'RAVDESS'
        docker_env_vars = {'env': 'value'}
        is_gpu = False
        mock_call_docker.return_value = True
        mock_prep_envs.return_value = {'env': 'value'}
        training_pipeline(modality, ssl_pre_train, ed_training, features_type, dataset, docker_env_vars, is_gpu)
        calls = [call(f'pre-processing-{modality}', env_vars=docker_env_vars),
                 call(f'handcrafted-features-generation-{modality}', env_vars=docker_env_vars),
                 call(f'ssl-{modality}', env_vars=docker_env_vars, gpu=is_gpu),
                 call(f'ssl-features-generation-{modality}', env_vars=docker_env_vars, gpu=is_gpu),
                 call(f'ed-training-{modality}', env_vars=docker_env_vars, gpu=is_gpu)]
        mock_call_docker.assert_has_calls(calls)
        self.assertEqual(mock_call_docker.call_count, 5)

    @patch('xr2learn_enablers_cli.train.prepare_env_vars')
    @patch('xr2learn_enablers_cli.train.call_docker')
    def test_training_pipeline_call_dockers_with_correct_parameters_with_ssl_pipeline_no_gpu(self, mock_call_docker,
                                                                                             mock_prep_envs):
        modality = 'audio'
        ssl_pre_train = 'encoder_fe'
        ed_training = False
        features_type = 'handcrafted'
        dataset = 'RAVDESS'
        docker_env_vars = {'env': 'value'}
        is_gpu = False
        mock_call_docker.return_value = True
        mock_prep_envs.return_value = {'env': 'value'}
        training_pipeline(modality, ssl_pre_train, ed_training, features_type, dataset, docker_env_vars, is_gpu)
        calls = [call(f'pre-processing-{modality}', env_vars=docker_env_vars),
                 call(f'handcrafted-features-generation-{modality}', env_vars=docker_env_vars),
                 call(f'ssl-{modality}', env_vars=docker_env_vars, gpu=is_gpu),
                 call(f'ssl-features-generation-{modality}', env_vars=docker_env_vars, gpu=is_gpu)]
        mock_call_docker.assert_has_calls(calls)
        self.assertEqual(mock_call_docker.call_count, 4)
