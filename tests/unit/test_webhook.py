from builton_sdk.api_models import Webhook


def test_rest_decorators():
    webhook = Webhook("request", "props")
    methods = ['create', 'delete', 'get', 'get_all', 'refresh', 'update']
    for m in methods: assert hasattr(webhook, m)


def test_init_sets_api_path():
    webhook = Webhook("request", "props")
    assert webhook.api_path == "webhooks"
