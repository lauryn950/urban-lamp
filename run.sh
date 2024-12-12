#!/bin/bash

set -es

function install_requirements {
    echo "Installing requirements..."
    pip3 install -r requirements.txt
}

function run_unit_tests {
    echo "Running unit tests ..."
    pytest -v
}

install_requirements
run_unit_tests