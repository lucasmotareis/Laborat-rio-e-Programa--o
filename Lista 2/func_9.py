def funcaoIMC (altura,sexo):
    if sexo == 'M':
        imc_ideal = 72.7*altura-58
    elif sexo == 'F':
        imc_ideal = 62.1*altura-44.7
    else:
        print("Escolha um sexo válido!")
        return False
    return imc_ideal

sexo = input("Digite seu sexo, Masculino (M) ou  Feminino (F): ")
altura = float(input("Digite sua altura, Ex: 1.92: "))
print(f"Seu peso ideal é {funcaoIMC(altura,sexo)}")
