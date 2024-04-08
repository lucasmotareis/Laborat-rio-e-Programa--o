
def indexou(lista,valor_ocorrencia_posicao):
    nova_lista = []
    primeira_ocorrencia_posicao = 'Não existe esse valor na lista'
    lista_reserva = lista[:]
    for i in range(len(lista_reserva)):
        if lista_reserva[i] == valor_ocorrencia_posicao:
            primeira_ocorrencia_posicao = i
    return primeira_ocorrencia_posicao