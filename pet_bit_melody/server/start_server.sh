#!/bin/bash
if [[ -f "${SYSTEM_ENV_LOCATION}/${SYSTEM_ENV_NAME}/bin/activate" ]]; then
    . ${SYSTEM_ENV_LOCATION}/${SYSTEM_ENV_NAME}/bin/activate
elif [[ -f ". ./server_env/bin/activate" ]]; then
    . ./server_env/bin/activate
else
    make create_environement install_dependencies
    if [[ -x ". ./server_env/bin/activate" ]]; then
        . ./server_env/bin/activate
    fi
    echo "Error: Unable to activate environment"
fi

python3 ./src/ \
    --host 0.0.0.0 \
    --port 5000 \
    --debug
