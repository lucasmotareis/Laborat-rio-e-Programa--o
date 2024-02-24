def imprimaNumero(num):
    if num >= 0:
        x = f"O valor {num} informado é positivo"
    else:
        x= f"O valor {num} informado é negativo"
    return x

numero = int(input("Digite um número: "))
print (imprimaNumero(numero))
