#!/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'Ma Yonglin'

import time
import functools

def timelog(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        print('call %-15s() in %.6f s:' % (func.__name__, time.time()-start))
        return result
    return wrapper

