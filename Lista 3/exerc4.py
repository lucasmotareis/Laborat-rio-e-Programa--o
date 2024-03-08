from func4 import *


menu()
escolha_usuario = int(input("Escolha um item: "))
while escolha_usuario != 4 :
    while escolha_usuario <= 0 or escolha_usuario >=5:
        escolha_usuario = int(input("Digite uma opção válida: "))
    if escolha_usuario  == 1:
        if podeVotar() == True :
            print("Pode votar!")
        else:
            print("Não pode votar!")
    elif escolha_usuario == 2:
        print(f"Você é um(a) {categoriaUsuario()}")

    elif escolha_usuario == 3:
        if podeAlistar() == True:
            print("Você pode se alistar!")
        else:
            print("Você não pode se alistar!")
    menu()
    escolha_usuario = int(input("Escolha um item: "))
