from func import *

lista1 = []
lista2 = []
entrada_lista = input("Digite uma palavra para ser adicionada na primeira lista (Digite 'sair' se quiser finalizar): ")
while entrada_lista != 'sair':
    lista1.append(entrada_lista)
    entrada_lista = input("Digite uma palavra para ser adicionada na lista (Digite 'sair' se quiser finalizar): ")
entrada_lista = input("Digite uma palavra para ser adicionada na segunda lista (Digite 'sair' se quiser finalizar): ")
while entrada_lista != 'sair':
    lista2.append(entrada_lista)
    entrada_lista = input("Digite uma palavra para ser adicionada na lista (Digite 'sair' se quiser finalizar): ")

print(ordenaAlfabetica(lista1,lista2))
