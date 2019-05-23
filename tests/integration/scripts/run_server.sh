#!/usr/bin/env bash

BASEDIR=$(dirname "$0")

# installs packages 
npm i --prefix $BASEDIR/../talkback/

# starts the server
node $BASEDIR/../talkback/index.js
