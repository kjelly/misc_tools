#! /usr/bin/env bash
docker build -t $@ - <  `pwd`/config/dockerfile
