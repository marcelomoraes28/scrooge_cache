import pytest
import time
import datetime as dt

from scrooge.exception import ScroogeClientException, ScroogeException
from tests.conftest import m_dict_delay, m_str_delay, m_list_delay, \
    m_float_delay, m_tuple_delay, m_obj_delay, m_int_delay, memcache_client


class TestClientWithRedis:

    def test_same_namespace(self):
        @memcache_client.gentlemen_cache(namespace='name', expiration_time=2)
        def name(delay_time=1):
            return 'foo-bar'

        with pytest.raises(ScroogeException):
            @memcache_client.gentlemen_cache(namespace='name', expiration_time=2)
            def name_(delay_time=1):
                return 'foo-bar'

    def test_client_cache_between_5_seconds(self):
        start = dt.datetime.utcnow()
        m_dict_delay(2, 3)
        end = dt.datetime.utcnow()
        assert (end - start).total_seconds() > 5
        start = dt.datetime.utcnow()
        m_dict_delay(2, 3)
        end = dt.datetime.utcnow()
        assert (end - start).total_seconds() < 1
        time.sleep(2)
        start = dt.datetime.utcnow()
        m_dict_delay(2, 3)
        end = dt.datetime.utcnow()
        assert (end - start).total_seconds() > 5

    def test_client_function_return_obj(self):
        with pytest.raises(ScroogeClientException):
            m_obj_delay(12)

    def test_client_response_if_is_dict(self):
        d1 = m_dict_delay(1, 2)
        assert d1 == {1: 2}

    def test_client_response_if_is_str(self):
        d1 = m_str_delay(1)
        assert d1 == 'foo-bar'

    def test_client_response_if_is_int(self):
        d1 = m_int_delay(2)
        assert d1 == 9

    def test_client_response_if_is_float(self):
        d1 = m_float_delay(3)
        assert d1 == 1.4

    def test_client_response_if_is_list(self):
        d1 = m_list_delay(4)
        assert d1 == ['foo', 'bar']

    def test_client_response_if_is_tuple(self):
        d1 = m_tuple_delay(5)
        assert d1 == (1, 2)
