class Components():
    def __init__(self, request, props):
        # raise Exception('Cannot construct Abstract instances')
        self.identifier = None
        self.request = request

        self._id_ = None

        if isinstance(props, str):
            self._id_ = props
        elif props is not None:
            self.build_instance(props)

    def build_instance(self, props):
        for key in props.keys():
            self.__setattr__(key, props[key])

        if props and props['_id'] and props['_id']['$oid']:
            self._id_ = props['_id']['$oid']

    def parse_json(self, res, res_constructor, raw_json):
        json = res.json()
        if raw_json:
            return json
        if isinstance(json, list):
            obj_array = []
            for element in json:
                if res_constructor:
                    obj_array.append(res_constructor(self.request, element))
                else:
                    component = self.__class__(self.request, element)
                    obj_array.append(component)
            return obj_array
        if isinstance(json, dict):
            if res_constructor:
                return res_constructor(self.request)
            self.build_instance(json)
            return self
        return json

    def simple_query(self,
                    _type='get',
                    _id='',
                    resource='',
                    url_params=None,
                    body=None,
                    api_path=None,
                    res_constructor=None,
                    json=False,
                    ):
        if _id is None:
            raise ValueError('Needs an ID to call this method')
        if self._id_ and _id is not '':
            local_id = '/%s' % self._id_
        elif _id:
            local_id = _id if _id[0] is '/' else '/%s' % _id
        else:
            local_id = ''

        local_resource = resource if not resource or resource[0] is '/' else '/%s' % resource
        local_api_path = api_path if api_path else self.api_path
        res = self.request.query(
            _type=_type,
            url_params=url_params,
            body=body,
            resource=local_api_path+local_id+local_resource
        )
        if not 200 >= res.status_code < 400:
            raise Exception('Bad response: %s' % res.status_code)

        return self.parse_json(res, res_constructor, raw_json=json)
