rem Set the working directory to where this file is located, then run the pytest command
SET mypath=%~dp0
cd %mypath:~0,-1%

pytest  --cov=mailroom --cov-report term-missing --random -v