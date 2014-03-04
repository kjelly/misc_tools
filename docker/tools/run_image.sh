#! /usr/bin/env bash
export a=a$RANDOM$RANDOM
echo $a > container_name
docker run -v `pwd`/container:/host:rw -p 22 -p 80 -p 443 -p 8080 -p 8000 -d -name $a $@ bash /host/init.sh
