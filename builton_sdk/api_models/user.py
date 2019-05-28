from builton_sdk.api_models.component import Component
from builton_sdk.api_models.order import Order
from builton_sdk.api_models.subscription import Subscription
from builton_sdk.utils.rest_functions import *


@rest_decorator(get, delete, get_all, refresh, update, search)
class User(Component):
    def __init__(self, request, props):
        super(User, self).__init__(request, props)
        self.api_path = 'users'
        if self.id is None:
            self.id = 'me'

    def create(self, body, url_params=None, json=False):
        return self.simple_query(_type='post', api_path='v2/users', url_params=url_params,
                                 body=body, json=json)

    def login(self, body, url_params=None, json=False):
        return self.create(body=body, url_params=url_params, json=json)

    def get_orders(self, url_params=None, json=False):
        return self.simple_query(resource='orders', _id=self.id, url_params=url_params, json=json,
                                 res_constructor=Order)

    def get_rating(self, url_params=None):
        return self.simple_query(resource='ratings', _id=self.id, url_params=url_params, json=True)

    def rate(self, body, url_params=None):
        return self.simple_query(_type='put', _id=self.id, resource='ratings', body=body,
                                 url_params=url_params,
                                 json=True)

    def update_addresses(self, body, url_params=None):
        return self.simple_query(_type='put', _id=self.id, resource='addresses', body=body,
                                 url_params=url_params,
                                 json=True)

    def get_subscriptions(self, body, url_params=None):
        return self.simple_query(_type='put', _id=self.id, resource='subscriptions', body=body,
                                 url_params=url_params,
                                 res_constructor=Subscription)
