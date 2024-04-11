#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker """

import requests
import redis
from functools import wraps
from typing import Callable
redis_clent = redis.Redis()


def url_count(method: Callable) -> Callable:
    """setting the decorator"""
    @wraps(method)
    def wrapper(*args, **kwargs):
        url = args[0]
        redis_client.incr(f"count:{url}")
        cached = redis_client.get(f'{url}')
        if cached:
            return cached.decode('utf-8')
        redis_client.setex(f'{url}, 10, {method(url)}')
        return method(*args, **kwargs)
    return wrapper


@url_count
def get_page(url: str) -> str:
    """get the page """
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    get_page('http://slowly.robertomurray.co.uk')
