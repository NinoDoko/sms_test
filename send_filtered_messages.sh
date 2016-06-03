#/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

python $DIR/manage.py send_message_through_filter $1
