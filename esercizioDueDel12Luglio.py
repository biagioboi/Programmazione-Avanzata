
def simil_singleton(clsa):
    clsa._instance = None
    __class__ = clsa
    def new_new(cls, *args, **kwargs):
         if clsa._instance is not clsa:
             clsa._instance = clsa
             return super().__new__(cls)
         else:
             raise RuntimeError("Esiste già un oggetto istanza della classe {}".format(clsa))
    clsa.__new__ = new_new
    return clsa


@simil_singleton
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