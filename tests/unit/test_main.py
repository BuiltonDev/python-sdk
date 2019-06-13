import pytest

from builton_sdk import Builton
from builton_sdk.api_models import *
from builton_sdk.main import DEFAULT_ENDPOINT
from builton_sdk.utils.request import Request


def test_init_sets_parameters():
    k = Builton("api_key", "bearer_token", endpoint="endpoint")
    assert k.api_key == "api_key"
    assert k.bearer_token == "bearer_token"
    assert k.endpoint == "endpoint"
    assert isinstance(k.request, Request)
    assert k.request.endpoint == "endpoint"


def test_init_sets_parameters_default_environment():
    k = Builton(api_key="api_key", bearer_token="bearer_token")
    assert k.api_key == "api_key"
    assert k.bearer_token == "bearer_token"
    assert k.endpoint == DEFAULT_ENDPOINT
    assert isinstance(k.request, Request)
    assert k.request.endpoint == DEFAULT_ENDPOINT


def test_none_endpoint_raises_exception():
    with pytest.raises(ValueError):
        Builton.validate_input(None, "api_key", "bearer_token")


def test_non_string_endpoint_raises_exception():
    with pytest.raises(ValueError):
        Builton.validate_input(42, "api_key", "bearer_token")


def test_none_api_key_raises_exception():
    with pytest.raises(ValueError):
        Builton.validate_input("endpoint", None, "bearer_token")


def test_non_string_api_key_raises_exception():
    with pytest.raises(ValueError):
        Builton.validate_input("endpoint", 42, "bearer_token")


def test_non_string_bearer_token_raises_exception():
    with pytest.raises(ValueError):
        Builton.validate_input("endpoint", "api_key", 42)


# validate_input
def test_instantiating_calls_validate_input(mocker):
    mocker.patch.object(Builton, 'validate_input')
    k = Builton("api_key", "bearer_token", "endpoint")
    k.validate_input.assert_called_once_with("endpoint",
                                             "api_key",
                                             "bearer_token")


def test_instantiating_calls_construct_headers(mocker):
    mocker.patch.object(Builton, '_construct_headers')
    k = Builton("endpoint", "api_key")
    k._construct_headers.assert_called_once


# refresh_bearer_token
def test_refresh_bearer_token():
    k = Builton("api_key", "bearer_token", endpoint="endpoint")
    assert k.bearer_token == "bearer_token"
    k.refresh_bearer_token("new_bearer")
    assert k.bearer_token == "new_bearer"


def test_refresh_bear_token_calls_construct_headers(mocker):
    k = Builton("api_key", "bearer_token", endpoint="endpoint")
    mocker.patch.object(Builton, '_construct_headers')
    k.refresh_bearer_token("new_barer_token")
    k._construct_headers.assert_called_once


# _construct_headers
def test_construct_headers_adds_api_key():
    k = Builton("api_key", "bearer_token", endpoint="endpoint")
    headers = k._construct_headers()
    assert 'X-Builton-API-Key' in headers
    assert headers['X-Builton-API-Key'] == "api_key"


def test_bearer_is_added_if_missing_when_constructing_headers():
    k = Builton("endpoint", "api_key", "foo")
    headers = k._construct_headers()
    assert headers['Authorization'].startswith("Bearer ")


def test_methods_return_right_instances():
    k = Builton("endpoint", "api_key", "bearer_token")
    assert isinstance(k.ai_model(), AIModel)
    assert isinstance(k.company(), Company)
    assert isinstance(k.event(), Event)
    assert isinstance(k.order(), Order)
    assert isinstance(k.payment(), Payment)
    assert isinstance(k.payment_method(), PaymentMethod)
    assert isinstance(k.plan(), Plan)
    assert isinstance(k.product(), Product)
    assert isinstance(k.provider(), Provider)
    assert isinstance(k.resource(), Resource)
    assert isinstance(k.subscription(), Subscription)
    assert isinstance(k.tag(), Tag)
    assert isinstance(k.user(), User)
    assert isinstance(k.webhook(), Webhook)
