from cachetools import TTLCache

REQUEST_TIMEOUT = 10

CACHE_TTL = 300

CACHE = TTLCache(
    maxsize=100,
    ttl=CACHE_TTL
)

APP_NAME = "Page Pulse"

APP_VERSION = "1.0.0"