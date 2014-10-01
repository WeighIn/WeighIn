@echo off

IF EXIST "..\env\" ( setup\install_packages.bat ) ELSE ( setup\install_virtual_env.bat )
