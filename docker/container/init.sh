#! /usr/bin/env bash
rm -rf /etc/supervisor
ln -s /host/supervisor /etc/supervisor
mkdir /root/.ssh
cd /root/.ssh
cp /host/authorized_keys .
supervisord
/usr/sbin/sshd -D
