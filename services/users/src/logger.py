import logging
from functools import wraps
logger = logging.getLogger('decorator-log')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


def logger(fn):
    log = logging.getLogger('DECORATOR-LOG ')

    @wraps(fn)
    def inner_logger(*args, **kwargs):
        try:
            value = fn(*args, **kwargs)
            log.debug(f": Called function :: {fn.__name__} with args: {args}, kwargs {kwargs}")
            return value
        except Exception as ex:
            log.error(f"ERROR :: Exception: {ex}")
            raise ex
    return inner_logger