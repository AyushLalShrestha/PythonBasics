
import logging as log
import subprocess
from threading import Timer


def _execute_command(command=[]):
    """
    Executes the command using subprocess
    :param command:
    :return:
    """
    if not command:
        return False

    try:
        output = subprocess.check_output(
            command,
            close_fds=True,
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        log.warning(output)
        return output
    except subprocess.CalledProcessError as e:
        log.exception("Error executing command: {}".format(command))


def execute_command(command=[], timeout=2):
    output = None
    if not command:
        return False

    timer = Timer(timeout, log_no_result, args=[command])
    try:
        timer.start()
        output = _execute_command(command)
    finally:
        timer.cancel()
        return output


def log_no_result(command):
    log.warning("Timeout: could not get result for : {}".format(command))


if __name__ == "__main__":
    command = [
        "/usr/bin/sudo",
        "/opt/immune/installed/system/root_actions/zpool.sh",
        "iostat"
    ]
    result = execute_command(command)
    log.warning("got result  : {}".format(result))
