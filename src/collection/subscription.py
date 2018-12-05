from src.collection.components import Components
from src.utils.rest_functions import rest_decorator, create, delete, get, get_all, refresh, update, search


@rest_decorator(create, delete, get, get_all, refresh, update, search)
class Subscription(Components):
    def __init__(self, request, props):
        super(Subscription, self).__init__(request, props)
        self.api_path = 'subscriptions'

    def start(self, body, url_params=None, json=False):
        return self.simple_query(_type='post', _id=self._id, resource='start', url_params=url_params, body=body,
                                 json=json)

    def stop(self, body, url_params=None, json=False):
        return self.simple_query(_type='post', _id=self._id, resource='stop', url_params=url_params, body=body,
                                 json=json)
