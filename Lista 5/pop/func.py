
def o_papa_e_pop(lista,posicao_elemento_tirar):
    nova_lista = []
    valor_retirado = 0
    lista_reserva = lista[:]
    if posicao_elemento_tirar == '' :
        valor_retirado = lista_reserva[len(lista) - 1]
        nova_lista = lista_reserva[:-1]
    else:
        posicao_elemento_tirar = int(posicao_elemento_tirar)
        for i in range(len(lista_reserva)):
            if i == posicao_elemento_tirar:
                nova_lista = lista_reserva[:i]
                valor_retirado = lista_reserva[i]
                for i in lista_reserva[i+1:]:
                    nova_lista.append(i)
    return nova_lista,valor_retirado