from builton_sdk.api_models import Product


def test_rest_decorators():
    product = Product("request", "props")
    methods = ['create', 'delete', 'get', 'get_all',
               'refresh', 'update', 'search']
    for m in methods: assert hasattr(product, m)


def test_init_sets_api_path():
    product = Product("request", "props")
    assert product.api_path == "products"
