
def reverter(lista):
    nova_lista = []
    lista_copia = lista[:]
    for i in range(len(lista_copia)):
        nova_lista.append(lista_copia[-i-1])
    return nova_lista