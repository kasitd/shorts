from functools import wraps


def make_html(element):

    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            return'<{el}>{function}</{el}>'.format(el=element, function=function())
        return wrapper
    return inner_function