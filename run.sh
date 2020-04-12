#!/bin/bash

PID_FILE=bunny.pid
PORT_NUM=$1
if [ -f "$PID_FILE" ]; then
    kill -9 $(cat $PID_FILE)
    echo "Killing old server $(cat $PID_FILE)"
fi 

if [ -z "${PORT_NUM// }" ]; then 
    PORT_NUM=5000
    echo "Setting default port $PORT_NUM"
else 
    echo "Setting port $PORT_NUM"
fi 

gunicorn --workers=3 -b 127.0.0.1:$PORT_NUM bunny:app -p bunny.pid -D

echo "Bunny2020 is running at http://127.0.0.1:$PORT_NUM/" 
echo "Success! Set http://127.0.0.1:$PORT_NUM/q/?query=%s as your search url to get started" 

