import itertools
import sys
"""blblblbl"""
class A:
    def __call__(self, *args, **kwargs):
        print("called")
    def __init__(self):
        pass
class B:
    print("Called111")

if __name__ == '__main__':
    a = A()
    a()
    c = 1
    v = sys.stdout.write("123")
    print(sys.stdout.write("aaa?"), "Nu ladno", sys.stdout.write("sdadim?"), print((lambda x: x)(__doc__ and 1)))
    print("doc",__doc__)
    a = -5
    b = -5
    print(a is b)
    a = -6
    b = -6
    print(a is b)
    print(*map(lambda x,y: x+y, (1,2), (5,6)))