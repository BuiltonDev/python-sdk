import pytest
import json

from builton_sdk.api_models import *

ignore_functions = [
    '_Component__extract_id',
    '__class__',
    '__delattr__',
    '__dict__',
    '__dir__',
    '__doc__',
    '__eq__',
    '__format__',
    '__ge__',
    '__getattribute__',
    '__gt__',
    '__hash__',
    '__init__',
    '__init_subclass__',
    '__le__',
    '__lt__',
    '__module__',
    '__ne__',
    '__new__',
    '__reduce__',
    '__reduce_ex__',
    '__repr__',
    '__setattr__',
    '__sizeof__',
    '__str__',
    '__subclasshook__',
    '__weakref__',

    '_build_url_params',
    '_extract_expand',
    '_extract_id',
    '_build_instance',
    '_build_resource',
    '_handle_error',
    '_parse_json',
    '_simple_get_query',
    '_simple_query'
    ]

def test_architecture():
    check_architecture_for_model(AIModel)
    check_architecture_for_model(Company)
    check_architecture_for_model(Event)
    check_architecture_for_model(Order)
    check_architecture_for_model(PaymentMethod)
    check_architecture_for_model(Payment)
    check_architecture_for_model(Plan)
    check_architecture_for_model(Product)
    check_architecture_for_model(Resource)
    check_architecture_for_model(Subscription)
    check_architecture_for_model(User)
    check_architecture_for_model(Webhook)

def get_functions_of(obj):
    functions = []
    for fn in dir(obj):
        if fn not in ignore_functions:
            functions.append(fn)
    functions.sort()
    return functions

def get_expected_functions_of(obj):
    function_name = obj.__name__
    with open('./tests/architecture/architecture.json', 'r') as f:
        functionArchitecture = json.load(f)[function_name]
        expected_functions = functionArchitecture['object']['roles']['admin'] + functionArchitecture['object']['roles']['user'] + functionArchitecture['resource']['roles']['admin'] + functionArchitecture['resource']['roles']['user']
        expected_functions.sort()
        return expected_functions

def check_architecture_for_model(obj):
    actual_functions = get_functions_of(obj)
    expected_functions = get_expected_functions_of(obj)
    assert(actual_functions==expected_functions)

