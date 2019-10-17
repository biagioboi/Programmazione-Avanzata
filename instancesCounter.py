def count(aClass):
    aClass.numInstances = 0

    aClass.__old_init__ = aClass.__init__

    def newInit(self, *args, **kwargs):
        aClass.numInstances += 1
        aClass.__old_init__(self, *args, **kwargs)
    aClass.__init__ = newInit

    return aClass

@count
class Prova:

    def __init__(self):
        print("cdscdsa")
        pass

    @classmethod
    def getInstances(cls):
        return cls.numInstances


a = Prova()
b = Prova()

print(Prova.getInstances())