def contar(lista, elemento):
    qtd = 0
    for i in range(len(lista)):
        if elemento == lista[i]:
            qtd+=1
    return qtd