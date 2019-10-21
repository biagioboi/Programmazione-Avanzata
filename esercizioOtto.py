def contaChiamate(function):
    def wrapper(self, *args, **kwargs):
        if self.__class__.__numChiamate__ is None:
            self.__class__.__numChiamate__ = 1
        else:
            self.__class__.__numChiamate__ += 1
        return function(self, *args, **kwargs)
    return wrapper

class classeProva:
    __numChiamate__ = None

    @contaChiamate
    def altroMetodo(self):
        pass

    @contaChiamate
    def altroAncoraMetodo(self):
        pass

    @classmethod
    def getNumeroChiamate(cls):
        return(cls.__numChiamate__)

x = classeProva()
x.altroMetodo()
x.altroAncoraMetodo()
print(x.getNumeroChiamate())