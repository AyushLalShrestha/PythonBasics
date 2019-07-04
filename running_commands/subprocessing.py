

import logging
logging.basicConfig(level=logging.DEBUG)

import subprocess
from threading import Timer


def execute_command(command=[]):
    try:
        if not command:
            return

        sub_proc = subprocess.Popen(
            command, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT, close_fds=True
        )

        timer = Timer(3, sub_proc.kill)
        try:
            timer.start()
            out, err = sub_proc.communicate()
        finally:
            timer.cancel()

            if out:
                logging.info("output is: {}".format(out))
                return out
    except subprocess.CalledProcessError as ex:
        logging.error(ex)
    except Exception as ex:
        logging.error(ex)


def test_pinging_google():
    ping_command = ["ping", "-c", "1", "-s", "1", "-W", "1", "8.8.8.8"]
    result = execute_command(ping_command)


def test_timeout():
    timeout_command = [
        'python',
        '/Users/ayushshrestha/my_projects/PythonBasics/running_commands/dummy_wait.py'
    ]
    execute_command(timeout_command)

if __name__=="__main__":
    test_timeout()
