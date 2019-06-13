from builton_sdk.api_models.user import User


class Provider(User):
    def __init__(self, request, props):
        super(User, self).__init__(request, props)
        self.api_path = 'providers'

    def find(self, url_params=None, json=False):
        return self.simple_query(resource='find', url_params=url_params, json=json)

    def get_available_count(self, url_params=None):
        return self.simple_query(resource='available-count', url_params=url_params, json=True)

    def get_all_reports(self, url_params=None):
        return self.simple_query(resource='reports-count', url_params=url_params, json=True)

    def get_reports(self, url_params=None):
        return self.simple_query(_id=self.id, resource='reports-count', url_params=url_params,
                                 json=True)

    def get_available_overview(self, url_params=None):
        return self.simple_query(_id=self.id, resource='available-overview', url_params=url_params,
                                 json=True)

    def get_schedule(self, url_params=None):
        return self.simple_query(_id=self.id, resource='schedule', url_params=url_params, json=True)

    def get_availability(self, url_params=None):
        return self.simple_query(_id=self.id, resource='availability', url_params=url_params,
                                 json=True)

    def get_available_at(self, url_params=None):
        return self.simple_query(_id=self.id, resource='available-at', url_params=url_params,
                                 json=True)

    def get_products(self, url_params=None):
        return self.simple_query(_id=self.id, resource='products', url_params=url_params, json=True)

    def update_addresses(self, body, url_params=None):
        raise NotImplementedError
