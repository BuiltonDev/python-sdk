import pytest

from src.collection.components import Components


# __init__
def test_cannot_construct_abstract_instances():
    with pytest.raises(Exception):
        Components(None, None)


def test_init_sets_parameters():
    class Comp(Components):
        pass

    comp = Comp("request", None)
    assert comp.identifier == None
    assert comp.request == "request"
    assert comp.id == None
    assert comp.api_path == None


def test_string_props_turns_into_id():
    class Comp(Components):
        pass

    comp = Comp(None, "props")
    assert comp.id == "props"


def test_dict_props_calls_build_instance(mocker):
    class Comp(Components):
        pass
    mocker.patch.object(Components, 'build_instance')
    props = {'foo' : 'bar'}
    Comp(None, props)
    Components.build_instance.assert_called_once_with(props)


# build_instance
def test_dict_props_turns_into_instance_props():
    class Comp(Components):
        pass
    props = {'foo' : 'bar', 'monty' : 42}
    comp = Comp(None, props)
    assert comp.foo == 'bar'
    assert comp.monty == 42


def test_id_oid_from_props_turns_into_instance_prop():
    class Comp(Components):
        pass

    props = {'_id' : {'$oid' : 42}}
    comp = Comp(None, props)
    assert comp.id == 42


# simple_query
def test_simple_query_without_id_raises_exception():
    class Comp(Components):
        pass

    comp = Comp(None, None)
    with pytest.raises(ValueError):
        comp.simple_query(_id=None)




