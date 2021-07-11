from .tags import Tags
from .categories import Categories
import os
import requests

# TODO maybe only for testing needed
# LUNCHMONEY_API_KEY = os.environ.get('LUNCHMONEY_API_KEY', None)
from dotenv import load_dotenv
load_dotenv()
LUNCHMONEY_API_KEY = os.getenv('LUNCHMONEY_API_KEY')


class APIKeyMissingError(Exception):
    pass


if LUNCHMONEY_API_KEY is None:
    raise APIKeyMissingError(
        'All functionality require an API key. Visit "https://my.lunchmoney.app/developers" to get one.'
    )

session = requests.Session()
session.params = {}
session.params['access_token'] = LUNCHMONEY_API_KEY
