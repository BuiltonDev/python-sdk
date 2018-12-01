from src.collection.components import Components
from src.utils.rest_functions import rest_decorator, create, get, get_all, search


@rest_decorator(create, create, get, get_all, search)
class AIModel(Components):
    def __init__(self, request, props):
        super(AIModel, self).__init__(request, props)
        self.api_path = 'ai/models'

    def train(self, url_params=None, json=False):
        return self.simple_query(_type='post', _id=self._id_, resource='train', url_params=url_params, json=json)

    def get_recommendations(self, body, url_params=None):
        _id = self._id_ if self._id_ is not None else ''
        return self.simple_query(_type='post', _id=_id, resource='invoke', url_params=url_params, body=body, json=True)
