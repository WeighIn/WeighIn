#!/bin/bash

file="../env/"

if [ -f "$file" ]
then
	bash install_packages.sh
else
	bash install_virtual_env.sh
fi

