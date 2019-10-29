def raddoppia():
    while True:
        x, y = yield
        print("stampa tra un yield e l'altro del corpo del while. x = ", y)
        x = yield x*2
        print("x = ", x)

g = raddoppia()
r = next(g)
r = g.send((10, 20))
print (r)
r = next(g)