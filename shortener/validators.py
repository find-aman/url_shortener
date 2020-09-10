from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

url_endings = [
    ".org",
    ".com",
    ".in",
    ".gov",
    ".io",
    ".net",
    ".to",
    ".edu",
    ".co",
    ".info",
    ".uk",
]


def validate_url_endings(value):
    url_validator = URLValidator()

    for url_ending in url_endings:
        if url_ending in value:
            return value

    raise ValidationError("Not a valid URL ending")


def validate_url_starting(value):
    url_validator = URLValidator()

    for url_starting in ["http://", "https://", "www."]:
        if url_starting in value:
            return value

    raise ValidationError("Not a valid URL startnig")
