"""
If this file gets any signal, the child subprocess wil continue 
to run in the background and do it's job.

However, if this parent process gets 'control + C', python will raise a
keyboardInterrupt exception and also explicitly kill it's subproccesses 
hence killing the child processes as well
"""
import logging
import subprocess
import signal
import os
import time


def sighandler(signum, frame):
    if signum == signal.SIGTERM:
        print("got TERMinate")
        signal.signal(signum, signal.SIG_DFL)
    elif signum == signal.SIGINT:
        print("got INTerrupte")
        signal.signal(signum, signal.SIG_DFL)
    os.kill(os.getpid(), signum)


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, sighandler)
    signal.signal(signal.SIGINT, sighandler)

    args = [
        'python',
        '/Users/ayushshrestha/my_projects/PythonBasics/subprocess/child_file.py'
    ]
    sp = subprocess.Popen(args, close_fds=True)
    logging.warning("Running child")
    while True:
        continue
