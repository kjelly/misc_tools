#! /usr/bin/env bash

echo "'$1'"
terminator -e "$1"&
#disown
