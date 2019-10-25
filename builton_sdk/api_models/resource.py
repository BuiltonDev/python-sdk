from builton_sdk.api_models._component import _Component
from builton_sdk.utils.rest_functions import *
from builton_sdk.api_models.order import Order


@rest_decorator(create, delete, get, get_all, refresh, update, search)
class Resource(_Component):
    def __init__(self, request, props):
        super(Resource, self).__init__(request, props)
        self.api_path = 'resources'

    def create_bulk(self, body, url_params=None, json=False):
        return self._simple_query(_type='post', resource='bulk', body=body, url_params=url_params,
                                  json=json)

    def update_bulk(self, body, url_params=None, json=False):
        return self._simple_query(_type='put', resource='bulk', body=body, url_params=url_params,
                                 json=json)

    def get_orders(self, body, url_params=None, json=False):
        return self._simple_query(_id=self.id, resource='orders', body=body, url_params=url_params,
                                 json=json, res_constructor=Order)
