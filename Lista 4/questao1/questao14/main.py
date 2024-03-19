from func import *
import time


i=0
numero_de_ramdons = int(input("Digite o tamanho da lista aleatória: "))
valor_desejado = int(input("Digite o valor que quer proucurar na lista: "))

lista_aleatoria = listaAleatoria(numero_de_ramdons)
#utilizar a mesma lista para que uma função não receba uma lista mais "fácil" que outra
print("Terminou a Lista Aleatoria!")

ini = time.time()
print(pesquisa_binaria(lista_aleatoria,valor_desejado))
fim = time.time()
print ("Pesquisa Binária: ",fim-ini)


ini = time.time()
print(pesquisa_lenta(lista_aleatoria,valor_desejado))
fim = time.time()
print ("Pesquisa Normal: ",fim-ini)
