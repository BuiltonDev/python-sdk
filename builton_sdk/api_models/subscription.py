from builton_sdk.api_models.component import Component
from builton_sdk.utils.rest_functions import *


@rest_decorator(create, delete, get, get_all, refresh, update, search)
class Subscription(Component):
    def __init__(self, request, props):
        super(Subscription, self).__init__(request, props)
        self.api_path = 'subscriptions'

    def start(self, body, url_params=None, json=False):
        return self.simple_query(_type='post', _id=self.id, resource='start', url_params=url_params,
                                 body=body,
                                 json=json)

    def stop(self, body, url_params=None, json=False):
        return self.simple_query(_type='post', _id=self.id, resource='stop', url_params=url_params,
                                 body=body,
                                 json=json)
