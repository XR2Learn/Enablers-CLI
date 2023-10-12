#!/bin/bash

# Deleting All dataset, output files
sudo rm -R datasets/*

sudo rm -R outputs/*

#echo "--------------------"
#echo "Pre-processing-audio"
#echo "--------------------"
#docker compose run --rm pre-processing-audio
#echo "--------------------"
#echo "Handcrafted-features-generation-audio"
#echo "--------------------"
#docker compose run --rm handcrafted-features-generation-audio
#echo "--------------------"
#echo "SSL-training-audio"
#echo "--------------------"
#docker compose run --rm ssl-audio
#echo "--------------------"
#echo "SSL-features-extraction-audio"
#echo "--------------------"
#docker compose run --rm ssl-features-generation-audio
#echo "--------------------"
#echo "Supervised-training-audio"s
#echo "--------------------"
#docker compose run --rm ed-training-audio
#echo "--------------------"
