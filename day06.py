# 9.3
def test(func):
    """
    Program that calculate 2 index's sum'
    :param func: decorate function
    :return: result
    """
    def new_func(*args, **kwargs):
        result = func(*args, **kwargs)
        print('Start: ', func.__name__)
        print('Result: ', result)
        print('End. Thank you for using', func.__name__)
        return  result
    return new_func

@test
def suma(x, y):
    return x + y

suma(3, 23)
