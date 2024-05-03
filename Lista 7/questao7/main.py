import func
lista = []
entrada = input("Digite uma palavra (Se quiser terminar digite -1): ")
while entrada != '-1':
    lista.append(entrada)
    entrada = input("Digite uma palavra (Se quiser terminar digite -1): ")

print(func.tiraPrimeiraLetra(lista))
