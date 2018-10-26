
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)-6s: %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='/Users/ayushshrestha/Desktop/basicLogging.txt')
logging.warn('This will get logged as a Warning!')