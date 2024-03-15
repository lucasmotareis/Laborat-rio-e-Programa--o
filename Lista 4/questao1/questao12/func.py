def repeteOuNao(lista):
    new_list = lista[:]
    for i in range(len(new_list)):
        if new_list.count(new_list[i]) > 1:
            return True
    return False

