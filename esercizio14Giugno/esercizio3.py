class Bambino:
    _status = {0: "ISCRITTO", 1: "ALSECONDOANNO", 2: "ALTERZOANNO", 3: "DIPLOMATO"}
    ISCRITTO, ALSECONDOANNO, ALTERZOANNO, DIPLOMATO = range(0, 4)

    def __init__(self):
        self._state = 0
        self.state = Bambino.ISCRITTO

    @property
    def state(self):
        if self._pred != self.pred:
            return Bambino.ISCRITTO
        elif self._salta_anno == self.salta_anno and self._pred == self.pred:
            return Bambino.ALSECONDOANNO
        elif self._salta_anno != self.salta_anno:
            return Bambino.ALTERZOANNO
        else:
            return Bambino.DIPLOMATO

    @state.setter
    def state(self, value):
        if value == Bambino.ISCRITTO:
            self.succ = self._succ
            self.pred = lambda *args: print("Il bambino  e` appena stato iscritto al I anno e non puo` tornare in uno stato precedente")
            self.salta_anno = Bambino._salta_anno
        elif value == Bambino.ALSECONDOANNO:
            self.succ = self._succ
            self.pred = self._pred
            self.salta_anno = self._salta_anno
        elif value == Bambino.ALTERZOANNO:
            self.succ = self._succ
            self.pred = self._pred
            self.salta_anno = lambda *args: print("Il bambino e` nello stato alTerzoAnno  e non puo` saltare un anno")
        elif value == Bambino.DIPLOMATO:
            self.succ = lambda *args: print("Il bambino  si e` gia` diplomato e non puo` avanzare in uno stato successivo")
            self.pred = self._pred
            self.salta_anno = lambda *args: print("Il bambino  si e` gia` diplomato e non puo` saltare un anno")

    def stampaStato(self):
        print("il bambino è nello stato " + str(self._status[self.state]))

    def _pred(self):
        self.state -=1

    def _succ(self):
        self.state +=1

    def _salta_anno(self):
        self.state +=2


def main():
    bambino = Bambino()
    bambino.stampaStato()
    bambino.pred()
    bambino.succ()
    bambino.stampaStato()
    bambino.succ()
    bambino.stampaStato()
    bambino.salta_anno()
    bambino.succ()
    bambino.stampaStato()
    bambino.succ()


if __name__ == "__main__":
    main()

"""IL programma deve stampare:

Il bambino e` nello stato  iscritto
Il bambino  e` appena stato iscritto al I anno e non puo` tornare in uno stato precedente
Il bambino e` nello stato  alSecondoAnno
Il bambino e` nello stato  alTerzoAnno
Il bambino e` nello stato alTerzoAnno  e non puo` saltare un anno
Il bambino e` nello stato  diplomato
Il bambino  si e` gia` diplomato e non puo` avanzare in uno stato successivo
"""