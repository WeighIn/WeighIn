#!/bin/bash

python_dir="/usr/lib/python2.7/python"

cwd=$(pwd)

cd ../
virtualenv env -p $python_dir
cd $cwd

./install_packages.sh
