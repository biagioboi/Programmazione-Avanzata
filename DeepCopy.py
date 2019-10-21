#scrivere una funzione ricorsia MyDeepCopy che prende in input una lista che potrebbe contenere al
#suo interno elementi di tipo lista che a loro volta prtrvvero contenere elementi di ripo lista, e così via. La funzione
#restituisce la deep copy della lista

def myDeepCopy(lista):
    if lista == None:
        return None
    if len(lista) == 0:
        return lista
    l = []
    for el in lista:
        if isinstance(el, list):
            l.append(myDeepCopy(el))
        else:
            l.append(el)
    return l

if __name__ == '__main__':
    listabrutta = [[5,6, [7, 8]], [3, 4], 5]
    listabella = myDeepCopy(listabrutta)
    if listabrutta == listabella: print("Inizialmente sono uguali")
    listabella[0] = 10
    print(listabrutta)
    print(listabella)