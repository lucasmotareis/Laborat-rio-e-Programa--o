from func1 import *
viagens_A = 0
qtd_viagens_B = 0
onibus_campeao = ''
qtd_passageiro_campeao = 0

tipo_onibus = input("Digite o seu Ônibus (A, B ou C): ")
while tipo_onibus != 'X':
    data_viagem = input("Digite a data da sua viagem (dd/mm/aa): ")
    qtd_passageiro = int(input("Digite a quantidade de passageiros: "))
    passagem_valor = float(input("Digite o valor da passagem: "))
    despesa_viagem = float(input("Digite a despesa da viagem: "))
    print(f"O Ônibus {tipo_onibus} que saiu {data_viagem}, com a quantidade de passageiros de {qtd_passageiro} pessoas,com a passagem no valor de R${passagem_valor}. {viagemLucro(qtd_passageiro,passagem_valor,despesa_viagem)} ")
    viagens_A += viagensOnibusA(tipo_onibus)
    qtd_viagens_B += viagensOnibusB(tipo_onibus, data_viagem)
    if onibusCampeao(qtd_passageiro, qtd_passageiro_campeao) == True:
        qtd_passageiro_campeao = qtd_passageiro
        onibus_campeao = tipo_onibus
    tipo_onibus = input("Digite o seu Ônibus (A,B ou C): ")
print(f"A quantidade de viagens realizadas pelo ônibus A foi de {viagens_A}.")
print(f"A quantidade de viagens realizadas pelo ônibus B no dia 23/12/22 foi de {qtd_viagens_B}.")
print(f"O ônibus que transportou mais passageiros foi o {onibus_campeao}.")


