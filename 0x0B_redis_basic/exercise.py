#!/usr/bin/env python3
""""
initialize import
"""
import re
import redis
from typing import Union, Optional, Callable
from uuid import uuid4
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Method count_calls
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        Wrapper
        """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Method call_history
    """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        Wrapper
        """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper


def replay(method: Callable):
    """
    Method replay
    """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"
    redis = method.__self__._redis
    counter = redis.get(key).decode("utf-8")
    print("{} was called {} times:".format(key, counter))
    input_list = redis.lrange(inputs, 0, -1)
    output_list = redis.lrange(outputs, 0, -1)
    redis_zipped = list(zip(input_list, output_list))
    for j, i in redis_zipped:
        attr, data = j.decode("utf-8"), i.decode("utf-8")
        print("{}(*{}) -> {}".format(key, attr, data))


class Cache():
    """"
    Class that Cache
    """

    def __init__(self):
        """
        method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Method generated key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] =
            None) -> Union[str, bytes, int, float]:
        """
        Method get
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """"
        Method to get str
        """
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """"
        Method to get int
        """
        data = self._redis.get(key)
        try:
            data = int(data.decode("utf-8"))
        except Exception:
            data = 0
        return data
