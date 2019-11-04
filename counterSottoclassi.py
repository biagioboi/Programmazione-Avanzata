
def counter_sottoclassi(clsa):
    old_new = clsa.__new__

    def wrapper(cls, *args, **kwargs):
        if cls is not clsa:
            clsa.figli += 1
        return old_new(cls, *args, **kwargs)

    clsa.__new__ = wrapper
    return clsa


@counter_sottoclassi
class prova:
    figli = 0

    def __init__(self):
        pass

class pippo(prova):
    def __init__(self):
        pass

pippo()
prova()
print("Esistono {} figli della classe prova.".format(prova.figli))