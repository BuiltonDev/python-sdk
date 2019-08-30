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


def refresh(cls, *args, **kwargs):
    return get(cls, id=cls.id, *args, **kwargs)


def update(cls, *args, **kwargs):
    return cls.simple_query(*args, _type='put', **kwargs)


def delete(cls, *args, **kwargs):
    return cls.simple_query(*args, _type='delete', **kwargs)


def create(cls, *args, **kwargs):
    return cls.simple_query(*args, _type='post', **kwargs)


def search(cls, *args, **kwargs):
    return cls.simple_query(*args, **kwargs)
