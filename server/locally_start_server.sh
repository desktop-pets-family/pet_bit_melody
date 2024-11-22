#!/bin/bash
# Author: Henry Letellier

ENVIRONEMENT_PATH=./server_env/bin/activate
if [[ -f "$ENVIRONEMENT_PATH" ]]; then
    . $ENVIRONEMENT_PATH
else
    make create_environement install_dependencies
    if [[ -f "$ENVIRONEMENT_PATH" ]]; then
        . $ENVIRONEMENT_PATH
    fi
    echo "Error: Unable to activate environment"
fi

python3 -m src \
    --host 0.0.0.0 \
    --port 5000 \
    --debug
deactivate
