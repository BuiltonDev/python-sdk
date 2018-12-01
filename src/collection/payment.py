from src.collection.components import Components
from src.utils.rest_functions import rest_decorator, create, delete, get, get_all, refresh, update, search


@rest_decorator(create, delete, get, get_all, refresh, update, search)
class Payment(Components):
    def __init__(self, request, props):
        super(Payment, self).__init__(request, props)
        self.api_path = 'payments'
