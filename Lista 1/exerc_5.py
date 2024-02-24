import random
numero_aleatorio = random.randint(0,100)
continuar = 's'
while continuar == 's':
    numero = int(input("Digite um número de 0 a 100: "))
    if numero != numero_aleatorio:
        print("Você errou!\n")
print("Parabéns você acertou!!")