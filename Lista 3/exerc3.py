from func3 import *

prefeitura_total_gasto = 0
maior_valor_B = 0
indenizacao_minima = float(input("Digite o valor da indenização mínima: "))
casa_metragem = float(input("Digite os m² da casa: "))
while casa_metragem != 0:
    casa_classe = input("Digite se a casa é classe A ou B: ")
    valor_indenizacao = valorIndenizacao(casa_classe, casa_metragem, indenizacao_minima)
    if casa_classe == 'B' and maior_valor_B<valor_indenizacao:
        maior_valor_B = valor_indenizacao
    prefeitura_total_gasto += valor_indenizacao
    print(f"O valor total da indenização foi de R${valor_indenizacao:.2f}")
    casa_metragem = float(input("Digite os m² da casa: "))
print(f"O valor total gasto pela prefeitura com indenizações foi de R${prefeitura_total_gasto:.2f}")
print(f"A maior indenização paga para um casa classe B foi de R${maior_valor_B:.2f}")