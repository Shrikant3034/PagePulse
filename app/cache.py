from app.config import CACHE

def get_cached(url: str):
    return CACHE.get(url)

def set_cache(url: str, data):
    CACHE[url] = data