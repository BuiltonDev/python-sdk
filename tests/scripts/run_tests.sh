#!/usr/bin/env bash

BASEDIR=`dirname "$0"`
ROOTDIR="$BASEDIR/../.."

cd $ROOTDIR

python -m pytest --cov=src

cd -

