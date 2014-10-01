@echo off

SET SETUP_DIR=%CD%

cd ../
virtualenv env
cd %SETUP_DIR%

install_packages.bat
