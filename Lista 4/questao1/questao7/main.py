from func import *

lista = []
i=0
entrada_lista_aninhada = input("Deseja fazer uma lista aninhada? ")
while entrada_lista_aninhada != 'sair':
    entrada_lista = input("Digite um número real para ser adicionada na lista (Digite 'sair' se quiser finalizar): ")
    new_list = []
    while entrada_lista != 'sair':
        new_list.append(int(entrada_lista))
        entrada_lista = input("Digite um número real para ser adicionada na lista (Digite 'sair' se quiser finalizar): ")
    lista.append(new_list)
    entrada_lista_aninhada = input("Deseja fazer uma lista aninhada? Sim(s) ou Sair(sair): ")


print(numeroMaisAltoDasListas(lista))
