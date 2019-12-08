from ChainOfResponsability.DP_ChainOfResponsability import Event
import functools

# nell'approccio con coroutine non avremo bisogno del null'handler, questo perchè tutti gli Handler saranno in realtà delle funzioni
# o meglio, delle coroutine. Una coroutine viene definita tale se all'interno ha due espressioni yield, una che prende parametri e l'altra
# che li restituisce in seguito all'elaborazione.
# è chiaro che possiamo utilizzare le coroutine in questo contesto perchè prendiamo come parametro il successore, e nella prima espressione di yield prendono l'evento
# se ci interessa (siamo noi i gestori)
# facciamo tutte le operazioni necessarie, altrimenti lo facciamo avanzare al prossimo gestore attraverso una send; sempre che esso non sia l'ultimo
# e quindi il successore non sia None

def main():
    pipeline = mouse_handler(key_handler(timer_handler()))
    gen = Event.next()
    while True:
        event = next(gen)
        if event.kind == Event.TERMINATE:
            break
        pipeline.send(event)


# in particolare l'annotazione coroutine serve per far avviare la funzione al cui interno ha una coroutine, altrimenti non potremmo farla partire
def coroutine(function):
    @functools.wraps(function)
    def newFun(*args, **kwargs):
        cor = function(*args, **kwargs)
        next(cor)
        return cor
    return newFun

@coroutine
def mouse_handler(successor = None):
    while True:
        event = (yield)
        if event.kind == Event.MOUSE:
            print("Mouse: {}".format(event))
        elif successor is not None:
            successor.send(event)

@coroutine
def key_handler(successor = None):
    while True:
        event = (yield)
        if event.kind == Event.KEYPRESS:
            print("Click Button: {}".format(event))
        elif successor is not None:
            successor.send(event)

@coroutine
def timer_handler(successor = None):
    while True:
        event = (yield)
        if event.kind == Event.TIMER:
            print("Timeout: {}".format(event))
        elif successor is not None:
            successor.send(event)

if __name__ == "__main__":
    main()
