import time

from scrooge.client import Client
from scrooge.cache import RedisCache

redis_client = RedisCache(host='127.0.0.1', port=6379)

client = Client(cache_client=redis_client)


class Test:
    pass


@client.gentlemen_cache(namespace='delay_5', expiration_time=2)
def dict_delay(delay_time=5, delay_time_=2):
    time.sleep(delay_time + delay_time_)
    print("Delay finished")
    return {delay_time: delay_time_}


@client.gentlemen_cache(namespace='obj_delay', expiration_time=2)
def obj_delay(delay_time=5):
    return Test()


@client.gentlemen_cache(namespace='str_delay', expiration_time=2)
def str_delay(delay_time=1):
    return 'foo-bar'


@client.gentlemen_cache(namespace='int_delay', expiration_time=2)
def int_delay(delay_time=2):
    return 9


@client.gentlemen_cache(namespace='float_delay', expiration_time=2)
def float_delay(delay_time=3):
    return 1.4


@client.gentlemen_cache(namespace='list_delay', expiration_time=2)
def list_delay(delay_time=4):
    return ['foo', 'bar']


@client.gentlemen_cache(namespace='tuple_delay', expiration_time=2)
def tuple_delay(delay_time=5):
    return (1, 2)
