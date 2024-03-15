from func import *

lista = []
entrada_lista = input("Digite um número real para ser adicionada na lista (Digite 'sair' se quiser finalizar): ")
while entrada_lista != 'sair':
    lista.append(float(entrada_lista))
    entrada_lista = input("Digite um número real para ser adicionada na lista (Digite 'sair' se quiser finalizar): ")
print(ordenaAlfabetica(lista))
