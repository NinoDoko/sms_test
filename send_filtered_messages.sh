#/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Attempting to send message : python $DIR/manage.py send_message_through_filter $1"
RESULT="$(python $DIR/manage.py send_message_through_filter $1)"
echo "Result : $RESULT"
