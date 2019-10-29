# conta il numero di invocazioni di un solo metodo
def countdecfact(meth):
    def countdecorator(aClass):
        aClass.numTimes = 0
        setattr(aClass, "old_meth", getattr(aClass, meth))
        def newMeth(*args, **kwargs):
            aClass.numTimes += 1
            getattr(aClass, "old_meth")(*args, **kwargs)
        setattr(aClass, meth, newMeth)
        def nTimes():
            return aClass.numTimes
        aClass.nTimes = staticmethod(nTimes)
        return aClass
    return countdecorator
@countdecfact("meth1")
class myClass:
    def meth1(self):
        print("meth 1")
    def meth2(self):
        print("meth 2")

a = myClass()
a.meth1()
print(a.numTimes)












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