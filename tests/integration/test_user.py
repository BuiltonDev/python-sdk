from builton_sdk.api_models import User


def test_get_users_has_attributes_with_right_types(builton):
    users = builton.user().get_all()

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
