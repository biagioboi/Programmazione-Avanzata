def is_not_empty_str(name, value):
    if not isinstance(value, str):
        raise ValueError("{} deve essere di tipo str.".format(name))
    if not bool(value):
        raise ValueError("{} non deve essere una str vuota".format(name))


def ensure(name, fun, doc = None):
    def decor(cls):
        privateName = "__" + name

        def getter(self):
            return getattr(self, privateName)

        def setter(self, value):
            try:
                fun(name, value)
            except ValueError as err:
                print("Eccezione lanciata dal setter: " + str(err))
            setattr(self, privateName, value)
        setattr(cls, name, property(getter, setter, doc=doc))
        return cls
    return decor


@ensure("title", is_not_empty_str)
class Book:
    def __init__(self, title, isbn, price, quantity):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.quantity = quantity

    def value(self):
        return self.price * self.quantity


bk = Book("5648", 56556, 50, 20)
