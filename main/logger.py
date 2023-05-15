import logging
import sys


def setup_logger(level=logging.DEBUG):
    logger = logging.getLogger('ZV')
    logger.setLevel(level)
    if len(logger.handlers) == 0:
        handler1 = logging.FileHandler('log.txt')
        handler2 = logging.StreamHandler(sys.stdout)
        handler1.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
        handler2.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
        logger.addHandler(handler1)
        logger.addHandler(handler2)
    return logger
