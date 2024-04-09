def qtdValor(lista):
    return len(lista)


def imprimeNaOrdem(lista):
    return lista
    
def imprimeInverso(lista):
    lista_reversa = lista[:]
    lista_reversa.reverse()
    return lista_reversa

def somaDosValores(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

def mediaDosValores(lista):
    return somaDosValores(lista)/len(lista)


def valoresAcimaMedia(lista):
    media = mediaDosValores(lista)
    valores_acima = []
    for i in lista:
        if i > media:
            valores_acima.append(i)
    return valores_acima

def valoresAbaixoDeSete(lista):
    valor_abaixo_sete = []
    for i in lista:
        if i < 7:
            valor_abaixo_sete.append(i)
    return valor_abaixo_sete




