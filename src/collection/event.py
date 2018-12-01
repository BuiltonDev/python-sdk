from src.collection.components import Components
from src.utils.rest_functions import rest_decorator, get, get_all, refresh, search


@rest_decorator(get, get_all, refresh, search)
class Event(Components):
    def __init__(self, request, props):
        super(Event, self).__init__(request, props)
        self.api_path = 'events'
