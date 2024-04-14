def valorTotalASerGasto(lista_colaboradores):
    lista_colaboradores = lista_colaboradores[:]
    soma = 0
    for i in range(len(lista_colaboradores)):
        soma += lista_colaboradores[i][1] + lista_colaboradores[i][2]
    return soma


def numFuncionariosLascados(lista_colaboradores):
    lista_colaboradores = lista_colaboradores[:]
    num = 0
    for i in lista_colaboradores:
        if i[2] == 100:
            num +=1
    return num

def maiorAbono(lista_colaboradores):
    lista_colaboradores = lista_colaboradores[:]
    maior_abono = 0
    nome_maior_abono = ''
    for i in lista_colaboradores:
        if i[2] > maior_abono:
            maior_abono = i[2]
            nome_maior_abono = i[1]
    return nome_maior_abono,maior_abono

def mediaAbono(lista_colaboradores):
    lista_colaboradores = lista_colaboradores[:]
    qtd_colaboradores = len(lista_colaboradores)
    soma_abono = 0
    for i in lista_colaboradores:
        soma_abono += i[2]
    return soma_abono/qtd_colaboradores

def colaboradoresAbonoAcimaMedia(lista_colaboradores):
    lista_colaboradores = lista_colaboradores[:]
    media_abono = mediaAbono(lista_colaboradores)
    qtd_acima_media = 0
    for i in lista_colaboradores:
        if i[2] > media_abono:
            qtd_acima_media +=1
    return qtd_acima_media

def somaSalario(lista_colaboradores):
    lista_colaboradores = lista_colaboradores[:]
    soma = 0
    for i in lista_colaboradores:
        soma += i[1] 
    return soma

def somaAbono(lista_colaboradores):
    lista_colaboradores = lista_colaboradores[:]
    soma = 0
    for i in lista_colaboradores:
        soma += i[2] 
    return soma