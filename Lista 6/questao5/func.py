def computaVotos(lista_votacao_jogadores):
    total_votacao = len(lista_votacao_jogadores)
    lista_votacao_jogadores = lista_votacao_jogadores[:]
    numeros_votados_e_qtd = []
    for i in range(24):
        if i in lista_votacao_jogadores:
            numeros_votados_e_qtd.append([lista_votacao_jogadores.count(i),i])
    numeros_votados_e_qtd.sort()
    numeros_votados_e_qtd.reverse()
    return numeros_votados_e_qtd, total_votacao