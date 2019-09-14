#!/usr/bin/env python

import argparse
import logging as log

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--date')
    parser.add_argument('-c', '--color')
    namespace = parser.parse_args()
    log.warning(namespace)


if __name__ == "__main__":
    main()
