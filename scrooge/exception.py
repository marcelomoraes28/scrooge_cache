class ScroogeException(Exception):
    """
    This exception is used only in base classes
    """
    pass


class ScroogeClientException(Exception):
    """
    This exceptions is used only in Client module
    """
    pass


class ScroogeRedisCacheException(Exception):
    """
    This exceptions is used only in Redis Client
    """
    pass


class ScroogeMemcacheCacheException(Exception):
    """
    This exceptions is used only in Memcache Client
    """
    pass
