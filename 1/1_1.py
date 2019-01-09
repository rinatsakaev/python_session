import types
from functools import wraps


class DecoratorClass:
    def __init__(self, func):
        wraps(func)(self)
        print("init is called")

    def __call__(self, *args, **kwargs):
        print("call is called")
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@DecoratorClass
def test_function():
    print("func is called")

if __name__ == '__main__':
    f = test_function()
    pass
