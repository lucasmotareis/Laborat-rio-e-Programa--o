def menuCardapio():
    return print(f'''-----Cardápio-----
    1- Cachorro-quente - R$ 5.0
    2- X-Salada - R$ 10.0
    3- X-Bacon - R$ 12.0
    4- Bauru - R$ 8.0
    5- Refrigerante - R$ 4.0
    6- Suco - R$ 6.0''')

def precoTotal(preco_cardapio, qtd_produto):
    return preco_cardapio * qtd_produto