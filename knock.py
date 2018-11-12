#!/usr/bin/env python
import socket
import sys

# TODO Add system for bash completion
import argparse

socket.setdefaulttimeout(0.1)

for p in sys.argv[2:]:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print("Connecting to %s:%d" % ((sys.argv[1], int(p))))
        s.connect((sys.argv[1], int(p)))
    except:
        s.close()
