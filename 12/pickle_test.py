import pickle


class SomeClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"SomeClass:{{ {self.a} {self.b} }}"

    def __getstate__(self):
        return {"key": 2}
    def __setstate__(self, state):
        print(state)

if __name__ == '__main__':
    o = SomeClass(1,2)
    pickled_obj = pickle.dumps(o)
    print(pickled_obj)
    unpickled_obj = pickle.loads(pickled_obj)
 