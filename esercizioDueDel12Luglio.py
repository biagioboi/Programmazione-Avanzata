
def counter_sottoclassi(clsa):
    old_new = clsa.__new__

    def wrapper(cls, *args, **kwargs):
        if cls is not clsa:
            clsa.figli += 1
        return old_new(cls, *args, **kwargs)

    clsa.__new__ = wrapper
    return clsa

# def simil_singleton(clsa):
#     clsa._instance = None
#     # __class__ = clsa
#     old_new = clsa.__new__
#     def wrapper(cls, *args, **kwargs):
#         if clsa._instance is not clsa:
#             clsa._instance = clsa
#             return old_new(cls, *args, **kwargs)
#         else:
#             raise RuntimeError("Esiste già un oggetto istanza della classe {}".format(clsa))
#     clsa.__new__ = wrapper
#     return clsa

@counter_sottoclassi
class prova:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

x = prova("biagio", "boi")
print(x.nome)
try:
    y = prova("biagio", "boi")
except RuntimeError:
    print("Errore a runtime.")