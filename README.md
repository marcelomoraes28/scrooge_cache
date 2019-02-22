
Scrooge Cache
=======================================

[![Build Status](https://travis-ci.org/marcelomoraes28/scrooge_cache.svg?branch=master)](https://travis-ci.org/marcelomoraes28/scrooge_cache)
[![Coverage Status](https://coveralls.io/repos/github/marcelomoraes28/scrooge_cache/badge.svg?branch=master)](https://coveralls.io/github/marcelomoraes28/scrooge_cache?branch=master)
[![Pypi Version](https://img.shields.io/badge/pypi-0.0.1-yellow.svg)](https://img.shields.io/badge/pypi-0.0.1--alpha-yellow.svg)
[![Python Version](https://img.shields.io/badge/python-3.6%7C3.7-blue.svg)](https://img.shields.io/badge/python-3.6%7C3.7-blue.svg)

![alt text](scrooge_mcduck.png)

What is Scrooge?
----------------------------------
Scrooge is smart cache storage for stronger gentlemen
Scrooge is a **S**mart **C**ache Sto**r**age f**o**r str**o**nger **g**entlem**e**n

**Backend supports:**
- [memcache](https://memcached.org/)
- [redis](https://redis.io/)


How can I use?
-------------

Scrooge is able to cache function returns for a given or infinite period.

**Rules:**
- Just a unique namespace per backend instance;
- If you do not set expiration_time scrooge it'll take infinite time;
- The return of decorated function must be str or int or float or tuple, or list or dict;
- If you use redis backend you can defined the db index using the parameter **db=index**, if you do not do this the default will be 0;

Installing
-------------
```
pip install scrooge-cache
```
Quick start
-----------

**Using with redis as backend**

This example below will cache the function return for the infinite time

```python
import time
from scrooge import RedisBackend, Client

backend = RedisBackend(host='127.0.0.1', port=6379)
client = Client(cache_backend=backend)

# Cached for infinite time
@client.gentlemen_cache(namespace='f1')
def function_to_be_cached(p1, p2):
    time.sleep(5)
    return {"p1": p1, "p2": p2}

# After 5 seconds the return will be {"p1": 4, "p2": 5}
print(function_to_be_cached(4,5))

# The return will be {"p1": 4, "p2": 5}
print(function_to_be_cached(4,5))
```

This example below will cache the function return for 10 seconds

```python
import time
from scrooge import RedisBackend, Client

backend = RedisBackend(host='127.0.0.1', port=6379)
client = Client(cache_backend=backend)

# Cached for infinite time
@client.gentlemen_cache(namespace='f1', expiration_time=10)
def function_to_be_cached(p1, p2):
    time.sleep(5)
    return {"p1": p1, "p2": p2}

# After 5 seconds the return will be {"p1": 4, "p2": 5}
print(function_to_be_cached(4,5))

# The return will be {"p1": 4, "p2": 5}
print(function_to_be_cached(4,5))

time.sleep(5)

# After 5 seconds the return will be {"p1": 4, "p2": 5}
print(function_to_be_cached(4,5))
```

**Using with memcache as backend**

This example below will cache the function return for the infinite time

```python
import time
from scrooge import MemcacheBackend, Client

backend = MemcacheBackend(host='127.0.0.1', port=6379)
client = Client(cache_backend=backend)

# Cached for infinite time
@client.gentlemen_cache(namespace='f1')
def function_to_be_cached(p1, p2):
    time.sleep(5)
    return {"p1": p1, "p2": p2}

# After 5 seconds the return will be {"p1": 4, "p2": 5}
print(function_to_be_cached(4,5))

# The return will be {"p1": 4, "p2": 5}
print(function_to_be_cached(4,5))
```

This example below will cache the function return for 10 seconds

```python
import time
from scrooge import MemcacheBackend, Client

backend = MemcacheBackend(host='127.0.0.1', port=6379)
client = Client(cache_backend=backend)

# Cached for infinite time
@client.gentlemen_cache(namespace='f1', expiration_time=10)
def function_to_be_cached(p1, p2):
    time.sleep(5)
    return {"p1": p1, "p2": p2}

# After 5 seconds the return will be {"p1": 4, "p2": 5}
print(function_to_be_cached(4,5))

# The return will be {"p1": 4, "p2": 5}
print(function_to_be_cached(4,5))

time.sleep(5)

# After 5 seconds the return will be {"p1": 4, "p2": 5}
print(function_to_be_cached(4,5))
```

Run tests
------------
```
pytest -ra
```
