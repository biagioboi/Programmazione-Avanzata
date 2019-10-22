class MyClass:

    def __init__(self, v):
        self.v = v

    def f(self, a):
        pass
    def g(self, x, y):
        print("Somma di {} e {} ".format(x, y))
    def create(self):
        pass
    def finalize(self):
        pass

class P:
    def __init__(self):
        self.instance = MyClass(10)
        self.operation = []

    def f(self, a):
        MyClass.f(self.instance, a)

    def g(self, x, y):
        self.operation.append((MyClass.g , x, y))
        return

    def create(self):
        self.operation.append((MyClass.create))
        return

    def finalize(self):
        for x, *y in self.operation:
            x(self.instance, *y)
            break


z = P()
z.g(5, 10)
z.finalize()