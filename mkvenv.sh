#!/bin/bash
basedir=$(dirname $0)
cd $basedir

virtualenv venv --python=python3
. venv/bin/activate
pip install -r requirements.txt
