# il pacco può essere odinato, spedito all'ufficio e quindi ricevuto
# vogliamo scrivere il suo stato ogni volta che esso cambia, lo stato iniziale è ordinato
# la classe Pacco ha il metodo _succ per passare allo stato successivo e _pred per passare a quello prcedente
# lo stato ordinato non ha stati che lo precedono, lo stato ricevuto non ha stati che vengono dopo

class Pacco:
    _status = {0: "ordinato", 1: "spedito", 2: "ricevuto"}
    ORDINATO, SPEDITO, RICEVUTO = range(0, 3)

    def __init__(self):
        self._state = 0
        self.state = Pacco.ORDINATO

    @property
    def state(self):
        if self.pred != self._pred:
            return Pacco.ORDINATO
        elif self.next != self._succ:
            return Pacco.RICEVUTO
        else:
            return Pacco.SPEDITO

    @state.setter
    def state(self, value):
        if value == Pacco.ORDINATO:
            self.next = self._succ
            self.pred = lambda *args : print("Non è possibile tornare indietro")
        elif value == Pacco.SPEDITO:
            self.next = self._succ
            self.pred = self._pred
        elif value == Pacco.RICEVUTO:
            self.next = lambda *args : print("Il pacco è stato già ricevuto")
            self.pred = self._pred

    def _pred(self):
        self.state -=1

    def _succ(self):
        self.state +=1

    def stampaStato(self):
        if self.next == self._succ: print("Il pacco è stato {} ma non ancora {}".format(self._status[self.state], self._status[self.state+1]))
        elif self.next != self._succ: print("Il pacco è stato {}".format(self._status[self.state]))

def main():
	print("\nCreo il pacco")
	pacco=Pacco()
	pacco.stampaStato()
	print("\nInoltro il pacco all'ufficio postale")
	pacco.next()
	pacco.stampaStato()
	print("\nConsegno il pacco al destinatario")
	pacco.next()
	pacco.stampaStato()
	print("\nProvo a passare ad uno stato successivo")
	pacco.next()
	pacco.stampaStato()

if __name__== "__main__":
	main()


"""Il  programma deve stampare:
Creo il pacco
Il pacco e` stato ordinato ma non ancora spedito

Inoltro il pacco all'ufficio postale
Il pacco e` stato spedito ma non ancora ricevuto

Consegno il pacco al destinatario
Il pacco e` stato ricevuto 

Provo a passare ad uno stato successivo
Il pacco e` gia` stato ricevuto
Il pacco e` stato ricevuto 
"""