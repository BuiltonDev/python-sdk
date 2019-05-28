from builton_sdk.api_models import Tag


def test_rest_decorators():
    tag = Tag("request", "props")
    methods = ['create', 'delete', 'get', 'get_all',
               'refresh', 'update', 'search']
    for m in methods: assert hasattr(tag, m)


def test_init_sets_api_path():
    tag = Tag("request", "props")
    assert tag.api_path == "tags"
