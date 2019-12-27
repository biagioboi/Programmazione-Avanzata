import itertools

class BookingObserver:
    def __init__(self):
        self.old_state = None

    def update(self, ob):
        if ob is not None:
            if self.old_state is not ob.prenotabile and ob.prenotabile is False:
                self.old_state = ob.prenotabile
                print("E' stata aggiunta una nuova prenotazione.")

class PriceObserver:
    def __init__(self):
        self.old_state = None

    def update(self, ob):
        if ob is not None:
            if self.old_state is not ob.prezzo:
                self.old_state = ob.prezzo
                print("Il prezzo della camera è cambiato.")

class Observ:
    def __init__(self):
        self._observers = list()

    def observer_add(self, observer, *observers):
        for x in itertools.chain((observer,) , observers):
            self._observers.append(x)
            self.observer_notify()

    def observer_notify(self):
        for x in self._observers:
            x.update(self)

    def observer_discard(self, observer):
        self._observers.remove(observer)

class Camera(Observ):
    _status = {False: "Occupata", True: "Libera"}
    OCCUPATA, LIBERA = False, True
    def __init__(self):
        super().__init__()
        self.prenotabile = Camera.LIBERA
        self._prenotabile = True
        self.prezzo = None

    @property
    def prezzo(self):
        return self._prezzo

    @prezzo.setter
    def prezzo(self, value):
        self._prezzo = value
        self.observer_notify()

    @property
    def prenotabile(self):
        if self.libera != self._libera:
            return Camera.LIBERA
        else:
            return Camera.OCCUPATA

    @prenotabile.setter
    def prenotabile(self, value):
        if value == Camera.LIBERA:
            self.occupa = self._occupa
            self.libera = lambda *args : print("Non è possibile liberare una camera già libera.")
            self.observer_notify()
        else:
            self.occupa = lambda *args : print("Non è possibile occupare una camera occupata.")
            self.libera = self._libera
            self.observer_notify()

    def _libera(self):
        self.prenotabile = Camera.LIBERA

    def _occupa(self):
        self.prenotabile = Camera.OCCUPATA

if __name__ == "__main__":
    vista_mare = Camera()
    one = BookingObserver()
    two = PriceObserver()
    vista_mare.observer_add(one, two)
    vista_mare.prezzo = 50
    vista_mare.libera()
    vista_mare.occupa()