from builton_sdk.api_models.component import Component
from builton_sdk.api_models.product import Product
from builton_sdk.api_models.provider import Provider
from builton_sdk.utils.rest_functions import *


@rest_decorator(create, delete, get, get_all, refresh, update, search)
class Tag(Component):
    def __init__(self, request, props):
        super(Tag, self).__init__(request, props)
        self.api_path = 'tags'

    def get_products(self, url_params=None, json=False):
        return self.simple_query(resource='products', url_params=url_params, json=json,
                                 res_constructor=Product)

    def get_providers(self, url_params=None, json=False):
        return self.simple_query(resource='providers', url_params=url_params, json=json,
                                 res_constructor=Provider)
