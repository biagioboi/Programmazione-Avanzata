import collections
import itertools


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

    def __init__(self, total_cfu = 0, grades = {}):
        self.total_cfu = total_cfu
        self._english_r = None
        self.grades = grades

    def add_grades(self, exam, voto):
        nome = exam.Exam
        cfu = exam.name_cfu
        if (nome == "inglese"):
            self.english_r = True

    @property
    def english_r(self):
        return self._english_r

    @english_r.setter
    def enflish_r(self, value):
        pass


Exam = collections.namedtuple("Exam", "name_cfu")



