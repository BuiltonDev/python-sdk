import pytest

from builton_sdk import Builton
from config import ENDPOINT, API_KEY, BEARER_TOKEN


@pytest.fixture
def builton():
    return Builton(endpoint=ENDPOINT,
                   api_key=API_KEY,
                   bearer_token=BEARER_TOKEN)
