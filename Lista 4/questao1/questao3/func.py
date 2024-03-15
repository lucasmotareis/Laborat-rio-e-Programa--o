def ordenaAlfabetica(lista1,lista2): 
    new_list = []
    menor_lista = lista1 if len(lista1) < len(lista2) else lista2
    maior_lista = lista1 if len(lista1) > len(lista2) else lista2
    for i in range(len(menor_lista)):
        new_list.append(lista1[i])
        new_list.append(lista2[i])
    new_list.extend(maior_lista[i+1:])
    return new_list



# new_list.extend(lista2[i+1:])


# print (new_list)
