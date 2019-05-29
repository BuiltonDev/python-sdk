import pytest

from builton_sdk import Builton
from config import API_KEY, BEARER_TOKEN, TALKBACK_ENDPOINT


@pytest.fixture
def builton():
    return Builton(endpoint=TALKBACK_ENDPOINT,
                   api_key=API_KEY,
                   bearer_token=BEARER_TOKEN)
