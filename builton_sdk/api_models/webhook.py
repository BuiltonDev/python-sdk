from builton_sdk.api_models._component import _Component
from builton_sdk.utils.rest_functions import *


@rest_decorator(create, delete, get, get_all, refresh, update, search)
class Webhook(_Component):
    def __init__(self, request, props):
        super(Webhook, self).__init__(request, props)
        self.api_path = 'webhooks'
