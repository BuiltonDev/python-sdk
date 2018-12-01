from src.collection.components import Components
from src.utils.rest_functions import rest_decorator, create, delete, get, get_all, refresh, update, search
from src.collection.product import Product
from src.collection.provider import Provider


@rest_decorator(create, delete, get, get_all, refresh, update, search)
class Tag(Components):
    def __init__(self, request, props):
        super(Tag, self).__init__(request, props)
        self.api_path = 'tags'

    def get_products(self, url_params=None, json=False):
        return self.simple_query(resource='products', url_params=url_params, json=json, res_constructor=Product)

    def get_providers(self, url_params=None, json=False):
        return self.simple_query(resource='providers', url_params=url_params, json=json, res_constructor=Provider)
