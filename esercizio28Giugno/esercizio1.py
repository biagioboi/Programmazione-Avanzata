import functools


def coroutine(function):
    @functools.wraps(function)
    def fun(*args, **kwargs):
        coro = function(*args, **kwargs)
        next(coro)
        return coro
    return fun


def init(sequence):
    pipeline = Handler_04(Handler_59(Handler_gt9(Default_Handler())))
    for x in sequence:
        print("\n\nEseguo la richiesta: {}".format(x))
        pipeline.send(x)



@coroutine
def Handler_04(successor = None):
    while True:
        richiesta = (yield)
        first = richiesta[0]
        if 0 <= first <= 4:
            print("Richiesta {} gestita da Handler_04".format(richiesta))
        elif successor is not None:
            successor.send(richiesta)


@coroutine
def Handler_59(successor = None):
    while True:
        richiesta = (yield)
        first = richiesta[0]
        if 5 <= first <= 9:
            print("Richiesta {} gestita da Handler_59".format(richiesta))
        elif successor is not None:
            successor.send(richiesta)


@coroutine
def Handler_gt9(successor = None):
    while True:
        richiesta = (yield)
        first = richiesta[0]
        if first > 9:
            print("Messaggio da Handler_gt9: non e` stato possibile gestire la richiesta {}. Richiesta modificata".format(richiesta))
            richiesta[0] = richiesta[0] - richiesta[1]
            pipeline = Handler_04(Handler_59(Handler_gt9(Default_Handler())))
            pipeline.send(richiesta)
        elif successor is not None:
            successor.send(richiesta)


@coroutine
def Default_Handler(successor = None):
    richiesta = (yield)
    first = richiesta[0]
    if first < 0:
        print("Richiesta {} gestita da Default_Handler: non e` stato possibile gestire la richiesta {}".format(richiesta, richiesta))
    elif successor is not None:
        successor.send(richiesta)


def main():
    x = [10,2,3,4,5]
    y = [6, 7, 8]
    init([x, y])


if __name__ == "__main__":
    main()
