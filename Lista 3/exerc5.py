from func5 import *

total_pagamento_vendedores = 0
vendedor_pessimo = ''
qtd_vendidas_vendedor_pessimo = 0


salario_minimo_valor = float(input("Digite o valor do salário mínimo: "))
nome_vendedor = input("Digite o nome do vendedor: ")
while nome_vendedor != 'sair':
    qtd_camisas_vendidas = int(input("Digite a quantidade de camisetas vendidas: "))
    if qtd_vendidas_vendedor_pessimo == 0:
        qtd_vendidas_vendedor_pessimo = qtd_camisas_vendidas
    elif qtd_vendidas_vendedor_pessimo  > qtd_camisas_vendidas:
        qtd_vendidas_vendedor_pessimo = qtd_camisas_vendidas
        vendedor_pessimo = nome_vendedor
    salario_vendedor = salarioVendedor(salario_minimo_valor, qtd_camisas_vendidas)
    total_pagamento_vendedores += salario_vendedor
    classe_vendedor = classeVendedor(salario_vendedor)
    print(f"O vendedor {nome_vendedor} tem a categoria {classe_vendedor} e recebeu R${salario_vendedor}.\n")
    nome_vendedor = input("Digite o nome do vendedor: ")
print(f"O total gasto com o pagamentos dos vendedores foi de R${total_pagamento_vendedores}.")
print(f"O vendedor que menos vendeu camisetas foi {vendedor_pessimo} que vendeu apenas {qtd_vendidas_vendedor_pessimo} camisetas.")
    
