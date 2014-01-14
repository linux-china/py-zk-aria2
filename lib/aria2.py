import os


def start():
    app_dir = os.path.dirname(os.path.realpath(__file__ + "/.."))
    os.system("aria2c --conf-path=" + app_dir + "/conf/aria2.conf")
    print "Aria2 Started"


def stop():
    os.system("killall -9 aria2c")