import requests

from builton_sdk.utils.request import Request


def test_init_sets_endpoint_and_headers():
    r = Request(endpoint="endpoint", headers="headers")
    assert r.endpoint == "endpoint"
    assert r.headers == "headers"


def test_update_headers():
    r = Request("endpoint", "headers")
    r.update_headers("bar")
    assert r.headers == "bar"


def test_query_with_no_arguments(mocker):
    r = Request(endpoint="endpoint", headers="headers")
    mocker.patch.object(requests, 'request')
    r.query()
    requests.request.assert_called_once_with('get', 'endpoint', headers='headers',
                                             json=None, params=None, verify=True)


def test_query_with_headers(mocker):
    r = Request(endpoint="endpoint", headers={'foo': 'bar'})
    mocker.patch.object(requests, 'request')
    r.query(headers={'monty': 'python'})
    requests.request.assert_called_once_with('get', 'endpoint',
                                             headers={'foo': 'bar', 'monty': 'python'},
                                             json=None, params=None, verify=True)


def test_query_builds_query_url(mocker):
    r = Request(endpoint="http://example.com", headers={})
    mocker.patch.object(requests, 'request')
    r.query(resource="/resource")
    requests.request.assert_called_once_with('get', 'http://example.com/resource', headers={},
                                             json=None, params=None, verify=True)


def test_build_query_url():
    url = "https://qa.builton.dev"
    resource = "users"
    expected_url = "%s/%s" % (url, resource)

    request = Request(endpoint=url, headers={})
    query_url = request._build_query_url(resource)
    assert expected_url == query_url

    url = "https://qa.builton.dev///"
    request = Request(endpoint=url, headers={})
    query_url = request._build_query_url(resource)
    assert expected_url == query_url
