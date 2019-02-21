import pytest

from scrooge.cache import MemcacheCache, RedisCache
from scrooge.client import Client
from scrooge.exception import ScroogeClientException
from tests.conftest import Test


class TestClient:
    def test_boostrap_client_with_another_instance(self):
        with pytest.raises(ScroogeClientException):
            Client(cache_client=Test())

    def test_boostrap_client(self, mocker):
        mocker.patch('redis.Redis')
        mocker.patch('pymemcache.client.Client')
        Client(cache_client=MemcacheCache(host='127.0.0.1', port=1234))
        Client(cache_client=RedisCache(host='127.0.0.1', port=1234))



