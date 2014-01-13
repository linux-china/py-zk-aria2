Python ZooKeeper Aria2
===========================================================
Integration Aria2 with ZooKeeper by Python glue language

### Protocol

* xml-rpc: Aria2

### Python ZooKeeper Client
All the download tasks are saved in "/aria2" and named as "task-xxx", and content is xml-rpc content.
http://kazoo.readthedocs.org/

### Python daemon

*  https://pypi.python.org/pypi/python-daemon/
*  http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/


### Flow

* Python script to start Aria2. If aria2c started, skipped.
* Python script connected to ZooKeeper quorum and set children watch on "/aria2"
* Watcher fired, and Python script to get the content and execute xml-rpc command to Aria2

### Directory structure

* bin: command
* conf: aria2.conf to setup Aria2 and zk.conf to setup ZooKeeper
* scripts: hooks for Aria2
