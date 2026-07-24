import validators

def validate_url(url: str):

    if not validators.url(url):
        raise ValueError("Invalid URL")

    return True