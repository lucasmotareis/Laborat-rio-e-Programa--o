
def remover(lista,retirar_elemento):
    nova_lista = []
    lista_reserva = lista[:]
    for i in range(len(lista_reserva)):
        if lista_reserva[i] == retirar_elemento:
            nova_lista = lista_reserva[:i]
            for i in lista_reserva[i+1:]:
                nova_lista.append(i)
    return nova_lista