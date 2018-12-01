from src.collection.components import Components
from src.utils.rest_functions import rest_decorator, get, create, delete, get_all, refresh, update, search


@rest_decorator(get, create, delete, get_all, refresh, update, search)
class Order(Components):
    def __init__(self, request, props):
        super(Order, self).__init__(request, props)
        self.api_path = 'orders'

    def get_deliveries(self, url_params=None):
        return self.simple_query(_id=self._id_, resource='deliveries', url_params=url_params, json=True)

    def pay(self, body, url_params=None, json=False):
        return self.simple_query(_type='post', _id=self._id_, resource='pay', body=body, url_params=url_params,
                                 json=json)

    def cancel(self, body, url_params=None, json=False):
        return self.simple_query(_type='post', _id=self._id_, resource='cancel', body=body, url_params=url_params,
                                 json=json)

    def create_delivery(self, body, url_params=None):
        return self.simple_query(_type='post', _id=self._id_, resource='deliveries', body=body, url_params=url_params,
                                 json=True)

    def trigger_delivery_action(self, body, delivery_id, url_params=None):
        # TODO: build query
        return None
