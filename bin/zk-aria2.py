#! /bin/env python
# -*- coding: utf-8 -*-
import sys
import os


def do_main_program():
    app_dir = os.path.dirname(os.path.realpath(__file__ + "/.."))
    os.system("aria2c --conf-path=" + app_dir + "/conf/aria2.conf")
    print "Aria2 Started"


def do_stop_program():
    os.system("killall -9 aria2c")
    print "All Stopped"


command = sys.argv[1]

if command == "start":
    do_main_program()
elif command == "stop":
    do_stop_program()
else:
    print "unkown"
