class prova:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass
x = prova(5, 6)
print(type(x))
print(x.x)