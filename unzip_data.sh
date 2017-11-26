#!/usr/bin/bash

FILE="data.zip"

if ! [ -f $FILE ]; then
  echo File $FILE not found, exiting...
  exit 1
fi

unzip $FILE
