from concurrent.futures import ProcessPoolExecutor
from concurrent.futures.process import BrokenProcessPool
from time import sleep, time
import logging


def task(message):
    sleep(200)
    print("{}: executed: {}".format(int(time()), message))
    return message


def main():
    try:
        executor = ProcessPoolExecutor(5)

        future_1 = executor.submit(task, ("process 1"))
        future_2 = executor.submit(task, ("process 2"))
    except BrokenProcessPool as bpp:
        logging.exception("Exception occured during executor")

    print(executor._processes)    
    print("{}: Started processes".format(int(time())))
    sleep(2.1)
    print("{}: Is 1 done: {}".format(int(time()), future_1.done()))
    print("{}: Is 2 done: {}".format(int(time()), future_2.done()))
    print("{}: Finished processes".format(int(time())))

if __name__ == '__main__':
    main()
