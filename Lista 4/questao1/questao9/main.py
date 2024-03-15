from func import *

lista = []
i=0
entrada_lista = input("Digite um número Inteiro, se quiser sair digite 'sair': ")
while entrada_lista != 'sair':
    lista.append(int(entrada_lista))
    entrada_lista = input("Digite um número Inteiro, se quiser sair digite 'sair': ")


print(retiraPrimeiroeUltimo(lista))
