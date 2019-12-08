import itertools

# classe che serve a tener traccia di tutti gli osservatori che vogliono essere notificati al cambio di stato da parte
# del modello.
import time


class Observed:

    # il costruttore inizializza un insieme vuoto, nel quale andranno a finire tutti gli osservatori
    def __init__(self):
        self.__observers = set()

    # questo metodo ci serve ad aggiungere oggetti all'insieme, in particolare andiamo a scrivere
    # observer, *observers per essere sicuri che venga passato almento un parametro e se ce n'è più di uno
    # essi verranno gestiti
    def oberservers_add(self, observer, *observers):
        # il metodo itertools.chain permette di restituire gli elementi degli iterabili passati come parametri
        # nel nostro caso però abbiamo che observer non è un iterabile e dunque andiamo a creare una pseudo lista
        # composta da observer e null e la passiamo come parametro unito ad observers; insieme ci restituiscono tutti gli elementi
        # passati come paramteri, sia che sono liste che se sono semplici elementi.
        for observer in itertools.chain((observer,), observers):
            # aggiungiamo l'elemento all'insieme degli ossevatori
            self.__observers.add(observer)
            # aggiorniamo lo stato dell'elemento appena aggiunto
            observer.update(self)

    # questo metodo ci permette di eliminare un elemento dall'insieme di osservatori
    def observer_discard(self, observer):
        self.__observers.discard(observer)

    # questo è il metodo di aggiornamento degli observers, viene invocato dal modello quando vuole notificare gli osservatori
    # del cambiamento di stato appena effettuato
    def observers_notify(self):
        for observer in self.__observers:
            observer.update(self)

# chiaramente ora gli oggetti che vogliono essere notificati dovranno avere un metodo update(), mentre il modello che vuole
# essere osservato deve estendere la classe Observed

# nel nostro esempio abbiamo un Model che notifica gli osservatori del cambiamento di valore
class Model(Observed):
    def __init__(self, value):
        super().__init__()
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if val != self.__value:
            self.__value = val
            self.observers_notify()


# infine dichiariamo un oggetto osservatore che quando verrà notificato stampa l'orario dell'aggiornamento e lo aggiunge alla lista
class History:
    def __init__(self):
        self.data = []

    def update(self, model):
        self.data.append((model.value, time.time()))


x = History() # nel nostro caso l'oggetto che fa qualcosa in seguito al cambio di stato
z = Model(50) # Il model che implementa la classe Observed e che vuole notificare Histoty
z.oberservers_add(x) # Aggiungiamo gli oggetti che vogliono essere notificati nel cambiamento di Model
print(x.data) # It works!