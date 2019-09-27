from builton_sdk.api_models.component import Component
from builton_sdk.utils.rest_functions import *


@rest_decorator(create, delete, get, get_all, refresh, update, search)
class Product(Component):
    def __init__(self, request, props):
        super(Product, self).__init__(request, props)
        self.api_path = 'products'

    def get_subproducts(self, url_params=None, json=False):
        return self.simple_query(_id=self.id, resource='sub_products', url_params=url_params,
                                 json=json)

    def search_subproducts(self, query="", url_params=None, json=False):
        return self.simple_query(_id=self.id, resource='sub_products', url_params=url_params,
                                 json=json, query=query)
