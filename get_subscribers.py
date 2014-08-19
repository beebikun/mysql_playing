#!/usr/bin/python
#sudo apt-get install python2.7-mysqldb
import MySQLdb
import random

alphabet = 'qwertyuiopasdfghjklzxcvbnm'


def generated_name():
    l = random.randint(3, 10)
    return ''.join([random.choice(alphabet) for i in xrange(l)])

user = 'root'
pswd = '123'
host = 'localhost'
db_name = 'test_db'
table_name = 'subscriber'
id_start = 1234
id_end = 1334

db = MySQLdb.connect(host=host, user=user, passwd=pswd, db=db_name)
cur = db.cursor()


########Fisrt - create table and generate subscribers

cur.execute('\n'.join(['CREATE TABLE IF NOT EXISTS %s(' % table_name,
                       'id INT NOT NULL AUTO_INCREMENT,',
                       'name VARCHAR(100) NOT NULL,',
                       'PRIMARY KEY ( id )',
                       ');']))

#generate subscribers
for i in xrange(1500):
    cur.execute("INSERT INTO %s (name) VALUES ('%s')" % (
        table_name, generated_name()))


########Now - select needed subscribers from table

cur.execute(
    'SELECT * FROM %s WHERE id > %s AND id < %s ORDER BY name;' % (
        table_name, id_start, id_end))
# here it is!
rows = cur.fetchall()

db.commit()
cur.close()
db.close()
