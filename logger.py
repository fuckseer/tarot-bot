import logging
import sys


def setup_logger():
    logger = logging.getLogger("bot_logger")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', datefmt='%H:%M:%S')

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger


logger = setup_logger()