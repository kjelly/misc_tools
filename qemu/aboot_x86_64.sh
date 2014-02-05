#! /usr/bin/env bash
echo $0
program=${0#*/a}
`pwd`/$program "$@" &
disown
