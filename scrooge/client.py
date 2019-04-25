from functools import wraps

import pickle

from scrooge.cache import RedisBackend, MemcacheBackend
from .exception import ScroogeClientException


class Client(object):
    def __init__(self, cache_backend):
        self.cache_backend = cache_backend

    # The allowed types in callback function
    ALLOWED_TYPES = [dict, list, str, int, float, tuple]

    @property
    def cache_backend(self):
        return self._cache_backend

    @cache_backend.setter
    def cache_backend(self, cache_backend):
        if not isinstance(cache_backend, RedisBackend) and not isinstance(cache_backend, MemcacheBackend):  # noqa
            raise ScroogeClientException("cache_backend must be RedisCache or MemcacheCache instance")  # noqa
        self._cache_backend = cache_backend

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

        self.cache_backend.register_namespace(namespace=namespace)

        def func_wrapper(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                no_cache = kwargs.get('no_cache', False)
                force_cache_update = kwargs.get('force_cache_update', False)
                gen_key = self.cache_backend.generate_key(namespace, *args)
                if no_cache:
                    return func(*args, **kwargs)
                elif not force_cache_update:
                    get_result = self.cache_backend.get(gen_key)
                    if get_result:
                        return pickle.loads(get_result)
                result = func(*args, **kwargs)
                if self._validate(result):
                    self.cache_backend.set(key=gen_key,
                                           value=pickle.dumps(result),
                                           expiration_time=expiration_time,
                                           no_cache=no_cache)
                    return result
                raise ScroogeClientException(
                    f"The return of {func.__qualname__} can not be object")

            return wrapper

        return func_wrapper
