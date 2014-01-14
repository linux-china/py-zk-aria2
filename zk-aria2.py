#! /bin/env python
# -*- coding: utf-8 -*-
import sys
import tornado.ioloop
import tornado.web
from lib import aria2, zk, handlers
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('conf/core.cfg')


def do_main_program():
    global config
    aria2.start()
    zk.start(config.get('ZooKeeper', 'quorum'), config.get('ZooKeeper', 'aria2_dir'))
    # start web server
    application = tornado.web.Application([
        (r"/", handlers.MainHandler),
    ])
    application.listen(config.getint("Core", "listen"))
    tornado.ioloop.IOLoop.instance().start()


def do_stop_program():
    aria2.stop()
    print "All Stopped"


if __name__ == "__main__":
    command = sys.argv[1]
    if command == "start":
        do_main_program()
    elif command == "stop":
        do_stop_program()
    else:
        print "unkown"
