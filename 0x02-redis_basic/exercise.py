#!/usr/bin/env python3
""" """

import redis
import uuid
from tping import Union
from collectio.abc import Callable


class Cache(object):
    """#"""
    def _init_(self):
        """#"""
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(data: str | bytes | int | float):
        """#"""



        return str
    def get():
        return
    def get_str():
