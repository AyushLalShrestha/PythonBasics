
import random
import sys
import time


if __name__=="__main__":
    number = random.randint(0, 100)
    if number%2 == 0:
        # print "waiting for infinity"
        while True:
            time.sleep(10)
    else:
        print "not waiting for infinity"
        sys.exit(0)