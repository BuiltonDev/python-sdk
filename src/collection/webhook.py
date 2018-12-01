from src.collection.components import Components
from src.utils.rest_functions import rest_decorator, create, delete, get, get_all, refresh, update


@rest_decorator(create, delete, get, get_all, refresh, update)
class Webhook(Components):
    def __init__(self, request, props):
        super(Webhook, self).__init__(request, props)
        self.api_path = 'webhooks'
