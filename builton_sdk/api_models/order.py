from builton_sdk.api_models.component import Component
from builton_sdk.utils.rest_functions import *


@rest_decorator(get, create, delete, get_all, refresh, update, search)
class Order(Component):
    def __init__(self, request, props):
        super(Order, self).__init__(request, props)
        self.api_path = 'orders'

    def get_deliveries(self, url_params=None):
        return self.simple_query(_id=self.id, resource='deliveries', url_params=url_params,
                                 json=True)

    def pay(self, body, url_params=None, json=False):
        return self.simple_query(_type='post', _id=self.id, resource='pay', body=body,
                                 url_params=url_params,
                                 json=json)

    def cancel(self, body, url_params=None, json=False):
        return self.simple_query(_type='post', _id=self.id, resource='cancel', body=body,
                                 url_params=url_params,
                                 json=json)

    def create_delivery(self, body, url_params=None):
        return self.simple_query(_type='post', _id=self.id, resource='deliveries', body=body,
                                 url_params=url_params,
                                 json=True)

    def trigger_delivery_action(self, body, delivery_id, url_params=None):
        if not self.id:
            raise ValueError('This method requires an ID')
        if not delivery_id:
            raise ValueError('This method requires a delivery_id')
        return self.simple_query(
            _type='post',
            resource="%s/%s/deliveries/%s" % (self.api_path, self.id, delivery_id),
            body=body,
            url_params=url_params,
            res_constructor=None
        )
