from builton_sdk.api_models._component import _Component
from builton_sdk.api_models.order import Order
from builton_sdk.api_models.subscription import Subscription
from builton_sdk.utils.rest_functions import *


@rest_decorator(get, delete, get_all, refresh, update, search)
class User(_Component):
    def __init__(self, request, props):
        super(User, self).__init__(request, props)
        self.api_path = 'users'

    def authenticate(self, *args, **kwargs):
        return self.create(*args, **kwargs)

    def create(self, *args, **kwargs):
        return self._simple_query(*args, _type='post', api_path='v2/users', **kwargs)

    def get_orders(self, url_params=None, json=False):
        return self._simple_query(resource='orders', _id=self.id, url_params=url_params, json=json,
                                  res_constructor=Order)

    def update_addresses(self, body, url_params=None):
        return self._simple_query(_type='put', _id=self.id, resource='addresses', body=body,
                                  url_params=url_params, json=True)

    def get_subscriptions(self, url_params=None, json=False):
        return self._simple_query(_type='get', _id=self.id, resource='subscriptions',
                                  url_params=url_params, res_constructor=Subscription,
                                  json=json)
