from src.collection.all import *
from src.utils.request import Request

class Kvass:
    def __init__(self, endpoint, api_key, bearer_token=None):
        if endpoint is None:
            raise ValueError('You need to define an endpoint')
        if api_key is None:
            raise ValueError('You need to define an api_key')
        self.api_key = api_key
        self.bearer_token = bearer_token
        self.endpoint = endpoint
        headers = self._construct_headers()
        self.request = Request(endpoint, headers)

    def refresh_bearer_token(self, new_bearer_token):
        self.bearer_token = new_bearer_token
        headers = self._construct_headers()
        self.request.updateHeaders(headers)

    def _construct_headers(self):
        headers = {
            'X-Kvass-API-Key': self.api_key,
        }
        if self.bearer_token is not None:
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
