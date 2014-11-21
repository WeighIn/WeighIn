@echo off

IF EXIST "..\env\" (
install_packages.bat
) ELSE (
install_virtual_env.bat
)
