#decoratore di classe parametrizzato con : la classe contenente ff, la funzione ff e la funzione
class ClasseConFF:
    @staticmethod
    def ff():
        print("Cddscsdac")

def estendiFF(Class):
    if ("ff" not in Class.__dict__):
        Class.ff = ClasseConFF.ff
    return Class

def aggiungiDelegato(classeConDelegato, functDaChiamare, functDelDelegato):
    def add(Class):
        setattr(Class, functDaChiamare, getattr(classeConDelegato, functDelDelegato))
        return Class
    return add


@aggiungiDelegato(ClasseConFF, "f", "ff")
class addMetodClass:
    @staticmethod
    def addMethod(function = None):
        if (function is not None):
            setattr(addMetodClass, "f", function)


addMetodClass.f()