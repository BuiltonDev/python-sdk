from builton_sdk.api_models._component import _Component
from builton_sdk.api_models.payment import Payment
from builton_sdk.utils.rest_functions import *


@rest_decorator(get, create, get_all, refresh, update, search)
class Order(_Component):
    def __init__(self, request, props):
        super(Order, self).__init__(request, props)
        self.api_path = 'orders'

    def pay(self, body, url_params=None, json=False):
        return self._simple_query(_type='post', _id=self.id, resource='pay', body=body,
                                  url_params=url_params,
                                  json=json)

    def cancel(self, body, url_params=None, json=False):
        return self._simple_query(_type='post', _id=self.id, resource='cancel', body=body,
                                  url_params=url_params,
                                  json=json)

    def get_payments(self, url_params=None, json=False):
        return self._simple_query(_id=self.id, resource='payments', url_params=url_params,
                                  json=json, res_constructor=Payment)
