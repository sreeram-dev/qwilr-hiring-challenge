Qwilr Hiring Challenge
================================

# Local Setup

## Virtual Environment
To install virtualenvwrapper with your default shell - https://itnext.io/virtualenv-with-virtualenvwrapper-on-ubuntu-18-04-goran-aviani-d7b712d906d5

1. Create a python3 virtual env  - `mkvirtualenv --python=/use/bin/python3 qwilr`
2. `workon qwilr` to enter the virtualenv environment
3. Add Project Absolute Path for ex: `$HOME/projects/qwilr` to PYTHONPATH in `$HOME/.virtualenvs/qwilr/postactivate`

Sample PostActivate file looks like this -
```sh
#!/usr/bin/zsh
# This hook is sourced after this virtualenv is activated.

PROJECT_PATH=$HOME/projects/qwilr
SOURCE_PATH=$HOME/projects/qwilr/
export PYTHONPATH=$PYTHONPATH:$SOURCE_PATH

cd $PROJECT_PATH
```

## Installation
1. Run `pip install -r requirements.txt`


# TESTING
1. Run `pytest tests/`
