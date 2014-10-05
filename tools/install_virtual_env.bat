@echo off

SET PYTHON_DIR="C:\Lib\Python27\python.exe"
SET SETUP_DIR=%CD%

cd ../
virtualenv env -p %PYTHON_DIR%
cd %SETUP_DIR%

install_packages.bat
