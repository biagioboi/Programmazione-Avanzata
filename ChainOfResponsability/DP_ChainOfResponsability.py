def main():
    handler = TimerHandler(KeyHandler(MouseHandler()))
    gen = Event.next()
    while True:
        event = next(gen)
        if event.kind == Event.TERMINATE:
            break
        handler.handle(event)

class Event:
    MOUSE = "MOUSE"
    KEYPRESS = "KEYPRESS"
    TIMER = "TIMER"
    TERMINATE = "TERMINATE"
    TimerId = 0

    def __init__(self, kind, **kwargs):
        self.kind = kind
        self.kwargs = kwargs


    def __str__(self):
        if self.kind == Event.MOUSE:
            return "Button {} ({}, {})".format(
                    self.kwargs.get("button", 1), self.kwargs.get("x", -1),
                    self.kwargs.get("y", -1))
        elif self.kind == Event.KEYPRESS:
            return "Key {}{}{}".format(
                    "Ctrl+" if self.kwargs.get("ctrl", False) else "",
                    "Shift+" if self.kwargs.get("shift", False) else "",
                    self.kwargs.get("key", ""))
        elif self.kind == Event.TIMER:
            return "Timer {}".format(self.kwargs.get("id", -1))
        elif self.kind == Event.TERMINATE:
            return "Terminate"

    @staticmethod
    def next():
        prova = [Event.KEYPRESS, Event.MOUSE, Event.MOUSE, Event.TIMER, Event.KEYPRESS, Event.TERMINATE]
        for x in prova:
            y = Event(x)
            yield y


# La classe NullHandler sarà quella che verrà estesa da tutte gli altri Handler, così che se uno degli Handler
# dopo aver deciso se gestire o meno l'evento, potrà inoltrare l'evento all'Handler successivo se esiste oppure lanciare un'eccezione
# se non ci sono Handler successivi
class NullHandler:
    def __init__(self, successor = None):
        self.__successor = successor

    # se è definito il successore, l'evento viene inoltrato ad esso
    def handle(self, event):
        if self.__successor is not None:
            self.__successor.handle(event)

# un esempio di Handler della catena è MouseHandler, andiamo a definire solo il metodo di handle
# è ovvio che se il tipo di evento ricevuto è uguale a quelli supportati dall'Handler allora svolge qualche azione
# altrimenti invoca lo stesso metodo del padre, che controlla se ci sono eventi successivi nella catena al fine di inoltrare l'evento
# descriviamo giù altri tipi di Handler basati sempre sulla stessa logica
class MouseHandler(NullHandler):
    def handle(self, event):
        if event.kind == Event.MOUSE:
            print("Click {}".format(event))
        else:
            super().handle(event)

class KeyHandler(NullHandler):

    def handle(self, event):
        if event.kind == Event.KEYPRESS:
            print("Press: {}".format(event))
        else:
            super().handle(event)

class TimerHandler(NullHandler):

    def handle(self, event):
        if event.kind == Event.TIMER:
            print("Timeout: {}".format(event))
        else:
            super().handle(event)


if __name__ == "__main__":
    main()


