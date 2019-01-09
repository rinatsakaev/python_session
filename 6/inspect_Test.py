import inspect
import abc
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self):
        return self.a + self.b

class B(abc.ABC):
    @abc.abstractmethod
    def some_method(self):
        pass
    pass
if __name__ == '__main__':
    a = A(1,2)
    a.get_sum()
    print(inspect.getmembers(A))
    print(inspect.isabstract(B))
