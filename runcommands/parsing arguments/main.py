#!/usr/bin/env python

import subprocess
import os


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    child_path = os.path.join(dir_path, 'child.py')
    print(child_path)

    fruits = ['apple', 'oranges']
    date_ts = 123123

    args = [
        '/usr/bin/env', 'python',
        child_path,
        '-f', fruits,
        '-d', date_ts
    ]
    subprocess.Popen(args)


if __name__ == "__main__":
    main()
