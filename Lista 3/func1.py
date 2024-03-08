def viagemLucro(qtd_passageiros, valor_passagem, despesa_viagem):
    viagem_lucro = (qtd_passageiros*valor_passagem)-despesa_viagem
    if viagem_lucro > 0:
        lucro = "Houve lucro!"
    elif viagem_lucro < 0:
        lucro = "Houve prejúizo!"
    else:
        lucro = "A viagem se pagou!"
    return lucro

def viagensOnibusA(tipo_onibus):
    if tipo_onibus == 'A':
        return 1
    else:
        return 0
    
def viagensOnibusB(tipo_onibus,data_viagem):
    if tipo_onibus == 'B' and data_viagem == '23/12/22':
        return 1
    else:
        return 0
    
def onibusCampeao (qtd_passageiros,passageiro_campeao):
    if qtd_passageiros > passageiro_campeao:
        return True