import time
import requests

from bs4 import BeautifulSoup

from app.logger import logger
from app.config import REQUEST_TIMEOUT

from app.cache import get_cached, set_cache
from app.utils import validate_url

from app.exceptions import AuditException


def audit_url(url: str):

    validate_url(url)

    cached = get_cached(url)

    if cached:

        logger.info("Returning cached response")

        cached["cached"] = True

        return cached

    try:

        logger.info(f"Auditing {url}")

        start = time.time()

        response = requests.get(
            url,
            timeout=REQUEST_TIMEOUT,
            headers={
                "User-Agent": "PagePulse/1.0"
            }
        )

        elapsed = round((time.time() - start) * 1000, 2)

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        title = soup.title.string.strip() if soup.title else "No Title"

        result = {

            "url": url,

            "status_code": response.status_code,

            "response_time_ms": elapsed,

            "https": url.startswith("https"),

            "title": title,

            "server": response.headers.get(
                "Server",
                "Unknown"
            ),

            "content_length": len(response.content),

            "cached": False

        }

        set_cache(url, result)

        logger.info("Audit completed")

        return result

    except Exception as e:

        logger.error(str(e))

        raise AuditException(str(e))