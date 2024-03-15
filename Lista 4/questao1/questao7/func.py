def numeroMaisAltoDasListas(lista):
    maior_valor_geral = 0
    new_list = lista[:]
    for i in range(len(new_list)):
        maior_valor_lista = 0
        new_list[i].sort()
        new_list[i].reverse()
        if new_list[i][0] > maior_valor_geral:
            maior_valor_geral = new_list[i][0]
    return [new_list[i][0] for i in range(len(new_list))],maior_valor_geral

