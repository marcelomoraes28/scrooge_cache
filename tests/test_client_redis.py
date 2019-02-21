import pytest
import time
import datetime as dt

from scrooge.exception import ScroogeClientException, ScroogeException
from tests.conftest import dict_delay, str_delay, list_delay, float_delay, \
    tuple_delay, obj_delay, int_delay, client


class TestClientWithRedis:

    def test_same_namespace(self):
        @client.gentlemen_cache(namespace='name', expiration_time=2)
        def name(delay_time=1):
            return 'foo-bar'

        with pytest.raises(ScroogeException):
            @client.gentlemen_cache(namespace='name', expiration_time=2)
            def name_(delay_time=1):
                return 'foo-bar'

    def test_client_cache_between_5_seconds(self):
        start = dt.datetime.utcnow()
        dict_delay(2, 3)
        end = dt.datetime.utcnow()
        assert (end - start).total_seconds() > 5
        start = dt.datetime.utcnow()
        dict_delay(2, 3)
        end = dt.datetime.utcnow()
        assert (end - start).total_seconds() < 1
        time.sleep(2)
        start = dt.datetime.utcnow()
        dict_delay(2, 3)
        end = dt.datetime.utcnow()
        assert (end - start).total_seconds() > 5

    def test_client_function_return_obj(self):
        with pytest.raises(ScroogeClientException):
            obj_delay(12)

    def test_client_response_if_is_dict(self):
        d1 = dict_delay(1, 2)
        assert d1 == {1: 2}

    def test_client_response_if_is_str(self):
        d1 = str_delay(1)
        assert d1 == 'foo-bar'

    def test_client_response_if_is_int(self):
        d1 = int_delay(2)
        assert d1 == 9

    def test_client_response_if_is_float(self):
        d1 = float_delay(3)
        assert d1 == 1.4

    def test_client_response_if_is_list(self):
        d1 = list_delay(4)
        assert d1 == ['foo', 'bar']

    def test_client_response_if_is_tuple(self):
        d1 = tuple_delay(5)
        assert d1 == (1, 2)