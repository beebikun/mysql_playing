#!/bin/sh

if [ $# -ne 4 ]; then
    echo "Usage: ./setup.sh USER PSWD START_ID END_ID"
    exit
fi

USER=$1
PSWD=$2
START_ID=$3
END_ID=$4
DB="subscribers_bd"
FILENAME='subscribers'
mysql -u $USER -p$PSWD $DB -e "SELECT * FROM subscribers WHERE id > $START_ID AND id < $END_ID ORDER BY name;" >> $FILENAME
python get.py $FILENAME
