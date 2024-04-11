#!/usr/bin/env python3
""" Writing strings to Redis"""

import redis
import uuid
from tping import Union, Callable, Optional
from functools import wraps


def call_history(method: Callabe) -> Callable:
    """Writing strings"""
    method_key = method.__qualname__
    inputs, outputs = method_key + ':inputs', method_key + ':outputs'

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(result))
        return result
    return wrapper

def count_calls(method: Callable) -> Callable:
    """counting calls"""
    method_key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method_key)
        return method(self, *args, **kwargs)
    return wrapper

def replay(method: Callable) -> None:
    """Displays the history of calls"""
    method_key = method.__qualname__
    inputs, outputs = method_key + ':inputs', method_key + ':outputs'
    redis = method.__self__._redis
    method_count = redis.get(method_key).decode('utf-8')
    print(f'{method_key} was called {method_count} times:')
    IOTuple = zip(redis.lrange(inputs, 0, -1), redis.lrange(outputs, 0, -1))
    for inp, outp in list(IOTuple):
        attr, data = inp.decode("utf-8"), outp.decode("utf-8")
        print(f'{method_key}(*{attr}) -> {data}')

class Cache(object):
    """Creating a class in redis"""
    def __init__(self):
        """initializing the created class"""
        self._redis = redis.Redis()
        self._redis.flushdb

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes,  int, float]) -> str:
        """Implementing stores"""
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key

    def get(self,  key: str, fn: Optional[Callable] = None) -> str:):
        """setting up the get function"""
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, data: str) -> str:
        """setting up the get string"""
        return data.decode('utf-8', 'strict')

    def get_int(self, data: str) -> int:
        """Returns int"""
        return int(data)

