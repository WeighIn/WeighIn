#!/bin/bash

# Script Directory Settings

virtual_env="../env"
require_file="../requirements.txt"

# Script Contents

$virtual_env/Scripts/pip.exe install -r $require_file --allow-all-external
