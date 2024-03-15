from func import *

lista = []
i=0
entrada_lista_aninhada = input("Deseja fazer uma lista aninhada? Sim(sim) ou Não(sair)")
while entrada_lista_aninhada != 'sair':
    new_list = []
    for i in range(3):
        entrada_lista = input("Digite um número real para ser adicionada na lista: ")
        new_list.append(int(entrada_lista))
    lista.append(new_list)
    entrada_lista_aninhada = input("Deseja fazer uma lista aninhada? Sim(s) ou Sair(sair): ")


print(mediaListas(lista))
