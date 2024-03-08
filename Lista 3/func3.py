def valorIndenizacao(casa_classe, casa_metragem, indenizacao_minima):
    if casa_classe == 'A':
        valor_total = indenizacao_minima + (casa_metragem*500)
    elif casa_classe == 'B':
        valor_total = indenizacao_minima + (casa_metragem*300)
    return valor_total