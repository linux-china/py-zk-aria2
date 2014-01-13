#! /bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import tornado.ioloop
from kazoo.client import KazooClient


def my_func(event):
    print "fired"


def do_main_program():
    app_dir = os.path.dirname(os.path.realpath(__file__ + "/.."))
    os.system("aria2c --conf-path=" + app_dir + "/conf/aria2.conf")
    print "Aria2 Started"
    zk = KazooClient(hosts='127.0.0.1:2181')
    zk.start()
    zk.get_children("/aria2", watch=my_func)
    # io loop
    tornado.ioloop.IOLoop.instance().start()


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
