from func2 import *


cardapio = [['Cachorro-quente',5.00],
['X-Salada', 10.00],
['X-Bacon', 12.00],
['Bauru', 8.00],
['Refrigerante', 4.00],
['Suco', 6.00]]

valor_total = 0
fechar_pedido = 'n'
while fechar_pedido == 'n':
    menuCardapio()
    codigo_produto = int(input("Digite o código do produto desejado: "))
    while codigo_produto >= 6 or codigo_produto < 1: 
        codigo_produto = int(input("Produto inválido, digite um código existente:"))
    produto_quantidade= int(input("Digite a quantidade do produto: "))
    produto_preco_total = precoTotal(cardapio[codigo_produto-1][1], produto_quantidade)
    valor_total += produto_preco_total
    print(f"{cardapio[codigo_produto-1][0]} - {produto_preco_total}")
    fechar_pedido = input("Deseja fechar o pedido? SIM(s) ou NÃO(n): ")
print(f"O Valor Total da conta foi de R${valor_total}.")
