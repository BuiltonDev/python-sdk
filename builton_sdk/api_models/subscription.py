from builton_sdk.api_models._component import _Component
from builton_sdk.api_models.payment import Payment
from builton_sdk.utils.rest_functions import *


@rest_decorator(create, delete, get, get_all, refresh, update, search)
class Subscription(_Component):
    def __init__(self, request, props):
        super(Subscription, self).__init__(request, props)
        self.api_path = 'subscriptions'

    def start(self, body, url_params=None, json=False):
        return self._simple_query(_type='post', _id=self.id, resource='start', url_params=url_params,
                                 body=body, json=json)

    def stop(self, body=None, url_params=None, json=False):
        return self._simple_query(_type='post', _id=self.id, resource='stop', url_params=url_params,
                                 body=body, json=json)

    def get_payments(self, url_params=None, json=False):
        return self._simple_query(_id=self.id, resource='payments', url_params=url_params,
                                 json=json, res_constructor=Payment)
