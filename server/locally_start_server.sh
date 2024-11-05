#!/bin/bash
if [[ -f ". ./server_env/bin/activate" ]]; then
    . ./server_env/bin/activate
else
    make create_environement install_dependencies
    if [[ -x ". ./server_env/bin/activate" ]]; then
        . ./server_env/bin/activate
    fi
    echo "Error: Unable to activate environment"
fi

python3 ./main.py \
    --host 0.0.0.0 \
    --port 5000 \
    --debug
