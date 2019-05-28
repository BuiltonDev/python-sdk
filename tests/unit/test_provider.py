from builton_sdk.api_models import Provider


def test_init_sets_api_path():
    provider = Provider("request", "props")
    assert provider.api_path == "providers"
