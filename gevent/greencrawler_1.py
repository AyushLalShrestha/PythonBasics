# monkey-patch
import gevent.monkey
gevent.monkey.patch_all()

import gevent.pool
import sys
import re
import requests

# Prepare a pool for 5 workers
pool = gevent.pool.Pool(5)

# Crawl tracker is back
crawled = 0

def crawler(u):
    '''A very simple pooled gevent web crawler'''
    global crawled

    # Crawl the page, print the status
    response = requests.get(u)
    print response.status_code, u

    # Extract some links to follow
    for link in re.findall('<a href="(http.*?)"', response.content):

        # Limit to 10 pages (ignores links when the pool is already full)
        if crawled < 10 and not pool.full():
            crawled += 1
            pool.spawn(crawler, link)

# Read the seed url from stdin
pool.spawn(crawler, sys.argv[1])

# Wait for everything to complete
pool.join()