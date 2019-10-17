def fattorial_special_number(L):
    if len(L) == 1:
        return L
    if len(L) == 2:
        [x, y] = L
        return ([[x,y], [y,x]])
    else:
        s = L
        L = fattorial_special_number(L[:-1])
        toReturn = list()
        for lista in L:
            for i in range(0, len(lista)+1):
                a = lista[:]
                a.insert(i, s[len(s)-1])
                toReturn.append(a)
        return toReturn


# start of main
L = list()
reAsk = True
cont = 1
while(reAsk):
    num = input("Inserisci il {}° numero (0 per uscire): ".format(cont))
    cont+=1
    if (int(num) == 0):
        reAsk = False
    else :
        L.append(num)
print(fattorial_special_number(L))

