#Scrivere la funzione procTesto all’interno del file esercizio4.py.
# Se la funzione ha bisogno di invocare altre procedure, fornire anche quest’ultime.
# La funzione procTesto prende in input una lista di nomi di file, una lista di stringhe,
# e il parametro concorrenza. La funzione procTesto deve cecare nel testo dell’i-esimo file
# della prima lista l’i-esima stringa della seconda lista e deve fare cio` con un processo
# separato per ogni coppia file-stringa. Attenzione, il callable utilizzato da procTesto
# deve riceve in input il testo del file e non il file. La funzione procTesto deve inoltre
# stampare per ciascuna coppia file-stringa se la stringa e` presente o meno nel file.
# Le stampe devono avvenire nell’ordine in cui terminano i processi e al termine degli stessi.
import multiprocessing
from concurrent import futures


def procTesto(file, stringhe):
    conc = len(file)
    future_set = set()
    with futures.ThreadPoolExecutor(max_workers=conc) as executor:
        for i, x in enumerate(file):
            str = stringhe[i]
            all_str_in_file = list()
            with open(x) as fp:
                lines = fp.read().replace("\n", " ").split(" ")
                for z in lines:
                    all_str_in_file.append(z)
            fut = executor.submit(cerca_stringa, x, all_str_in_file, str)
            future_set.add(fut)
    result = wait_futures(future_set)
    for x in result:
        print(x)


def wait_futures(future_set):
    res = list()
    for x in futures.as_completed(future_set):
        res.append(x.result())
    return res


def cerca_stringa(file, stringhe_file, stringa_to_find):
    if stringa_to_find in stringhe_file:
        return "La stringa " + stringa_to_find + " e' presente nel file " + file
    return "La stringa " + stringa_to_find + " non e' presente nel file " + file



def main():
    files = ["file2", "file5", "file8", "file2", "file5", "file8"]
    stringhe = ["panca", "Trento", "entrarono", "a", "di", "capra"]
    procTesto(files, stringhe)


if __name__ == "__main__":
    main()

"""  Ecco cosa deve essere stampato:
La stringa panca e` presente nel file file2:
La stringa Trento e` presente nel file file5:
La stringa entrarono e` presente nel file file8:
La stringa a non e` presente nel file file2:
La stringa di non e` presente nel file file5:
La stringa capra non e` presente nel file file8:
"""

