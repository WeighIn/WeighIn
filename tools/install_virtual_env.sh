#!/bin/bash

python_dir="/usr/bin/python2.7"

cwd=$(pwd)

cd ../
virtualenv env -p $python_dir
cd $cwd

./install_packages.sh
