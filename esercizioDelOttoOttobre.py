def dec(old_fun):
    print("cdscdcsdsc")
    def wrap(param):
        return old_fun(param)
    return wrap


class Parrot:

    def __init__(self):
        self.__voltage = 100000

    @dec
    def bye(self):
        print(self.__voltage)

    def ciao (self):
        print("cdsacsdc")

c = Parrot()
c.bye()

prova = []
prova.append(("cd", "cdsc"))
prova.append(("cd", "dcsacds"))
for x in prova:
    y, z = x
    print("{} => {}".format(y, z))


