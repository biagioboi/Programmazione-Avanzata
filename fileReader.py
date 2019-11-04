def reader(file):
    try:
        fp = open(file)
        for line in fp :
            print(line)
    except FileNotFoundError:
        print("Il file non è stato trovato")

# reader("prova.txt")

def decoratore(function):
    def wrapper(*args, **kwargs):
        if 'y' in kwargs:
            print(kwargs['y'])
        return function(**kwargs)
    return wrapper

@decoratore
def prova(x = 0, y = 3):
    print(x)


prova(5, y = 10)