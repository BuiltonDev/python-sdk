import pytest

from src.main import Kvass
from src.collection.ai_model import AIModel
from src.collection.company import Company
from src.collection.event import Event
from src.collection.order import Order
from src.collection.payment import Payment
from src.collection.payment_method import PaymentMethod
from src.collection.plan import Plan
from src.collection.product import Product
from src.collection.provider import Provider
from src.collection.resource import Resource
from src.collection.subscription import Subscription
from src.collection.tag import Tag
from src.collection.user import User
from src.collection.webhook import Webhook
from src.utils.request import Request


#__init__
def test_init_sets_parameters():
    k = Kvass("endpoint", "api_key", "bearer_token")
    assert k.api_key == "api_key"
    assert k.bearer_token == "bearer_token"
    assert k.endpoint == "endpoint"
    assert isinstance(k.request, Request)
    assert k.request.endpoint == "endpoint"


def test_none_endpoint_raises_exception():
    with pytest.raises(ValueError):
        Kvass.validate_input(None, "api_key", "bearer_token")


def test_non_string_endpoint_raises_exception():
    with pytest.raises(ValueError):
        Kvass.validate_input(42, "api_key", "bearer_token")


def test_none_api_key_raises_exception():
    with pytest.raises(ValueError):
        Kvass.validate_input("endpoint", None, "bearer_token")


def test_non_string_api_key_raises_exception():
    with pytest.raises(ValueError):
        Kvass.validate_input("endpoint", 42, "bearer_token")


def test_non_string_bearer_token_raises_exception():
    with pytest.raises(ValueError):
        Kvass.validate_input("endpoint", "api_key", 42)


# validate_input
def test_instantiating_calls_validate_input(mocker):
    mocker.patch.object(Kvass, 'validate_input')
    k = Kvass("endpoint", "api_key", "bearer_token")
    k.validate_input.assert_called_once_with("endpoint",
                                             "api_key",
                                             "bearer_token")


def test_instantiating_calls_construct_headers(mocker):
    mocker.patch.object(Kvass, '_construct_headers')
    k = Kvass("endpoint", "api_key")
    k._construct_headers.assert_called_once


# refresh_bearer_token
def test_refresh_bearer_token():
    k = Kvass("endpoint", "api_key", "bearer_token")
    assert k.bearer_token == "bearer_token"
    k.refresh_bearer_token("new_bearer")
    assert k.bearer_token == "new_bearer"


def test_refresh_bear_token_calls_construct_headers(mocker):
    k = Kvass("endpoint", "api_key", "bearer_token")
    mocker.patch.object(Kvass, '_construct_headers')
    k.refresh_bearer_token("new_barer_token")
    k._construct_headers.assert_called_once


# _construct_headers
def test_construct_headers_adds_api_key():
    k = Kvass("endpoint", "api_key", "bearer_token")
    headers = k._construct_headers()
    assert 'X-Kvass-API-Key' in headers
    assert headers['X-Kvass-API-Key'] == "api_key"


def test_bearer_is_added_if_missing_when_constructing_headers():
    k = Kvass("endpoint", "api_key", "foo")
    headers = k._construct_headers()
    assert headers['Authorization'].startswith("Bearer ")

#
def test_methods_return_right_instances():
    k = Kvass("endpoint", "api_key", "bearer_token")
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
