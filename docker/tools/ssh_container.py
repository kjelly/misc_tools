#! /usr/bin/env python
from subprocess import check_output, Popen
import re


contain_info = check_output('docker ps|grep `cat container_name`', shell=True)
result = re.findall(':\d+->22/tcp', contain_info)
port = result[0][1:-8]

p = Popen("ssh root@127.0.0.1 -p {port}".format(port=port), shell=True)
p.wait()
