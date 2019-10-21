
def trasformaInteri(function):
    return lambda *args : function(*(int(x) for x in args[0]))

@trasformaInteri
def somma(*numeri, somma = 0):
    for x in numeri:
        somma += x
    return somma

print(somma([5, 6, "80"]))
