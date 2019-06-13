from builton_sdk.api_models import AIModel


def test_rest_decorators():
    ai = AIModel("request", "props")
    methods = ['create', 'get', 'get_all', 'search']
    for m in methods: assert hasattr(ai, m)


def test_init_sets_api_path():
    ai = AIModel("request", "props")
    assert ai.api_path == "ai/models"
