# Scrivere nel file esercizio1.py una funzione generatrice myGenerator(n) che prende in input
# un intero n>=1 e restituisce un iteratore dei primi n fattoriali. In altre parole, la prima volta
# che viene invocato next viene restituito 1!, la seconda volta 2!, la terza volta 3!, e cosi` via
# fino ad n! .
# All’esercizio verra` assegnato un bonus se la funzione generatrice sara` definita
# ricorsivamente. E` possibile scrivere una funzione generatrice ricorsiva che prende in input
# piu` parametri e che poi viene opportunamente invocata da myGenerator.

def myGenerator(n):
    if (n==1):
        yield 1
    else:
        yield
        myGenerator(n-1, s)
        yield s


prova = myGenerator(5)
for x in prova:
    print(x)

