from func import *

lista = []
i=0
entrada_lista = input("Digite algo para adicionar à lista: ")
while entrada_lista != 'sair':
    lista.append(entrada_lista)
    entrada_lista = input("Digite algo para adicionar à lista, se quiser sair digite 'sair': ")


print(repeteOuNao(lista))
