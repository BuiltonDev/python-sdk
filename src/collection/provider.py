from src.collection.user import User


class Provider(User):
    def __init__(self, request, props):
        super(User, self).__init__(request, props)
        self.api_path = 'providers'

    def create(self, body, url_params=None, json=False):
        return self.simple_query(_type='post', api_path='v2/providers', url_params=url_params, body=body, json=json)

    def find(self, url_params=None, json=False):
        return self.simple_query(resource='find', url_params=url_params, json=json)

    def get_available_count(self, url_params=None):
        return self.simple_query(resource='available-count', url_params=url_params, json=True)

    def get_all_reports(self, url_params=None):
        return self.simple_query(resource='reports-count', url_params=url_params, json=True)

    def get_reports(self, url_params=None):
        return self.simple_query(_id=self._id_, resource='reports-count', url_params=url_params, json=True)

    def get_available_overview(self, url_params=None):
        return self.simple_query(_id=self._id_, resource='available-overview', url_params=url_params, json=True)

    def get_schedule(self, url_params=None):
        return self.simple_query(_id=self._id_, resource='schedule', url_params=url_params, json=True)

    def get_availability(self, url_params=None):
        return self.simple_query(_id=self._id_, resource='availability', url_params=url_params, json=True)

    def get_available_at(self, url_params=None):
        return self.simple_query(_id=self._id_, resource='available-at', url_params=url_params, json=True)

    def get_products(self, url_params=None):
        return self.simple_query(_id=self._id_, resource='products', url_params=url_params, json=True)

    def post_products(self, body, url_params=None):
        return self.simple_query(_type='post', _id=self._id_, resource='products', body=body, url_params=url_params,
                                 json=True)

    def update_addresses(self, body, url_params=None):
        raise NotImplementedError
