import contextlib
def func():
    try:
        raise ValueError
    except IndexError:
        print("index err")
    finally:
        print("finally")

class SomeClass(contextlib.AbstractContextManager):
    pass


if __name__ == '__main__':
    #func()
    c = SomeClass()