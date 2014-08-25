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
    print("Usage: python get.py FILENAME")
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
