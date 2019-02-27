import pickle
import redis

from pymemcache.client import base as memcache
from .exception import ScroogeException


class BaseCache(object):
    cache_backend = None

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._con = None

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, host):
        self._host = host

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        if not str(port).isdigit():
            raise ScroogeException("Port must be numbers")
        self._port = port

    def get(self, key):
        return self._con.get(key)

    def set(self, key, value, **kwargs):
        self._con.set(key, value, **kwargs)

    def clear_namespaces(self):
        self._con.delete('namespaces')

    def register_namespace(self, namespace):
        namespaces = self.get('namespaces')
        if namespaces:
            namespaces = pickle.loads(namespaces)
            if namespace in namespaces:
                raise ScroogeException(f"Scrooge Mcduck got you!! The namespace {namespace} already exist")  # noqa
            namespaces.append(namespace)
            self.set(key='namespaces', value=pickle.dumps(namespaces))
        else:
            self.set(key='namespaces', value=pickle.dumps([namespace]))

    @staticmethod
    def generate_key(*args):
        return "-".join(map(str, args))


class RedisBackend(BaseCache):
    cache_backend = redis

    def __init__(self, db=0, **kwargs):
        super().__init__(**kwargs)
        self._con = self.cache_backend.Redis(host=self.host, port=self.port,
                                             db=db)
        self.clear_namespaces()

    def set(self, **kwargs):
        """
        Overwrite set method to translate expiration_time to redis pattern
        """
        if not kwargs.get('no_cache', False):
            kwargs.pop("no_cache", None)
            if kwargs.get('expiration_time'):
                expiration_time = kwargs['expiration_time']
                del kwargs['expiration_time']
                super().set(ex=expiration_time, **kwargs)
            else:
                super().set(**kwargs)


class MemcacheBackend(BaseCache):
    cache_backend = memcache

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._con = self.cache_backend.Client((self.host, self.port))
        self.clear_namespaces()

    def set(self, **kwargs):
        """
        Overwrite set method to translate expiration_time to memcache pattern
        """
        if not kwargs.get('no_cache', False):
            kwargs.pop("no_cache", None)
            if kwargs.get('expiration_time'):
                expiration_time = kwargs['expiration_time']
                del kwargs['expiration_time']
                super().set(expire=expiration_time, **kwargs)
            else:
                super().set(**kwargs)
