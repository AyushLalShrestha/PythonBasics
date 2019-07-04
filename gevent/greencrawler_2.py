# monkey-patch
import gevent.monkey
gevent.monkey.patch_all()

import gevent.pool
import gevent.queue

import sys
import re
import requests

# Prepare a pool for 5 workers and a messaging queue
pool = gevent.pool.Pool(5)
queue = gevent.queue.Queue()
crawled = 0

def crawler():
    '''A very simple queued gevent web crawler'''
    global crawled

    while 1:
        try:
            u = queue.get(timeout=1)
            response = requests.get(u)
            print response.status_code, u

            # Extract some links to follow
            for link in re.findall('<a href="(http.*?)"', response.content):
                # Limit to 10 pages (ignores links when the pool is already full)
                if crawled < 10:
                    crawled += 1
                    queue.put(link)

        except gevent.queue.Empty:
            break

queue.put(sys.argv[1])

while not queue.empty() and not pool.free_count() == 5:
    gevent.sleep(0.1)
    for x in xrange(0, min(queue.qsize(), pool.free_count())):
        pool.spawn(crawler)

# Wait for everything to complete
pool.join()



