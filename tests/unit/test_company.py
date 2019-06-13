from builton_sdk.api_models import Company


def test_rest_decorators():
    company = Company("request", "props")
    assert hasattr(company, "get")
    assert hasattr(company, "refresh")


def test_init_sets_api_path():
    company = Company("request", "props")
    assert company.api_path == "companies"
