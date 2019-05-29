import re

from builton_sdk.api_models import *
from builton_sdk.utils.request import Request

DEFAULT_ENDPOINT = "https://api.builton.dev/"


class Builton:
    def __init__(self, api_key, bearer_token, endpoint=DEFAULT_ENDPOINT):
        self.validate_input(endpoint, api_key, bearer_token)
        self.api_key = api_key
        self.bearer_token = bearer_token
        self.endpoint = endpoint
        headers = self._construct_headers()
        self.request = Request(endpoint, headers)

    @staticmethod
    def validate_input(endpoint, api_key, bearer_token):
        if endpoint is None:
            raise ValueError('You need to define an endpoint')
        if not isinstance(endpoint, str):
            raise ValueError('endpoint not a string')
        if api_key is None:
            raise ValueError('You need to define an api_key')
        if not isinstance(api_key, str):
            raise ValueError('api_key not a string')
        if bearer_token and not isinstance(bearer_token, str):
            raise ValueError('Bearer token not a string')

    def refresh_bearer_token(self, new_bearer_token):
        self.bearer_token = new_bearer_token
        headers = self._construct_headers()
        self.request.update_headers(headers)

    def _construct_headers(self):
        headers = {
            'X-Builton-API-Key': self.api_key,
        }
        if self.bearer_token is not None:
            # Remove 'Bearer ' if it's in the beginning of the bearer_token. Add it under
            self.bearer_token = re.sub('^bearer ', '', self.bearer_token, flags=re.IGNORECASE)
            headers['Authorization'] = "Bearer %s" % self.bearer_token
        return headers

    def ai_model(self, props=None):
        return AIModel(self.request, props)

    def company(self, props=None):
        return Company(self.request, props)

    def event(self, props=None):
        return Event(self.request, props)

    def order(self, props=None):
        return Order(self.request, props)

    def payment(self, props=None):
        return Payment(self.request, props)

    def payment_method(self, props=None):
        return PaymentMethod(self.request, props)

    def plan(self, props=None):
        return Plan(self.request, props)

    def product(self, props=None):
        return Product(self.request, props)

    def provider(self, props=None):
        return Provider(self.request, props)

    def resource(self, props=None):
        return Resource(self.request, props)

    def subscription(self, props=None):
        return Subscription(self.request, props)

    def tag(self, props=None):
        return Tag(self.request, props)

    def user(self, props=None):
        return User(self.request, props)

    def webhook(self, props=None):
        return Webhook(self.request, props)
