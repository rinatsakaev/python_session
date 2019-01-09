def f1():
    a = 1
    b = 2

def f2():
    c = 3
    e = 8
    d = 4
    def f3():
        e = 5
        nonlocal d
        d = 6
