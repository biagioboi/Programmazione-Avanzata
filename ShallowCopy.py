def myShallowCopy(ls):
    if (len(ls) == 0): return []
    return [ls[0]] + myShallowCopy(ls[1:len(ls)])

lista = [3, 4, 5]
print(lista, myShallowCopy(lista))