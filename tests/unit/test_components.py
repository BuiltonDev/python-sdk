import pytest

from builton_sdk.api_models.component import Component


class RandomComponent(Component):
    pass


# __init__
def test_cannot_construct_abstract_instances():
    with pytest.raises(Exception):
        Component(None, None)


def test_init_sets_parameters():
    component = RandomComponent("request", {})
    assert component.identifier is None
    assert component.request == "request"
    assert component.id is None
    assert component.api_path is None


def test_string_props_turns_into_id():
    component = RandomComponent(None, "props")
    assert component.id == "props"


def test_dict_props_calls_build_instance(mocker):
    mocker.patch.object(Component, 'build_instance')
    props = {'foo': 'bar'}
    RandomComponent(None, props)
    Component.build_instance.assert_called_once_with(props)


def test_invalid_props_type_raises_exception():
    with pytest.raises(ValueError):
        RandomComponent("request", 42)


# build_instance
def test_dict_props_turns_into_instance_props():
    props = {'foo': 'bar', 'monty': 42}
    component = RandomComponent(None, props)
    assert component.foo == 'bar'
    assert component.monty == 42


def test_id_oid_from_props_turns_into_instance_id():
    props = {'_id': {'$oid': 42}}
    component = RandomComponent(None, props)
    assert component.id == 42


# simple_query
def test_simple_query_without_id_raises_exception():
    component = RandomComponent(None, None)
    with pytest.raises(ValueError):
        component.simple_query(_id=None)


def test_build_resource():
    user = RandomComponent("request")
    user.api_path = "users"
    assert user.api_path == "users"
    assert "users" == user.build_resource("", "")
    assert "users/1" == user.build_resource("1", "")
    assert "users/1/payments" == user.build_resource("1", "payments")
