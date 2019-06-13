from builton_sdk.api_models import Subscription


def test_rest_decorators():
    subscription = Subscription("request", "props")
    methods = ['create', 'delete', 'get', 'get_all',
               'refresh', 'update', 'search']
    for m in methods: assert hasattr(subscription, m)


def test_init_sets_api_path():
    sub = Subscription("request", "props")
    assert sub.api_path == "subscriptions"
