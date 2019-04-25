import time

from scrooge import Client
from scrooge import RedisBackend, MemcacheBackend

redis_backend = RedisBackend(host='localhost', port=6379)
memcache_backend = MemcacheBackend(host='localhost', port=11211)

redis_client = Client(cache_backend=redis_backend)
memcache_client = Client(cache_backend=memcache_backend)


class Test:
    pass


@redis_client.gentlemen_cache(namespace='no_cache', expiration_time=10)
def r_no_cache(**kwargs):
    time.sleep(2)
    return "Scrooge got you!!"


@redis_client.gentlemen_cache(namespace='force_cache_update', expiration_time=10)
def force_cache_update(**kwargs):
    time.sleep(2)
    return "Scrooge got you!!"


@redis_client.gentlemen_cache(namespace='dict_delay', expiration_time=2)
def r_dict_delay(delay_time=5, delay_time_=2):
    time.sleep(delay_time + delay_time_)
    print("Delay finished")
    return {delay_time: delay_time_}


@redis_client.gentlemen_cache(namespace='obj_delay', expiration_time=2)
def r_obj_delay(delay_time=5):
    return Test()


@redis_client.gentlemen_cache(namespace='str_delay', expiration_time=2)
def r_str_delay(delay_time=1):
    return 'foo-bar'


@redis_client.gentlemen_cache(namespace='int_delay', expiration_time=2)
def r_int_delay(delay_time=2):
    return 9


@redis_client.gentlemen_cache(namespace='float_delay', expiration_time=2)
def r_float_delay(delay_time=3):
    return 1.4


@redis_client.gentlemen_cache(namespace='list_delay', expiration_time=2)
def r_list_delay(delay_time=4):
    return ['foo', 'bar']


@redis_client.gentlemen_cache(namespace='tuple_delay', expiration_time=2)
def r_tuple_delay(delay_time=5):
    return (1, 2)


@memcache_client.gentlemen_cache(namespace='dict_delay', expiration_time=2)
def m_dict_delay(delay_time=5, delay_time_=2):
    time.sleep(delay_time + delay_time_)
    print("Delay finished")
    return {delay_time: delay_time_}


@memcache_client.gentlemen_cache(namespace='obj_delay', expiration_time=2)
def m_obj_delay(delay_time=5):
    return Test()


@memcache_client.gentlemen_cache(namespace='str_delay', expiration_time=2)
def m_str_delay(delay_time=1):
    return 'foo-bar'


@memcache_client.gentlemen_cache(namespace='int_delay', expiration_time=2)
def m_int_delay(delay_time=2):
    return 9


@memcache_client.gentlemen_cache(namespace='float_delay', expiration_time=2)
def m_float_delay(delay_time=3):
    return 1.4


@memcache_client.gentlemen_cache(namespace='list_delay', expiration_time=2)
def m_list_delay(delay_time=4):
    return ['foo', 'bar']


@memcache_client.gentlemen_cache(namespace='tuple_delay', expiration_time=2)
def m_tuple_delay(delay_time=5):
    return (1, 2)


@memcache_client.gentlemen_cache(namespace='no_cache', expiration_time=10)
def m_no_cache(**kwargs):
    time.sleep(2)
    return "Scrooge got you!!"
