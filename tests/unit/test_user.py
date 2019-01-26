from src.collection.user import User


def test_rest_decorators():
    user = User("request", "props")
    methods = ['create', 'delete', 'get', 'get_all',
               'refresh', 'update', 'search']
    for m in methods: assert hasattr(user, m)


def test_init_sets_api_path():
    user = User("request", "props")
    assert user.api_path == "users"