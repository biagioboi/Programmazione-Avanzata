import collections
import copy
import datetime
import itertools
import time


class HistoryView:
    def __init__(self):
        self.data = list()

    def update(self, ob):
        self.data.append((copy.copy(ob.grades), ob.english_r, time.time()))


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

    def __init__(self,  total_cfu = 0, english_r = False):
        super().__init__()
        self._total_cfu = total_cfu
        self.english_r = english_r
        self.grades = {}

    def add_grade(self, exam, voto):
        nome = exam.name
        cfu = exam.cfu
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

Exam = collections.namedtuple("Exam", "name cfu")
historyView = HistoryView()
liveView = LiveView()
student = LaureaT_Student(0)
student.observers_add(historyView, liveView)
print("Lo studente sta per superare analisi matematica")
student.add_grade(Exam("analisi matematica", 9), 28)
print("Lo studente sta per superare asistemi operativi")
student.add_grade(Exam("sistemi operativi", 6), 20)
print("Lo studente sta per superare la prova di Inglese")
student.english_r = True

for grades, flag, timestamp in historyView.data:
    print("Esami: {}, Inglese: {}, Data: {}".format(grades," " if flag == None else "superato" if flag else "non superato", datetime.datetime.fromtimestamp(timestamp)))



"""Il programma stampa:

Lo studente sta per superare analisi matematica
Cambio stato: lo studente ha superato un nuovo esame
Cambio stato: il numero di CFU e` :  9 

Lo studente sta per superare asistemi operativi
Cambio stato: lo studente ha superato un nuovo esame
Cambio stato: il numero di CFU e` :  15 

Lo studente sta per superare la prova di Inglese
Cambio stato: lo studente ha appena superato la prova di Inglese

Esami: {}, Inglese: non superato, Data: 2019-12-10 10:54:41.413786
Esami: {'analisi matematica': 28}, Inglese: non superato, Data: 2019-12-10 10:54:41.474924
Esami: {'analisi matematica': 28}, Inglese: non superato, Data: 2019-12-10 10:54:41.658306
Esami: {'analisi matematica': 28, 'sistemi operativi': 20}, Inglese: non superato, Data: 2019-12-10 10:54:41.707940
Esami: {'analisi matematica': 28, 'sistemi operativi': 20}, Inglese: non superato, Data: 2019-12-10 10:54:41.908861
Esami: {'analisi matematica': 28, 'sistemi operativi': 20}, Inglese: superato, Data: 2019-12-10 10:54:41.959334

"""