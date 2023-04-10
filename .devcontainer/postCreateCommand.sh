#!/bin/bash

pip install --user poetry
poetry config virtualenvs.in-project true
poetry config installer.modern-installation false
poetry install
