#!/usr/bin/env bash

# full path to script
ABSOLUTE_FILENAME=`readlink -e "$0"`
# folder script
DIRECTORY=`dirname "$ABSOLUTE_FILENAME"`

source "${DIRECTORY}/venv/bin/activate"

python "${DIRECTORY}/src/main.py" &