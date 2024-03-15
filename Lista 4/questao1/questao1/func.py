def ordenaCaracter(lista): 
    new_list = []
    for i in range(len(lista)):
        lista[i] = [len(lista[i]),lista[i]]
    lista.sort()
    new_list = [lista[i][1] for i in range(len(lista))]
    return new_list

