from func import *
print("Enquete\nQuem foi o Melhor Jogador?")

lista_votacao_jogadores=[]
numero_jogador = int(input("Digite o número do jogador (0=fim): "))
while numero_jogador != 0:
    if numero_jogador > 23 or numero_jogador < 0:
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
    else:
        lista_votacao_jogadores.append(numero_jogador)
    numero_jogador = int(input("Digite o número do jogador (0=fim): "))

(lista_votacao_resultado,total_votacao) = (computaVotos(lista_votacao_jogadores))

print(lista_votacao_resultado)
print(f'''
Resultado da votação:
Foram computados {total_votacao} votos.
Jogador Votos %''')
for i in range(len(lista_votacao_resultado)):
    print (f"{lista_votacao_resultado[i][1]}        {lista_votacao_resultado[i][0]}        {(lista_votacao_resultado[i][0]/total_votacao)*100:.2f}%")
print(f"\nO melhor jogador foi o número {lista_votacao_resultado[0][1]}, com {lista_votacao_resultado[0][0]} votos, correspondendo a {(lista_votacao_resultado[0][0]/total_votacao)*100:.2f}% do total de votos.")


