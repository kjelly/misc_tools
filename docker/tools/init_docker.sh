#! /usr/bin/env bash
EXE_PATH="`dirname \"$0\"`"  
if [ -e container ];then
   echo 'container exists'
   exit 1
fi
if [ -e config ];then
   echo 'config exists'
   exit 1
fi

cp -rf $EXE_PATH/../container .
cp -rf $EXE_PATH/../config .

echo 'Finished. Please put your public key in container folder. And name you public key file with authorized_keys for ssh into you container.'
