WeighIn
=======

[![Build Status](https://magnum.travis-ci.com/dylanplecki/WeighIn.svg?token=he1AtLNKhnxJsTXoLfHx&branch=develop)](https://magnum.travis-ci.com/dylanplecki/WeighIn)

Links
-----

Development Website: http://dev.weighin.me

API Documentation: http://bit.ly/weighin_api_list

Slack Web Board: https://weighin.slack.com

Setup
-----

Before starting the setup procedure, make sure to go to the [JetBrains Student Website](http://www.jetbrains.com/student/) and sign-up for a student account. Then download and install the PyCharm Professional Edition IDE, validating using the student account.

1. First download and install the [Python 2.7](https://www.python.org/download/releases/2.7.8/) intepreter. Ensure that you have no other Python installations on your computer.
2. Download and save the [get-pip.py](https://bootstrap.pypa.io/get-pip.py) file to your computer, preferrably in a short directory.
3. Open a command line terminal and run the command `python /path/to/get-pip.py`, replacing the path with the path of the directory to which you saved the file.
4. Once installed, run this command in the terminal: `pip install virtualenv`.
5. Navigate to the directory in which you cloned the WeighIn git repository using `cd /path/to/weighin/repo` in the terminal.
6. Windows users can skip to step #9 by running the command `tools\setup.bat`.
7. Install the local virtual python environment by running `virtualenv env`.
8. Now we can install the package requirements with the Windows command `env\Scripts\pip.exe install -r "%REQUIRE_FILE%" --allow-all-external` or the Linux/OSX command `env/Scripts/pip install -r "%REQUIRE_FILE%" --allow-all-external`.
9. Open the PyCharm IDE and create a new project. Name the project `WeighIn`, with the location of the Github cloned repository used in set #5, and the `Django project` project type. Make sure the local Python 2.7 virtual environment intepreter is selected. Once finished, a popup may appear asking if you would like to use the existing sources, select yes.
