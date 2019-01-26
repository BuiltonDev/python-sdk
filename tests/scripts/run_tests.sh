#!/usr/bin/env bash


PYTHONPATH=$(dirname "$0")../../ python -m pytest --cov=src


