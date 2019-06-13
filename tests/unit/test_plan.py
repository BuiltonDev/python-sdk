from builton_sdk.api_models import Plan


def test_rest_decorators():
    plan = Plan("request", "props")
    methods = ['create', 'delete', 'get', 'get_all',
               'refresh', 'update', 'search']
    for m in methods: assert hasattr(plan, m)


def test_init_sets_api_path():
    plan = Plan("request", "props")
    assert plan.api_path == "plans"
