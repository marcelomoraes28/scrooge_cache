import pytest

from scrooge.cache import RedisBackend, MemcacheBackend
from scrooge.exception import ScroogeException


class TestBackends:
    def test_invalid_port(self):
        with pytest.raises(ScroogeException):
            RedisBackend(host='localhost', port='foo-bar')
        with pytest.raises(ScroogeException):
            MemcacheBackend(host='localhost', port='foo-bar')
