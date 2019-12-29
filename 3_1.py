def lru_cache(function):
    cache = {}

    def wrapper(*args, **kwargs):
        args_key = args
        kwargs_key = ('kwargs',)
        kwargs_key = kwargs_key + tuple(kwargs.items())
        key = args_key + kwargs_key
        if key in cache:
            return cache.get(args_key)

        value = function(*args, **kwargs)
        cache[args_key] = value
        return value

    return wrapper
