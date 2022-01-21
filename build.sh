#!/bin/bash

rm -rf build dist ask_jennie.egg-info
python -m build
pip uninstall -y ask-jennie
pip install dist/ask_jennie-0.0.1-py3-none-any.whl
rm -rf sample_projects
mkdir sample_projects
