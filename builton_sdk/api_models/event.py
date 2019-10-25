from builton_sdk.api_models._component import _Component
from builton_sdk.utils.rest_functions import *


@rest_decorator(get, get_all, refresh, search)
class Event(_Component):
    def __init__(self, request, props):
        super(Event, self).__init__(request, props)
        self.api_path = 'events'
