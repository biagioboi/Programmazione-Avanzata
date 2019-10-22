#funzione generatrice che prende in input n e restituisce un iteratore degli interi 0..1..3..6.. l'iesimo elemento scandito dell'iteratore è (0+1+...+i-1)

def generatore(n, somma = 0):
    for i in range(0, n):
        somma+=i
        yield somma

for x in generatore(10):
    print(x)