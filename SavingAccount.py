
def count(aClass):
    aClass.numInstances = 0
    aClass.old_init = aClass.__init__
    def mod_init(self, *args, **kwargs):
        aClass.numInstances = aClass.numInstances + 1
        aClass.old_init(self, *args, **kwargs)
    aClass.__init__ = mod_init
    return aClass


@count
class SavingAccount:
    # in questo caso la percentuale degli interessi è fissa, dunque fa parte della classe e non dell'oggetto specifico
    interestPercent = 5.2

    def __init__(self, name, save):
        self.name = name
        self.save = save

    @staticmethod
    def getInterest():
        return SavingAccount.interestPercent


SavingAccount("Carlo", 5)
SavingAccount("Gerardo", 20)
print(SavingAccount.numInstances)
