from builton_sdk.api_models import Payment


def test_rest_decorators():
    payment = Payment("request", "props")
    methods = ['create', 'delete', 'get', 'get_all',
               'refresh', 'update', 'search']
    for m in methods: assert hasattr(payment, m)


def test_init_sets_api_path():
    payment = Payment("request", "props")
    assert payment.api_path == "payments"
