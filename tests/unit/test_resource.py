from builton_sdk.api_models import Resource


def test_rest_decorators():
    resource = Resource("request", "props")
    methods = ['create', 'delete', 'get', 'get_all',
               'refresh', 'update', 'search']
    for m in methods: assert hasattr(resource, m)


def test_init_sets_api_path():
    resource = Resource("request", "props")
    assert resource.api_path == "resources"
