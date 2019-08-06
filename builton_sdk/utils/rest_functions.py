def rest_decorator(*fns):
    def wrapper(cls):
        for fn in fns:
            setattr(cls, fn.__name__, fn)
        return cls

    return wrapper


def get(cls, *args, **kwargs):
    return cls.simple_get_query(cls.id, *args, **kwargs)


def get_all(cls, *args, **kwargs):
    return cls.simple_query(*args, **kwargs)


def refresh(cls, url_params=None, json=False):
    return get(cls, url_params=url_params, json=json)


def update(cls, *args, **kwargs):
    return cls.simple_query(*args, _type='put', **kwargs)


def delete(cls, *args, **kwargs):
    return cls.simple_del_query(cls.id, *args, **kwargs)


def create(cls, *args, **kwargs):
    return cls.simple_query(*args, _type='post', **kwargs)


def search(cls, query, url_params=None, json=False):
    params = url_params.copy()
    params.update(query)
    return cls.simple_query(url_params=params, json=json)
