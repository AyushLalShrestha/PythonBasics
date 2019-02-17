#! /usr/bin/local python
import gevent.monkey
gevent.monkey.patch_all()
import gevent
import sys
import re
import requests
import time

greenlets = []

# 1
def crawler(u):
    global crawled

    response = requests.get(u)
    for link in re.findall('<a href="(http.*?)"', response.content):
        if len(greenlets) < 10:
            greenlets.append(gevent.spawn(crawler, link))


t1 = time.time()
greenlets.append(gevent.spawn(crawler, sys.argv[1]))

while len(greenlets) < 10:
    gevent.sleep(1)

# Wait for everything to complete
gevent.joinall(greenlets)

t2 = time.time()

print t2-t1

