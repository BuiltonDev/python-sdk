import pytest

from src.collection.components import Components


class Component(Components): pass


# __init__
def test_cannot_construct_abstract_instances():
    with pytest.raises(Exception):
        Components(None, None)


def test_init_sets_parameters():
    component = Component("request", None)
    assert component.identifier == None
    assert component.request == "request"
    assert component.id == None
    assert component.api_path == None


def test_string_props_turns_into_id():
    component = Component(None, "props")
    assert component.id == "props"


def test_dict_props_calls_build_instance(mocker):
    mocker.patch.object(Components, 'build_instance')
    props = {'foo' : 'bar'}
    Component(None, props)
    Components.build_instance.assert_called_once_with(props)


# build_instance
def test_dict_props_turns_into_instance_props():
    props = {'foo' : 'bar', 'monty' : 42}
    component = Component(None, props)
    assert component.foo == 'bar'
    assert component.monty == 42


def test_id_oid_from_props_turns_into_instance_prop():
    props = {'_id' : {'$oid' : 42}}
    component = Component(None, props)
    assert component.id == 42


# simple_query
def test_simple_query_without_id_raises_exception():
    component = Component(None, None)
    with pytest.raises(ValueError):
        component.simple_query(_id=None)

