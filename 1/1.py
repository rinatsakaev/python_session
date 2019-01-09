import inspect
import types
def func(x, y, *args, **kwargs):
    print(x)
    print(y)
    f = lambda m: str(m) + " positioned arg"
    generator = (f(arg) for arg in args)
    for val in generator:
        print(val)
    g = lambda k, v: str(k) + " value:  " + str(v)
    generator2 = (g(key, value) for key, value in kwargs.items())
    for val in generator2:
        print(val)


def caching_dec(some_func):
    cached_values = dict()

    def result(*args):
        if args in cached_values:
            return cached_values[args]
        res = some_func(*args)
        cached_values[args] = res
        return res

    return result


def texting_dec(some_func):
    def result(self, text):
        return some_func(self, text +" from decorator")
    return result


class A:
    def __init__(self):
        self.age = 21

    @texting_dec
    def say_age(self, text):
        print(self.age, text)


# декоратор класса
def addAnotherArg(cls):
    class AddAnotherArg(cls):
        def __init__(self, another_arg, *args, **kwargs):
            cls.__init__(self, *args, **kwargs)
            self.another_arg = another_arg

    return AddAnotherArg


@addAnotherArg
class B:
    def __init__(self, some_arg):
        self.some_arg = some_arg

if __name__ == '__main__':
    #func(1,2,3,4,5,6, name1=1, name2=234)
    f = lambda x: x**3
    decorated_lambda = caching_dec(f)
    print(decorated_lambda(2))
    print(decorated_lambda(5))
    print(decorated_lambda(2))
    a = A()
    a.say_age("etete")
    print([f for f in globals().values() if type(f) == types.FunctionType])
    b = B(1,3)


    pass
