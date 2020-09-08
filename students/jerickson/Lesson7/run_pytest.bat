rem Set the working directory to where this file is located, then run the pytest command
SET mypath=%~dp0
cd %mypath:~0,-1%

pytest --cov=html_render --cov-report term-missing --random test_html_render.py -v