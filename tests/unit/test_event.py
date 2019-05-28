from builton_sdk.api_models import Event


def test_rest_decorators():
    event = Event("request", "props")
    methods = ['get', 'get_all', 'refresh', 'search']
    for m in methods: assert hasattr(event, m)


def test_init_sets_api_path():
    event = Event("request", "props")
    assert event.api_path == "events"
