class Element:
    def __init__(self, number):
        self.number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if value < 0:
            raise Exception()
        self._number = value

    @number.getter
    def number(self):
        return self._number + 1000

    def __contains__(self, item):
        return self._number == item

    def __call__(self, *args, **kwargs):
        return 120


class Meta(type):

    def __new__(mcs, *args, **kwargs):
        instance = super().__new__(mcs, *args, **kwargs)
        instance.attr = 150
        return instance


class SomeClass(metaclass=Meta):
    pass


if __name__ == '__main__':
    e = Element(50)
    print(e.number)
    print(50 in e)
    print(e()) #120
    c = SomeClass()
    pass