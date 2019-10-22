def contaMetodo(metodo):
    def wrapper(cls):
        setattr(cls, "old_met", getattr(cls, metodo))
        def nuovoMetodo(*args, **kwargs):
            cls.__numeroChiamate__ += 1
            getattr(cls, "old_met")(*args, **kwargs)
        setattr(cls, metodo, nuovoMetodo)


        def numeroChiamate():
            return cls.__numeroChiamate__
        cls.numeroChiamate = staticmethod(numeroChiamate)


        return cls

    return wrapper

@contaMetodo("methodOne")
class myClass:
    __numeroChiamate__ = 0
    def methodOne(self):
        pass
    def methodTwo(self):
        pass

x = myClass()
x.methodOne()
print(myClass.numeroChiamate())