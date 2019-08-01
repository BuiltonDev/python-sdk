from urllib.parse import urljoin


ALLOWED_URL_PARAMS = ["size", "sort", "page", "order_status"]


class Component:
    def __init__(self, request, props=None):
        if self.__class__ == Component:
            raise Exception('Cannot construct Abstract instances')

        self.identifier = None
        self.request = request
        self.id = None
        self.api_path = None

        if isinstance(props, str):
            self.id = props
        elif isinstance(props, dict):
            self.build_instance(props)
        elif props is not None:
            raise ValueError("props should be str, dict or None")

    def build_instance(self, props):
        for key, value in props.items():
            self.__setattr__(key, value)

        if props and '_id' in props and '$oid' in props['_id']:
            self.id = props['_id']['$oid']

    def parse_json(self, res_data, res_constructor, raw_json=False):
        data = {}
        if raw_json:
            data = res_data
        elif isinstance(res_data, list):
            data = [self.parse_json(element, res_constructor) for element in res_data]
        elif isinstance(res_data, dict):
            if res_constructor:
                data = res_constructor(self.request, res_data)
            else:
                new_instance = self.__class__(self.request, res_data)
                data = new_instance
        elif isinstance(res_data, (int, str, float)):
            data = res_data
        return data

    def build_resource(self, _id, resource, api_path=None):
        if _id is None:
            raise ValueError('This method requires an ID')

        local_id = ''
        if _id:
            local_id = urljoin('/', _id)
        elif self.id:
            local_id = urljoin('/', self.id)

        local_resource = resource if not resource or resource[0] is '/' else '/%s' % resource
        local_api_path = api_path if api_path else self.api_path
        return ''.join([local_api_path, local_id, local_resource])

    def handle_error(self, response):
        if not 200 >= response.status_code < 400:
            error = {'Bad response': '%s' % response.status_code}
            try:
                error_message = response.json()
                if isinstance(error_message, dict):
                    error = error_message
            except Exception:
                pass
            raise Exception(error)

    @staticmethod
    def _build_url_params(kwargs):
        return dict(filter(lambda item: item[0] in ALLOWED_URL_PARAMS, kwargs.items()))

    def simple_get_query(self, *args, _type='get', **kwargs):
        _id = ''

        if len(args) == 2:
            _id = args[1]
        elif len(args) > 2:
            raise Exception("Not expecting more than the id as an argument")
        elif 'id' in kwargs:
            _id = kwargs.pop('id')
        else:
            raise Exception("Need id to get resource")

        url_params = self._build_url_params(kwargs)

        return self.simple_query(_id=_id, url_params=url_params, _type=_type)

    def simple_query(self,
                     _type='get',
                     _id='',
                     resource='',
                     url_params=None,
                     body=None,
                     api_path=None,
                     res_constructor=None,
                     json=False,
                     **kwargs):

        # TODO: add pagination
        # TODO: add object expand

        if url_params is None:
            url_params = {}

        resource = self.build_resource(_id, resource, api_path)

        if _type == 'get':
            url_params.update(self._build_url_params(kwargs))

        elif _type == 'put':
            if body is None:
                body = {}

            body.update(kwargs)

        response = self.request.query(
            _type=_type,
            url_params=url_params,
            body=body,
            resource=resource
        )
        self.handle_error(response)

        try:
            response_data = response.json()
            response = self.parse_json(response_data, res_constructor, raw_json=json)
        except Exception:
            raise Exception("Error parsing JSON")
        return response

    def __repr__(self):
        if hasattr(self, 'id'):
            return "<%s %s>" % (self.__class__.__name__, self.id)
