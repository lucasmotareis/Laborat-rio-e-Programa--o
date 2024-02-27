def retornaSinal(num):
    if num % 2 == 0:
        x = 'Par'
    else:
        x= 'Ímpar'
    return x

numero = int(input("Digite um número: "))
print (f"O valor é {retornaSinal(numero)}")
 