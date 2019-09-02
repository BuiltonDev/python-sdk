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


def test_get_users(builton):
    users = builton.user().get_all(page=0, size=2)
    first_user = users[0]
    second_user = users[1]
    assert first_user.id != second_user.id


def test_get_user_orders(builton):
    users = builton.user().get_all(page=0, sort="-created")

    assert sorted(users,
                  key=lambda user: user.created['$date'],
                  reverse=True) == users

    for user in users:
        orders = user.get_orders()
        for order in orders:
            assert order.id is not None
            assert order.user["$oid"] == user.id


def test_get_users_params_instead_of_dict(builton):
    users = builton.user().get_all(size=1)
    assert isinstance(users, list)
    assert 1 == len(users)


def test_get_user_by_id(builton):
    users = builton.user().get_all(size=1)
    user_id = users[0].id

    user = builton.user().get(user_id)
    assert isinstance(user, User)
    assert user.id == user_id

    new_user = builton.user().get(id=user_id)
    assert isinstance(new_user, User)
    assert new_user.id == user.id == user_id

