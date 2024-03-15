def estaOrdenadaouNao(lista):
    new_list = lista[:]
    new_list.sort()
    if new_list == lista:
        return True
    else:
        return False

