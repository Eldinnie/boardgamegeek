import pytest
from requests_cache import CachedSession

from boardgamegeek.cache import CacheBackendMemory, CacheBackendSqlite
from boardgamegeek.exceptions import BGGValueError


def test_memory_cache_creation_error():
    with pytest.raises(BGGValueError):
        CacheBackendMemory("NaN")


def test_sql_cache_creation_error():
    with pytest.raises(BGGValueError):
        CacheBackendSqlite(path="NULL", ttl="NaN")


def test_sql_cache_creation():
    cache = CacheBackendSqlite(path="NULL", ttl=3600)
    assert type(cache.cache) is CachedSession
    assert cache.cache.settings.expire_after == 3600
