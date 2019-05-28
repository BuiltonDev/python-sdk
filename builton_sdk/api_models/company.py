from builton_sdk.api_models.component import Component
from builton_sdk.utils.rest_functions import *


@rest_decorator(get_all, refresh)
class Company(Component):
    def __init__(self, request, props):
        super(Company, self).__init__(request, props)
        self.api_path = 'companies'

    def get(self, url_params=None, json=False):
        return self.get_all(url_params=url_params, json=json)

    def get_properties(self, url_params=None):
        return self.simple_query(resource='properties', url_params=url_params, json=True)
