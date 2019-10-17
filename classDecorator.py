import numbers
def is_not_empty_str(name, value):
    if not isinstance(value, str):
        raise ValueError("{} deve essere di tipo str.".format(name))
    if not bool(value):
        raise ValueError("{} non deve essere una str vuota".format(name))


def is_in_range(minimum = None, maximum = None):
    assert minimum is not None or maximum is not None

    def wrapper(name, value):
        if not isinstance(value, numbers.Number):
            raise ValueError("{} deve essere di tipo Number".format(name))
        if minimum is not None and value < minimum:
            raise ValueError("{} è più piccolo del minimo {} consentito/a ({})".format(name, name, minimum))
        if maximum is not None and value > maximum:
            raise ValueError("{} è più grande del massimo {} consentito/a ({})".format(name, name, maximum))
    return wrapper


def ensure(name, fun, doc = None):
    def decor(cls):
        privateName = "__" + name

        def getter(self):
            return getattr(self, privateName)

        def setter(self, value):
            try:
                fun(name, value)
                setattr(self, privateName, value)
            except ValueError as err:
                print("Eccezione lanciata dal setter: " + str(err))
        setattr(cls, name, property(getter, setter, doc=doc))
        return cls
    return decor


@ensure("title", is_not_empty_str)
@ensure("price", is_in_range(None, 1000))
@ensure("quantity", is_in_range(None, 200))
class Book:
    def __init__(self, title, isbn, price, quantity):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.quantity = quantity

    def value(self):
        return self.price * self.quantity


bk = Book("5648", 50, 50, 20)
print(bk.price)