# __main__.py
import sys

from .consumer import Consumer


if __name__ == '__main__':
    consumer = Consumer(sys.argv[1])
    consumer.star_read()