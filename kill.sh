PID_FILE=bunny.pid
if [ -f "$PID_FILE" ]; then
    kill -9 $(cat $PID_FILE)
    echo "Killing gunicorn process $(cat $PID_FILE)"
fi 