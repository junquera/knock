#!/usr/bin/env python
import socket
import sys

# TODO Add system for bash completion
import argparse

socket.setdefaulttimeout(0.1)

def knock(host, ports):
    for p in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print("Connecting to %s:%d" % ((host, int(p))))
            s.connect((host, int(p)))
        except Exception as e:
            s.close()

# knock('eldiario.es', [80, 81, 82])
import yaml
import os

def main():
    HOME=os.environ.get('HOME')

    with open('%s/.ssh/knock_conf' % HOME) as f:
        c_text = f.read()
        conf = yaml.load(c_text)


    host_name = sys.argv[1]

    host = conf.get(host_name)

    if not host:
        host = dict(ip=host_name, port=sys.argv[2:])

    host_name = host.get('ip')
    ports = host.get('ports')

    knock(host_name, ports)


if __name__ == '__main__':
    main()
