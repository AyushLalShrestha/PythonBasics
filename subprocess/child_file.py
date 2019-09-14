

import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)-6s: %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='/tmp/childLogging.log')

if __name__=='__main__':
    count = 0
    while True:
        logging.warning("Log {}".format(count))
        count += 1
        time.sleep(2)