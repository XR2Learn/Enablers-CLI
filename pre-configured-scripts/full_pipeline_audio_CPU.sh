#!/bin/bash

python xr2learn_enablers_cli/xr2learn_enablers.py --experiment_id supervised_training train --dataset ravdess --features_type ssl --ssl_pre_train encoder_fe --ed_training true
