import itertools
import sys
import time
import copy
import datetime


def main():
    # stessa vista per i due libri osservati
    IV = VistaIst()

    # se il vostro codice non funziona con un'univa vista di tipo VisitIst allora togliete il commento alla linea qui sotto
    # e sostituite IVbis al posto di IV nella linea 25

    # IVbis=VistaIst()

    bibliotecaCentrale = Biblioteca("Biblioteca Centrale")
    libreriaMandetori = Libreria("Libreria Mandetori")
    libreriaFaltranella = Libreria("Libreria Faltranella")
    libroCPiuPiu = Libro("C++", {})
    libroJava = Libro("Java per tutti", [libroCPiuPiu])
    libroJava.observers_add(IV)
    libroPython = Libro("Python versus Java", [libroJava, libroCPiuPiu])
    libroOOP = Libro("OOP fundamentals", [libroJava, libroPython, libroCPiuPiu])
    libroOOP.observers_add(IV)

    print("La biblioteca centrale acquisisce \"Java per tutti\"\n")
    bibliotecaCentrale.compra(libroJava)
    print("I riferimenti di \"{}\" sono {}\n".format(libroJava.titolo,
                                                     [(x, y.titolo) for x, y in libroJava.riferimenti.items()]))
    print("La libreria Faltrenella compra 199 copie di \"{}\"\n".format(libroJava.titolo))
    libreriaFaltranella.compra(libroJava, 199)
    print("La biblioteca centrale acquisisce \"{}\"\n".format(libroOOP.titolo))
    print("I riferimenti di \"{}\" sono {}\n".format(libroOOP.titolo,
                                                     [(x, y.titolo) for x, y in libroOOP.riferimenti.items()]))
    print("La libreria Faltrenella compra 100 copie di \"{}\"\n".format(libroOOP.titolo))
    libreriaFaltranella.compra(libroOOP, 100)
    print("La {} compra 48 copie di  \"{}\"\n".format(libreriaMandetori.nome, libroOOP.titolo))
    libreriaMandetori.compra(libroOOP, 48)
    print("Proviamo a modificare i riferimenti di libroCPiuPiu")
    try:
        libroCPiuPiu.riferimenti[1] = libroPython
    except RuntimeError:
        print("Errore: non e` possibile modificare i riferimenti del libro\n")

    print("I riferimenti di \"{}\" sono {}\n".format(libroCPiuPiu.titolo,
                                                     [(x, y.titolo) for x, y in libroCPiuPiu.riferimenti.items()]))


class fruitore:
    def __init__(self, nome):
        self.nome = nome

    def compra(self, libro, num=1):
        libro.numero_copie += num


class Biblioteca(fruitore):

    def compra(self, libro):
        super().compra(libro)


class Libreria(fruitore):
    pass


class Observed:

    def __init__(self):
        self.__observers = set()

    def observers_add(self, observer, *observers):
        for observer in itertools.chain((observer,), observers):
            self.__observers.add(observer)
            observer.update(None)

    def observer_discard(self, observer):
        self.__observers.discard(observer)

    def observers_notify(self, ob):
        for observer in self.__observers:
            observer.update(ob)

class MyDict(dict):
    def __setitem__(self, key, value):
        raise RuntimeError("Operazione vietata")


class Libro(Observed):
    def __init__(self, titolo, riferimenti, numero_copie = 0, alta_progressione = None):
        super().__init__()
        self.titolo = titolo
        self.__riferimenti = None
        self.__numero_copie = 0
        self.riferimenti = riferimenti
        self.numero_copie = numero_copie
        self.alta_progressione = alta_progressione

    @property
    def riferimenti(self):
        return self.__riferimenti

    @riferimenti.setter
    def riferimenti(self, value):
        if self.__riferimenti != None:
            raise RuntimeError
        else:
            self.__riferimenti = MyDict()
            for x, z in enumerate(value):
                self.__riferimenti.update({x : z})

    @property
    def numero_copie(self):
        return self.__numero_copie

    @numero_copie.setter
    def numero_copie(self, val):
        doppio = self.__numero_copie * 2
        meta = self.numero_copie/2
        if (val>=doppio):
            self.alta_progressione = True
        elif (val<meta):
            self.alta_progressione = False
        else:
            self.alta_progressione = None
        self.__numero_copie = val
        self.observers_notify(self)


# scrivere qui la classe VistaIst
class VistaIst:
    def __init__(self):
        pass

    def update(self, obj):
        if obj is not None:
            print("Cambio stato: nuove vendite del libro \"{}\" per un totale di copie vendute pari a {}\n".format(obj.titolo, obj.numero_copie))
            if obj.alta_progressione == True:
                print("Cambio stato: con l'ultimo acquisto, il libro \"{}\" ha più che raddoppiato le vendite\n".format(obj.titolo))
            elif obj.alta_progressione == False:
                print("Cambio stato: con l'ultimo acquisto, il libro \"{}\" sono aumentate meno della metà\n".format(obj.titolo))


if __name__ == "__main__":
    main()

"""Il programma deve effettuare le segueenti stampe :

La biblioteca centrale acquisisce "Java per tutti"

Cambio stato: nuove vendite del libro "Java per tutti" per un totale di copie vendite pari a 1 

Cambio stato: con l'ultimo acquisto, il libro "Java per tutti" ha piu` che raddoppiato le vendite

I riferimenti di "Java per tutti" sono [(0, 'C++')]

La libreria Faltrenella compra 199 copie di "Java per tutti"

Cambio stato: nuove vendite del libro "Java per tutti" per un totale di copie vendite pari a 200 

Cambio stato: con l'ultimo acquisto, il libro "Java per tutti" ha piu` che raddoppiato le vendite

La biblioteca centrale acquisisce "OOP fundamentals"

I riferimenti di "OOP fundamentals" sono [(0, 'Java per tutti'), (1, 'Python versus Java'), (2, 'C++')]

La libreria Faltrenella compra 100 copie di "OOP fundamentals"

Cambio stato: nuove vendite del libro "OOP fundamentals" per un totale di copie vendite pari a 100 

Cambio stato: con l'ultimo acquisto, il libro "OOP fundamentals" ha piu` che raddoppiato le vendite

La Libreria Mandetori compra 48 copie di  "OOP fundamentals"

Cambio stato: nuove vendite del libro "OOP fundamentals" per un totale di copie vendite pari a 148 

Cambio stato: con l'ultimo acquisto, le vendite di "OOP fundamentals" sono aumentate meno della meta`

Proviamo a modificare i riferimenti di libroCPiuPiu
Errore: non e` possibile modificare i riferimenti del libro

I riferimenti di "C++" sono []
"""