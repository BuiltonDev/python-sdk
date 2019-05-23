import pytest

from src.main import Kvass
from src.collection.user import User
from tests.integration.config_example import ENDPOINT, API_KEY, BEARER_TOKEN


@pytest.fixture
def kvass():
    return Kvass(endpoint=ENDPOINT,
                 api_key=API_KEY,
                 bearer_token=BEARER_TOKEN)


def test_get_users_has_attributes_with_right_types(kvass):
    users = kvass.user().get_all()

    assert isinstance(users, list)

    for user in users:
        assert isinstance(user, User)
        assert isinstance(user.id, str)
        assert isinstance(user.first_name, str)
        assert isinstance(user.last_name, str)
        if hasattr(user, "email"):
            assert isinstance(user.email, str)
        assert isinstance(user.roles, list)
        if hasattr(user, "mobile_phone_number"):
            assert isinstance(user.mobile_phone_number, str)
        assert isinstance(user.addresses, list)
        assert isinstance(user.bio, str)
        assert isinstance(user.tags, list)
