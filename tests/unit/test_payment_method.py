from builton_sdk.api_models import PaymentMethod


def test_rest_decorators():
    pay_method = PaymentMethod("request", "props")
    methods = ['create', 'delete', 'get', 'get_all', 'refresh', 'update']
    for m in methods: assert hasattr(pay_method, m)


def test_init_sets_api_path():
    pay_method = PaymentMethod("request", "props")
    assert pay_method.api_path == "payment_methods"
