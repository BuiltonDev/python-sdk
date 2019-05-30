import logging
from urllib.parse import urljoin

import requests

logger = logging.getLogger(__name__)


class Request:
    def __init__(self, endpoint, headers):
        self.endpoint = endpoint
        self.headers = headers

    def update_headers(self, headers):
        self.headers = headers

    def _build_query_url(self, resource):
        return urljoin(self.endpoint, resource)

    def query(self, _type='get', resource='', url_params=None, body=None, headers=None):
        query_url = self._build_query_url(resource)
        query_headers = self.headers

        if headers:
            query_headers.update(headers)

        logger.debug("query_url: %s" % query_url)
        logger.debug("headers: %s" % query_headers)
        logger.debug("url_params: %s" % url_params)
        logger.debug("body: %s" % body)

        return requests.request(_type, query_url, params=url_params, json=body,
                                headers=query_headers, verify=True)
