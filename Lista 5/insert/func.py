def inserir(lista,elemento, posicao):
    nova_lista = []
    for i in range(len(lista)):
        if i == posicao:
            nova_lista = lista[:i]
            nova_lista.append(elemento)
            for i in lista[i:]:
                nova_lista.append(i)
            # nova_lista.append(lista[i:])


    return nova_lista