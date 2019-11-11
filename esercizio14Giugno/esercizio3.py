class Bambino:

    ISCRITTO, ALSECONDOANNO, ALTERZOANNO, DIPLOMATO = ("iscritto", "alSecondoAnno", "alTerzoAnno", "diplomato")

    def __init__(self):
        self.state = Bambino.ISCRITTO

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        if (value == Bambino.ISCRITTO):
            self.__state = Bambino.ISCRITTO
            self.success = Bambino.ALSECONDOANNO
            self.salto = Bambino.ALTERZOANNO
            self.preced = "e` appena stato iscritto al I anno e non puo` tornare in uno stato precedente"
        elif (value == Bambino.ALSECONDOANNO):
            self.__state = Bambino.ALSECONDOANNO
            self.success = Bambino.ALTERZOANNO
            self.salto = Bambino.DIPLOMATO
            self.preced = Bambino.ISCRITTO
        elif(value == Bambino.ALTERZOANNO):
            self.__state = Bambino.ALTERZOANNO
            self.success = Bambino.DIPLOMATO
            self.salto = "e` nello stato alTerzoAnno  e non puo` saltare un anno"
            self.preced = Bambino.ALSECONDOANNO
        elif(value == Bambino.DIPLOMATO):
            self.__state = Bambino.DIPLOMATO
            self.success = "si e` gia` diplomato e non puo` avanzare in uno stato successivo"
            self.preced = Bambino.ALTERZOANNO
            self.salto = "si e` gia` diplomato e non puo` avanzare in uno stato successivo"
        else:
            print("il bambino " + str(value))


    def stampaStato(self):
        print("il bambino è " + str(self.state))
    def pred(self):
        self.state = self.preced
    def succ(self):
        self.state = self.success
    def salta_anno(self):
        self.state = self.salto

def main():
    bambino =Bambino()
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