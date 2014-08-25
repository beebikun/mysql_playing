#!/bin/sh

if [ $# -ne 2 ]; then
    echo "Usage: ./setup.sh USER PSWD"
    exit
fi

USER=$1
PSWD=$2
DB="subscribers_bd"
mysql -u $USER -p$PSWD -e "CREATE DATABASE $DB;"
mysql -u $USER -p$PSWD $DB < "dump.sql"
