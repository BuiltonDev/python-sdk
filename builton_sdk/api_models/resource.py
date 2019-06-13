from builton_sdk.api_models.component import Component
from builton_sdk.utils.rest_functions import *


@rest_decorator(create, delete, get, get_all, refresh, update, search)
class Resource(Component):
    def __init__(self, request, props):
        super(Resource, self).__init__(request, props)
        self.api_path = 'resources'

    def create_bulk(self, body, url_params=None, json=False):
        return self.simple_query(_type='post', resource='bulk', body=body, url_params=url_params,
                                 json=json)
