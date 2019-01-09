import operator
from collections import namedtuple


def gen():
    some_val = 0
    while True:
        new_val = yield some_val
        if new_val is None:
            some_val += 1
        else:
            some_val = new_val
if __name__ == '__main__':
    g = gen()
    print(next(g))
    print(next(g))
    g.send(120)
    print(next(g))

    m1 = [x for x in range(10)]
    print(type(m1))
    m2 = (x for x in range(10))
    print(type(m2))
    m3 = {x for x in range(10)}
    print(type(m3))
    m4 = tuple(x for x in range(10))
    print(type(m4))
    m5 = {f"k{x}": x for x in range(10)}
    print(type(m5))
    l = [1, 2, 3, 5]
    res = map(lambda x: x**2, l)
    print(type(res))
    getter = operator.itemgetter(2)
    print(getter((1,2,3,4)))
    getter1 = operator.attrgetter("some_attr")
    tup = namedtuple("NamedTuple", ["attr1", "attr2", "some_attr"])
    t = tup(1,2,10)
    print(getter1(t))
    pass