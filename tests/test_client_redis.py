import pytest
import time
import datetime as dt

from scrooge.exception import ScroogeClientException, ScroogeException
from tests.conftest import r_no_cache, r_dict_delay, r_str_delay, r_list_delay, \
    r_float_delay, r_tuple_delay, r_obj_delay, r_int_delay, redis_client


class TestClientWithRedis:

    def test_same_namespace(self):
        @redis_client.gentlemen_cache(namespace='name', expiration_time=2)
        def name(delay_time=1):
            return 'foo-bar'

        with pytest.raises(ScroogeException):
            @redis_client.gentlemen_cache(namespace='name', expiration_time=2)
            def name_(delay_time=1):
                return 'foo-bar'

    def test_client_cache_between_5_seconds(self):
        start = dt.datetime.utcnow()
        r_dict_delay(2, 3)
        end = dt.datetime.utcnow()
        assert (end - start).total_seconds() > 5
        start = dt.datetime.utcnow()
        r_dict_delay(2, 3)
        end = dt.datetime.utcnow()
        assert (end - start).total_seconds() < 1
        time.sleep(2)
        start = dt.datetime.utcnow()
        r_dict_delay(2, 3)
        end = dt.datetime.utcnow()
        assert (end - start).total_seconds() > 5

    def test_client_function_return_obj(self):
        with pytest.raises(ScroogeClientException):
            r_obj_delay(12)

    def test_client_response_if_is_dict(self):
        d1 = r_dict_delay(1, 2)
        assert d1 == {1: 2}

    def test_client_response_if_is_str(self):
        d1 = r_str_delay(1)
        assert d1 == 'foo-bar'

    def test_client_response_if_is_int(self):
        d1 = r_int_delay(2)
        assert d1 == 9

    def test_client_response_if_is_float(self):
        d1 = r_float_delay(3)
        assert d1 == 1.4

    def test_client_response_if_is_list(self):
        d1 = r_list_delay(4)
        assert d1 == ['foo', 'bar']

    def test_client_response_if_is_tuple(self):
        d1 = r_tuple_delay(5)
        assert d1 == (1, 2)

    def test_client_no_cache(self):
        start = dt.datetime.utcnow()
        no_cache = r_no_cache()
        end = dt.datetime.utcnow()
        assert (end - start).total_seconds() > 2
        assert no_cache == "Scrooge got you!!"
        start = dt.datetime.utcnow()
        r_no_cache(no_cache=True)
        end = dt.datetime.utcnow()
        assert (end - start).total_seconds() > 2
        assert no_cache == "Scrooge got you!!"

    def test_force_cache_update(self):
        start = dt.datetime.utcnow()
        cache = r_no_cache()
        end = dt.datetime.utcnow()
        assert (end - start).total_seconds() > 2
        assert cache == "Scrooge got you!!"
        start = dt.datetime.utcnow()
        cache = r_no_cache()
        end = dt.datetime.utcnow()
        assert (end - start).total_seconds() < 1
        assert cache == "Scrooge got you!!"
        start = dt.datetime.utcnow()
        cache = r_no_cache(force_cache_update=True)
        end = dt.datetime.utcnow()
        assert (end - start).total_seconds() > 2
        assert cache == "Scrooge got you!!"