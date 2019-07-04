# monkey-patch
import requests
import re
import sys
import gevent.pool
import gevent.monkey
gevent.monkey.patch_all()

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


# Prepare a pool for 5 workers
pool = gevent.pool.Pool(5)

# Crawl tracker is back
crawled = 0

# Read the seed url from stdin
url = "https://www.reddit.com/"
# pool.spawn(crawler, sys.argv[1])
pool.spawn(crawler, url)

# Wait for everything to complete
pool.join()
