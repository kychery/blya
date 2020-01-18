def lru_cache(function):
  cache = {}

  def wrapper(*args, **kwargs):
    args_key = args
    kwargs_key = ('kwargs',)
    kwargs_key = kwargs_key + tuple(kwargs.items())
    key = args_key + kwargs_key
   
    if key in cache:
      return cache.get(key)

    result = function(*args, **kwargs)
    cache[key] = result
    return result

  return wrapper

@lru_cache
def sum_two_numbers(a, b, c=3):
  return a + b
