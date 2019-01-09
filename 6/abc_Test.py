# Python 3.4+
from abc import ABC, abstractmethod


class Abstract(ABC):
    @abstractmethod
    def foo(self):
        pass

    def bar(self):
        print("Called bar")


class GoodClass(Abstract):
    def foo(self):
        pass
    pass

class NonAbcClass:
    @abstractmethod
    def foo(self):
        pass

class NonAbcChild(NonAbcClass):
    pass
# без использования АБК можно запретить создание класса вот так:


class Base:
    def __init__(self):
        if type(self) is Base:
            raise Exception('Base is an abstract class and cannot be instantiated directly')
        # Any initialization code
        print('In the __init__  method of the Base class')


class Sub(Base):
    def __init__(self):
        print('In the __init__ method of the Sub class before calling __init__ of the Base class')
        super().__init__()
        print('In the __init__ method of the Sub class after calling __init__ of the Base class')

if __name__ == '__main__':
    a = GoodClass()
    a.bar()
    b = Sub()

    c = NonAbcChild() # abstractmethod ignored