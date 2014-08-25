#!/usr/bin/python
import sys


def subscriber_generator(filename):
    try:
        subscribers = open(filename).readlines()
    except IOError, e:
        print(e)
        subscribers = []
    to_list = lambda s: s.replace('\n', '').split('\t')
    raw_keys = subscribers[0]
    keys = to_list(raw_keys)
    for subscriber in [s for s in subscribers if s != raw_keys]:
        yield dict(zip(keys, to_list(subscriber)))


def instruction():
    print('\n'.join([
        "Usage: python get.py -p PSWD" +
        "[-u USER -d DBNAME -h HOST -s ID_START -e ID_END]",
        "where:"
        "-p\tMySQL password",
        "-u\tMySQL user ('root' as default)",
        "-d\tMySQL db name ('test_db' as default)",
        "-h\tMySQL-server host (localhost as default)",
        "-s\tsubscriber id which is a filter's start (1234 as default)",
        "-s\tsubscriber id which is a filter's end (1334 as default)",
    ]))
    sys.exit()

SETTINGS = dict(u='root', p=True, d='test_db', h='localhost', s=1234, e=1334)

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        instruction()
    else:
        filename = args[1]
        #here it is
        generator = subscriber_generator(filename)
        for s in generator:
            print s
