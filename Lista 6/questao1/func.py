def culpadoOuNao(resposta_questionario):
    soma = 0
    for resposta in resposta_questionario:
        if resposta == 'Sim' or resposta == 'sim':
            soma+=1
    if soma >=2:
        culpado = 'Suspeito'
    if soma >=3:
        culpado = 'Cúmplice'
    if soma >=5:
        culpado = 'ASSASSINO'
    return culpado


def interrogatorio(perguntas):
    resposta = []
    for pergunta in perguntas:
        resposta.append(input(pergunta))
    return culpadoOuNao(resposta)
