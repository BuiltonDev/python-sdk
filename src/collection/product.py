from src.collection.components import Components
from src.utils.rest_functions import rest_decorator, create, delete, get, get_all, refresh, update, search


@rest_decorator(create, delete, get, get_all, refresh, update, search)
class Product(Components):
    def __init__(self, request, props):
        super(Product, self).__init__(request, props)
        self.api_path = 'products'
