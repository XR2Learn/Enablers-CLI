#!/bin/bash

python xr2learn_enablers_cli/xr2learn_enablers.py --experiment_id supervised_training train --dataset ravdess --features_type handcrafted --ssl_pre_train none --ed_training true
