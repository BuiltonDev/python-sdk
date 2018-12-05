class Components():
    def __init__(self, request, props, _id=None, api_path=None):
        # raise Exception('Cannot construct Abstract instances')
        self.identifier = None
        self.request = request
        self.api_path = api_path
        self._id = _id

        if isinstance(props, str):
            self._id = props
        elif props is not None:
            self.build_instance(props)

    def build_instance(self, props):
        for key, value in props.items():
            self.__setattr__(key, value)

        if props and '_id' in props and '$oid' in props['_id']:
            self._id = props['_id']['$oid']

    def parse_json(self, res, res_constructor, raw_json=False):
        data = {}
        res_data = res.json() if not isinstance(res, (dict, list)) else res
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
        if self._id and _id is not '':
            local_id = '/%s' % self._id
        elif _id:
            local_id = _id if _id[0] is '/' else '/%s' % _id
        else:
            local_id = ''

        local_resource = resource if not resource or resource[0] is '/' else '/%s' % resource
        local_api_path = api_path if api_path else self.api_path
        resource = self.build_resource_path(local_api_path, local_id, local_resource)
        # TODO: add pagination
        res = self.request.query(
            _type=_type,
            url_params=url_params,
            body=body,
            resource=resource
        )
        if not 200 >= res.status_code < 400:
            error = None
            try:
                error = res.json()
            except Exception:
                pass
            raise Exception('Bad response: %s | %s' % (res.status_code, error))

        return self.parse_json(res, res_constructor, raw_json=json)

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

        return self.parse_json(res, res_constructor, raw_json=json)

    @staticmethod
    def build_resource_path(*args):
        resource = ""
        for arg in args:
            resource += arg
        return resource
