@echo off

REM // Script Directory Settings

SET VIRTUAL_ENV=..\env\
SET REQUIRE_FILE=..\requirements.txt

REM // Script Contents

%VIRTUAL_ENV%Scripts\pip.exe install -r "%REQUIRE_FILE%" --allow-all-external
