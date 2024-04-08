from func import *

lista_final = []
lista = input("Digite uma lista de valores (Para interromper digite 'sair'): ")
while lista != 'sair':
    lista_final.append(lista)
    lista = input("Digite uma lista de valores (Para interromper digite 'sair'): ")


repeteOuNao = input("Digite um valor para ver se é repetido na lista: ")

print(contar(lista_final,repeteOuNao))