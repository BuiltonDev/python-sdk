class Components():
    def __init__(self, request, props):
        if self.__class__.__name__ == 'Components':
            raise Exception('Cannot construct Abstract instances')

        self.identifier = None
        self.request = request
        self.id = None
        self.api_path = None

        if isinstance(props, str):
            self.id = props
        elif isinstance(props, dict):
            self.build_instance(props)

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
                data = res_constructor(self.request)
            else:
                self.build_instance(res_data)
                data = self
        elif isinstance(res_data, (int, str, float)):
            data = res_data
        return data

    def simple_query(
            self,
            _type='get',
            _id='',
            resource='',
            url_params=None,
            body=None,
            api_path=None,
            res_constructor=None,
            json=False
    ):
        if _id is None:
            raise ValueError('This method requires an ID')
        if self.id and _id is not '':
            local_id = '/%s' % self.id
        elif _id:
            local_id = _id if _id[0] is '/' else '/%s' % _id
        else:
            local_id = ''

        local_resource = resource if not resource or resource[0] is '/' else '/%s' % resource
        local_api_path = api_path if api_path else self.api_path
        resource = ''.join([local_api_path, local_id, local_resource])

        # TODO: add pagination
        # TODO: add object expand

        res = self.request.query(
            _type=_type,
            url_params=url_params,
            body=body,
            resource=resource
        )
        if not 200 >= res.status_code < 400:
            error = {'Bad response': '%s' % res.status_code}
            try:
                error_message = res.json()
                if isinstance(error_message, dict):
                    error = error_message
            except Exception:
                pass
            raise Exception(error)

        res_data = res.json()
        return self.parse_json(res_data, res_constructor, raw_json=json)

    def build_query(self, _type='get', resource='', url_params=None, body=None, headers=None,
                    endpoint=None, res_constructor=None, json=False):
        res = self.request.query(
            _type=_type,
            url_params=url_params,
            body=body,
            resource=resource,
            headers=headers,
            endpoint=endpoint
        )
        if not 200 >= res.status_code < 400:
            raise Exception('Bad response: %s' % res.status_code)

        res_data = res.json()
        return self.parse_json(res_data, res_constructor, raw_json=json)
