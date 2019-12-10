import collections
import itertools
import time


class HistoryView:
    def __init__(self):
        self.history = list()

    def update(self, ob):
        if len(ob.grades) > 0:
            self.history.append((ob.grades, ob.english_r, time.time()))


class LiveView:

    def update(self, ob):
        if ob.english_r is True:
            print("Cambio stato: lo studente ha appena superato la prova di Inglese\n")
        elif ob.total_cfu > 0:
            print("Cambio stato: lo studente ha superato un nuovo esame")
            print("Cambio stato: il numero di CFU e` : ", ob.total_cfu, "\n")


class Observer:

    def __init__(self):
        self.__observers = set()

    def observers_add(self, observer, *observers):
        for observer in itertools.chain((observer, ), observers):
            self.__observers.add(observer)
            observer.update(self)

    def observer_discard(self, observer):
        self.__observers.discard(observer)

    def observers_notify(self, ob):
        for observer in self.__observers:
            observer.update(ob)

class LaureaT_Student(Observer):

    def __init__(self, english_r = False):
        super().__init__()
        self._total_cfu = 0
        self.english_r = english_r
        self.grades = {}

    def add_grades(self, exam, voto):
        nome = exam.nome_esame
        cfu = exam.name_cfu
        self.grades.update({nome: voto})
        self.total_cfu += cfu

    @property
    def total_cfu(self):
        return self._total_cfu

    @total_cfu.setter
    def total_cfu(self, value):
        self._total_cfu = value
        self.observers_notify(self)

    @property
    def english_r(self):
        return self._english_r

    @english_r.setter
    def english_r(self, value):
        self._english_r = value
        if value is True:
            self.observers_notify(self)


history = HistoryView()
live = LiveView()
laurea = LaureaT_Student()
laurea.observers_add(history, live)
Exam = collections.namedtuple("Exam", ["nome_esame", "name_cfu"])
x = Exam("Programmazione I", 9)
laurea.add_grades(x, 28)
laurea.english_r = True




