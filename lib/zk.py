from kazoo.client import KazooClient

kazoo = None


def start(quorum, aria2_dir):
    global kazoo
    kazoo = KazooClient(hosts=quorum)
    kazoo.start()
    kazoo.get_children(aria2_dir, watch=aria2_changed)


def aria2_changed(event):
    global kazoo
    print "fired"