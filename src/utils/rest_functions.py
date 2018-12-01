def rest_decorator(*fns):
    def wrapper(self):
        for fn in fns:
            setattr(self, fn.__name__, fn)
        return self
    return wrapper


def get(self, url_params=None, json=False):
    return self.simple_query(_id=self._id_, url_params=url_params, json=json)


def get_all(self, url_params=None, json=False):
    return self.simple_query(url_params=url_params, json=json)


def refresh(self, url_params=None, json=False):
    return get(self, url_params=url_params, json=json)


def update(self, body=None, url_params=None, json=False):
    return self.simple_query(_type='put', _id=self._id_, body=body, url_params=url_params, json=json)


def delete(self, url_params=None, json=False):
    return self.simple_query(_type='del', _id=self._id_, url_params=url_params, json=json)


def create(self, body=None, url_params=None, json=False):
    return self.simple_query(_type='post', body=body, url_params=url_params, json=json)


def search(self, query, url_params=None, json=False):
    params = url_params.copy()
    params.update(query)
    return self.simple_query(url_params=params, json=json)
