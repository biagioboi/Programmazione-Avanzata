def is_empty(name, value):
    pass

class Ensure:
    def __init__(self, validate, doc = None):
        self.validate = validate
        self.doc = doc


def do_ensure(cls):
    def make_property(name, val):
        privateName = "_" + name

        def getter(self):
            return getattr(self, privateName)

        def setter(self, value):
            val.validate(name, value)
            setattr(self, privateName, value)

        return property(getter, setter, doc=val.doc)

    for name, val in cls.__dict__.items():
        if isinstance(val, Ensure):
            setattr(cls, name, make_property(name, val))

    return cls

@do_ensure
class prova:
    nome = Ensure(is_empty)
    cognome = Ensure(is_empty)

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

x = prova('Biagio', 'Boi')
print(x.nome)