from builton_sdk.api_models._component import _Component
from builton_sdk.utils.rest_functions import *


@rest_decorator(create, get, get_all, search, refresh, delete)
class AIModel(_Component):
    def __init__(self, request, props):
        super(AIModel, self).__init__(request, props)
        self.api_path = 'ai/models'

    def train(self, url_params=None, json=False):
        return self._simple_query(_type='post', _id=self.id, resource='train', url_params=url_params,
                                  json=json)

    def get_recommendations(self, body, url_params=None):
        _id = self.id if self.id is not None else ''
        return self._simple_query(_type='post', _id=_id, resource='invoke', url_params=url_params,
                                  body=body, json=True)

    def create_version(self, body, url_params=None):
        return self.simple_query(_type='post', _id=self._id, resource='invoke', url_params=url_params,
                                 body=body, json=True)

    def create(self, body, url_params=None, json=False):
        return self._simple_query(_type='post', _id=self.id, body=body, url_params=url_params,
                                  json=json)
