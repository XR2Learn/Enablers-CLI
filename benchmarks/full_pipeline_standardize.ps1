Write-Output "--------------------"
Write-Output "FULL PIPELINE WITH STANDARDIZE INPUT"
Write-Output "--------------------"

$FILE_NAME="configuration_input_standardize.json."
$PATH_JSON="./benchmarks_configs/$FILE_NAME"

Write-Output "--------------------"
Write-Output "Pre-processing-audio"
Write-Output "--------------------"
$env:CONFIG_FILE_PATH=$PATH_JSON ; docker compose run --rm pre-processing-audio


Write-Output "--------------------"
Write-Output "Handcrafted-features-generation-audio"
Write-Output "--------------------"
$env:CONFIG_FILE_PATH=$PATH_JSON ; docker compose run --rm handcrafted-features-generation-audio


Write-Output "--------------------"
Write-Output "SSL-training-audio"
Write-Output "--------------------"
$env:CONFIG_FILE_PATH=$PATH_JSON ; docker compose run --rm ssl-audio

Write-Output "--------------------"
Write-Output "SSL-features-extraction-audio"
Write-Output "--------------------"
$env:CONFIG_FILE_PATH=$PATH_JSON ; docker compose run --rm ssl-features-generation-audio

Write-Output "--------------------"
Write-Output "Supervised-training-audio"
Write-Output "--------------------"
$env:CONFIG_FILE_PATH=$PATH_JSON ; docker compose run --rm ed-training-audio

Write-Output "--------------------"