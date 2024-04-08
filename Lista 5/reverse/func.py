
def organizar(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0]
        menor_que_pivo = []
        maior_que_pivo = []
        for i in lista[1:]:
            if i <= pivo:
                menor_que_pivo.append(i)
            else:
                maior_que_pivo.append(i)
    return organizar(menor_que_pivo) + [pivo]+ organizar(maior_que_pivo)