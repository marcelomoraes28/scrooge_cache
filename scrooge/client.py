from functools import wraps

import pickle

from scrooge.cache import RedisCache, MemcacheCache
from .exception import ScroogeClientException


class Client(object):
    def __init__(self, cache_client):
        self.cache_client = cache_client

    # The allowed types in callback function
    ALLOWED_TYPES = [dict, list, str, int, float, tuple]

    @property
    def cache_client(self):
        return self._cache_client

    @cache_client.setter
    def cache_client(self, cache_client):
        if not isinstance(cache_client, RedisCache) and not isinstance(cache_client, MemcacheCache):  # noqa
            raise ScroogeClientException("cache_client must be RedisCache or MemcacheCache instance")  # noqa
        self._cache_client = cache_client

    def _validate(self, data):
        """
        Validate if data has one of allowed type
        """
        if type(data) in self.ALLOWED_TYPES:
            return True
        return False

    def gentlemen_cache(self, namespace=None, expiration_time=None):
        """
        This decorator will cache the return of an function
        Rules:
           The return of decorated function must be list or dict or str or int
           or float or tuple
           There must be a unique namespace per function
        :param namespace: str
        :param expiration_time: integer (seconds)
        """

        self.cache_client.register_namespace(namespace=namespace)

        def func_wrapper(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                gen_key = self.cache_client.generate_key(namespace, *args)
                get_result = self.cache_client.get(gen_key)
                if get_result:
                    return pickle.loads(get_result)
                result = func(*args, **kwargs)
                if self._validate(result):
                    self.cache_client.set(gen_key, pickle.dumps(result),
                                          ex=expiration_time)
                    return result
                raise ScroogeClientException(
                    f"The return of {func.__qualname__} can not be object")

            return wrapper

        return func_wrapper
