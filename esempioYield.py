# Quando lo yield viene messo ad un assegnamento ex. x = yield allora aspetterà una send per ricevere
# il valore da assegnare a x, contestualmente potrebbe anche restituire un valore 'yield x',
# che restituisce il valore di x

def raddoppia():
    while True:
        # viene restiuito none in quanto non è specificato nulla dopo lo yield
        # allo stesso tempo si aspetta una send() per dare un valore a x
        yield
        # print("stampa tra un yield e l'altro del corpo del while. x = ", x)
        x = yield
        # se al precedente yield non è stato assegnato nulla a x, la seguente operazione
        # non è fattibile perchè None * int non si puo' fare
        x = yield x*2
        print("x = ", x)

g = raddoppia()
r = next(g)
next(g)
g.throw(TypeError)
print (r)


