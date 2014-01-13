#! /bin/env python
# -*- coding: utf-8 -*-
import sys
import os


def do_main_program():
    appDir = os.path.dirname(os.path.realpath(__file__ + "/.."))
    os.system("aria2c --conf-path=" + appDir + "/conf/aria2.conf")
    print "started"


def do_stop_program():
    print "stopped"


command = sys.argv[1]

if command == "start":
    do_main_program()
elif command == "stop":
    do_stop_program()
else:
    print "unkown"
