import time
import datetime
from esercizio28Giugno.esercizio3_IParte import Libro

def main():
    HV = VistaStorica()

    bibliotecaCentrale = Biblioteca("Biblioteca Centrale")
    libreriaMandetori = Libreria("Libreria Mandetori")
    libreriaFaltranella = Libreria("Libreria Faltranella")
    libroCPiuPiu = Libro("C++", {})
    libroJava = Libro("Java per tutti", [libroCPiuPiu])
    libroJava.observers_add(HV)
    libroPython = Libro("Python versus Java", [libroJava, libroCPiuPiu])
    libroOOP = Libro("OOP fundamentals", [libroJava, libroPython, libroCPiuPiu])
    libroOOP.observers_add(HV)

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

    print("Questa e` la storia delle vendite di \"{}\" e \"{}\": \n".format(libroOOP.titolo, libroJava.titolo))
    vendite = HV.storia()[0]
    for titolo, num, data in vendite:
        print(
            "{}: numero di copie vendute di \"{}\" e` {}\n".format(datetime.datetime.fromtimestamp(data), titolo, num))
    andamenti = HV.storia()[1]
    for evento, data in andamenti:
        print("{}: {}\n".format(datetime.datetime.fromtimestamp(data), evento))


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


# scrivere qui la classe VistaStorica
class VistaStorica:
    def __init__(self):
        self.storia_vendite = list()
        self.andamento_vendite = list()

    def update(self, obj):
        if obj is not None:
            self.storia_vendite.append((obj.titolo, obj.numero_copie, time.time()))
            if obj.alta_progressione == True:
                self.andamento_vendite.append(("Raddoppio vendite di \"{}\"".format(obj.titolo), time.time()))
            elif obj.alta_progressione == False:
                self.andamento_vendite.append(("Incremento delle vendite di \"{}\" inferiore ad un mezzo del valore precedente".format(obj.titolo), time.time()))

    def storia(self):
        return [self.storia_vendite, self.andamento_vendite]

if __name__ == "__main__":
    main()

"""Il programma deve effettuare le seguenti stampe ovviamente con orari diversi:

La biblioteca centrale acquisisce "Java per tutti"

I riferimenti di "Java per tutti" sono [(0, 'C++')]

La libreria Faltrenella compra 199 copie di "Java per tutti"

La biblioteca centrale acquisisce "OOP fundamentals"

I riferimenti di "OOP fundamentals" sono [(0, 'Java per tutti'), (1, 'Python versus Java'), (2, 'C++')]

La libreria Faltrenella compra 100 copie di "OOP fundamentals"

La Libreria Mandetori compra 48 copie di  "OOP fundamentals"

Proviamo a modificare i riferimenti di libroCPiuPiu
Errore: non e` possibile modificare i riferimenti del libro

Questa e` la storia delle vendite di "OOP fundamentals" e "Java per tutti": 

2019-06-28 07:48:13.415401: numero di copie vendute di "Java per tutti" e` 1

2019-06-28 07:48:13.550107: numero di copie vendute di "Java per tutti" e` 200

2019-06-28 07:48:13.749610: numero di copie vendute di "OOP fundamentals" e` 100

2019-06-28 07:48:13.815696: numero di copie vendute di "OOP fundamentals" e` 148

2019-06-28 07:48:13.415411: Raddoppio vendite di "Java per tutti"

2019-06-28 07:48:13.550115: Raddoppio vendite di "Java per tutti"

2019-06-28 07:48:13.749621: Raddoppio vendite di "OOP fundamentals"

2019-06-28 07:48:13.815706: Incremento delle vendite di "OOP fundamentals" inferiore ad un mezzo del valore precedente

"""