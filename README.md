*Assumed, that mysql-server and mysql-client are already installed*

USAGE
=====

SETUP
-----
First, run a setup shell script
<br>
```
chmod 777 setup.sh
./setup.sh USER PSWD
```
<br>
where USER - it is your username for mysql and PSWD - your password for mysql<br>
<br>
This script creates a table and restores a dump in it.

GET SUBSCRIBER
--------------
```
chmod 777 get.sh
./get.sh USER PSWD START END
```
where USER - it is your username for mysql and PSWD - your password for mysql, START - start subscriber id for a filter, END - end subscriber id for a filter

For example
```
./get.sh root 123 1 10

{'id': '2', 'name': 'jjhf'}
{'id': '3', 'name': 'jjff'}
{'id': '2', 'name': 'jjhf'}
{'id': '5', 'name': 'lcif'}
{'id': '9', 'name': 'mivjci'}
{'id': '4', 'name': 'ptyfawacy'}
{'id': '6', 'name': 'twcsn'}
{'id': '8', 'name': 'xlv'}
{'id': '7', 'name': 'zoeo'}
```


