import func3

dicionario = {'hello':'olá','kiss':'beijo','love': 'amor', 'car': 'carro'}

entrada_ingles = input("Digite a palavra que deseja traduzir\nEntrada:")
saida_portugues = func3.pegarTraducao(dicionario,entrada_ingles)
if saida_portugues == None:
    print('Palavra ainda não cadastrada!')
else: 
    print(f"Saída: {saida_portugues}")
