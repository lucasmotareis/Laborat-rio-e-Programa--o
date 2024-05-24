def contarObjetos(dicionario,objeto):
    if dicionario.get(objeto,False) == False:
        dicionario.update({objeto:{'quantidade': 1 }})
    else:
        quantidade_antiga = dicionario[objeto]['quantidade']
        dicionario[objeto] = {'quantidade': quantidade_antiga+1 }


def contarTotalObjetos(dicionario):
    cont = 0
    for objeto,quantidade_objeto in dicionario.items():
        cont += int(quantidade_objeto['quantidade'])
    return cont