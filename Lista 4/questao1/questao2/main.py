from func import *

lista = []
entrada_lista = input("Digite uma palavra para ser adicionada na lista (Digite 'sair' se quiser finalizar): ")
while entrada_lista != 'sair':
    lista.append(entrada_lista)
    entrada_lista = input("Digite uma palavra para ser adicionada na lista (Digite 'sair' se quiser finalizar): ")
print(ordenaAlfabetica(lista))
