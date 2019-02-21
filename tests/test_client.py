import pytest

from scrooge.cache import MemcacheBackend, RedisBackend
from scrooge.client import Client
from scrooge.exception import ScroogeClientException
from tests.conftest import Test


class TestClient:
    def test_boostrap_client_with_another_instance(self):
        with pytest.raises(ScroogeClientException):
            Client(cache_backend=Test())

    def test_boostrap_client(self, mocker):
        mocker.patch('redis.Redis')
        mocker.patch('pymemcache.client.base.Client')
        Client(cache_backend=RedisBackend(host='127.0.0.1', port=1234))
        Client(cache_backend=MemcacheBackend(host='127.0.0.1', port=1234))
