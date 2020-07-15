import logging
from logging.handlers import RotatingFileHandler
import os
import time

# Rough log of processing progress
LOGINTERVAL = 1000000
LOG_FORMAT = ' '.join(["%(asctime)s",
                       "%(funcName)s",
                       "line",
                       "%(lineno)d",
                       "%(levelname)-8s",
                       "%(message)s"])
LOG_DATE_FORMAT = '%d %b %Y %H:%M'
LOGFILE_MAX_BYTES = 52000000 
LOGFILE_BACKUP_COUNT = 5

# .............................................................................
def get_logger(name, fname):
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)
    formatter = logging.Formatter(LOG_FORMAT, LOG_DATE_FORMAT)
    handlers = []
    handlers.append(RotatingFileHandler(fname, maxBytes=LOGFILE_MAX_BYTES, 
                                        backupCount=LOGFILE_BACKUP_COUNT))
    handlers.append(logging.StreamHandler())
    for fh in handlers:
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        log.addHandler(fh)
    return log

# ...............................................
def rotate_logfile(log, logpath, logname=None):
    if log is None:
        if logname is None:
            nm, _ = os.path.splitext(os.path.basename(__file__))
            logname = '{}.{}'.format(nm, int(time.time()))
        logfname = os.path.join(logpath, '{}.log'.format(logname))
        log = get_logger(logname, logfname)
    return log
