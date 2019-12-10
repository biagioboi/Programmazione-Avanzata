# scrivere una classe FW_factory che produce istanze di oggetti FW che condividono parte dello stato con altri oggetti
# fw_factory ha un metodo get_fw che prende in input uno stato condiviso sotto forma di lista e restituisce un obj FW per quello stato
# se già esiste, oppure ne crea uno nuovo; oltre all'obj restituisce un metodo list_fws che stampa prima il numero di oggetti FW creati fino
# a quel momento e poi stampa gli stati relativi agli oggetti FW creati.
# la classe fw ha un costruttore che prende in input lo stato condiviso e lo assegna ad una variabile d'istanza, shared_state dell'oggetto creato
# inoltre fw ha un metodo op(self, itsownstate: list, tipo: type, file) che crea un'istanza di tipo con stato formato dalla concetenzaione
# delle liste shared_State e itsownstate. il metodo aggiunge al file una linea che contiene lo stato dell'oggetto creato e stampa il suddetto stato restituendolo poi in output.

class FW():

    # FW memorizza la parte comune dello stato in SharedState
    __slots__ = ["sharedState"]
    def __init__(self, sharedState: list):
        self.sharedState = sharedState

    """op aggiunge un oggetto oggetto al file  prendendo tutta la parte condivisa dell'auto da sharedState e il resto dal
    parametro itsOwnState"""

    def op(self, itsOwnState: list, tipo: type, file):
        pass


class FWFactory():

    factory = dict()

    """
    Questa classe crea oggetti FW: ne crea uno nuovo se non esiste, altrimenti resituisce uno preesistente

    """
    def __init__(self, shared_state: list):
        for lista in shared_state:
            index = ""
            for y in lista:
                index = index + y
            if index not in FWFactory.factory:
                x = FW(lista)
                FWFactory.factory.update({index : x})



    def get_FW(self, shared_state: list) -> FW:
        """
        restituisce un FW con un certo stato o ne crea uno nuovo
        """
        index = ""
        for y in shared_state:
            index = index + y
        if index in FWFactory.factory:
            print("FWFactory:  uso un FW esistente.")
            return FWFactory.factory.get(index)
        else:
            print("FWFactory: non trovo un FW, ne creo uno nuovo.")
            x = FW(shared_state)
            FWFactory.factory.update({index : x})
            return x


    def list_FWs(self):
        """ stampa numero oggetti FW's e gli stati degli FW's"""
        print("Sono presenti {} oggetti di tipo FW.".format(len(FWFactory.factory)))
        for x in FWFactory.factory.values():
            print(x.sharedState[1] + "_" + x.sharedState[0] + "_" + x.sharedState[2])


class automobile:
    def __init__(self, state: list):
        self._state = state

    def state(self): return self._state


def add_car(factory: FWFactory, targa: str, proprietario: str, marca: str, modello: str, colore: str):
    print("\n\nClient: Aggiungo un automobile.")
    fw = factory.get_FW([marca, modello, colore])

    fw.op([targa, proprietario], automobile, "automobili.txt")


if __name__ == "__main__":
    """
    The client code usually creates a bunch of pre-populated flyweights in the
    initialization stage of the application.
    """

    factory = FWFactory([
        ["Chevrolet", "Camaro2018", "rosa"],
        ["Mercedes Benz", "C300", "nera"],
        ["Mercedes Benz", "C500", "rossa"],
        ["BMW", "M5", "rossa"],
        ["BMW", "X6", "bianca"],
    ])

    factory.list_FWs()

    add_car(
        factory, "DE123AT", "Bob Bab", "BMW", "M5", "rossa")

    add_car(
        factory, "AR324SD", "Mike Smith", "BMW", "X1", "rossa")

    print("\n")

    factory.list_FWs()

"""Il programma stampa :

FWFactory: ho  5 oggetti FW: 
Camaro2018_Chevrolet_rosa
C300_Mercedes Benz_nera
C500_Mercedes Benz_rossa
BMW_M5_rossa
BMW_X6_bianca


Client: Aggiungo un automobile.
FWFactory:  uso un FW esistente.
Il nuovo oggetto di tipo <class '__main__.automobile'> e` ['BMW', 'M5', 'rossa', 'DE123AT', 'Bob Bab']:


Client: Aggiungo un automobile.
FWFactory: non trovo un FW, ne creo uno nuovo.
Il nuovo oggetto di tipo <class '__main__.automobile'> e` ['BMW', 'X1', 'rossa', 'AR324SD', 'Mike Smith']:


FWFactory: ho  6 oggetti FW: 
Camaro2018_Chevrolet_rosa
C300_Mercedes Benz_nera
C500_Mercedes Benz_rossa
BMW_M5_rossa
BMW_X6_bianca
BMW_X1_rossa

"""