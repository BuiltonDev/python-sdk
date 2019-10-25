from builton_sdk.api_models._component import _Component
from builton_sdk.utils.rest_functions import *
from builton_sdk.api_models.subscription import Subscription


@rest_decorator(create, delete, get, get_all, refresh, update, search)
class Plan(_Component):
    def __init__(self, request, props):
        super(Plan, self).__init__(request, props)
        self.api_path = 'plans'

    def get_subscriptions(self, url_params=None, json=False):
        return self._simple_query(_id=self.id, resource='subscriptions', url_params=url_params,
                                  json=json, res_constructor=Subscription)
