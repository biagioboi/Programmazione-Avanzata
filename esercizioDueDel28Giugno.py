from functools import wraps


def decoratore(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        nuoviArgs = []
        for x in args:
            try:
                y = int(x)
                nuoviArgs.append(y)
            except ValueError:
                print("L'argomento {} non puo' essere convertito".format(x))
                continue
        return function(*nuoviArgs, **kwargs)
    return wrapper

@decoratore
def prova(*args):
    print(*args)


prova(5, 6, "cdscd")
