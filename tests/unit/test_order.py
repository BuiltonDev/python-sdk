from builton_sdk.api_models import Order


def test_rest_decorators():
    order = Order("request", "props")
    methods = ['create', 'delete', 'get', 'get_all', 'refresh', 'update']
    for m in methods: assert hasattr(order, m)


def test_init_sets_api_path():
    order = Order("request", "props")
    assert order.api_path == "orders"
