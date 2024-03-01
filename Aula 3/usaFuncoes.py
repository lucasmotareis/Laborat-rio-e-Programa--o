from funcoes import *
resposta = 11
while resposta != 0:
    print("*"*60)
    print("Seja bem-vindo ao programa main.py. Por favor, escolha a opção desejada:")
    print("1 - Verifica número inteiro e retorna True para positivo ou False para Negativo")
    print("2 – Verifica se um número é positivo ou negativo")
    print("3 – Verifica se um número é ímpar ou par")
    print("4 - Verifica a média de um Aluno")
    print("5 - Transforma a idade do usuário em dias")
    print("6 - Verifica uma ordem de números e coloca-os ordenados")
    print("7 - Transforma Segundos em Horas:Minutos:Segundos ")
    print("8 - Verifica se um número é perfeito ou não")
    print("9 - Verifica seu Peso Ideal")
    print("10 - Verifica o tipo de Triângulo de acordo com os Lados")
    print("0 - Verifica o tipo de Triângulo de acordo com os Lados")

    resposta = int(input("Sua opção >>>> "))
    if resposta == 1:
        numero = int(input("Digite um número: "))
        print(negativoPositivo(numero))
        print("\n")
    elif resposta == 2:
        numero = int(input("Digite um número: "))
        print (imprimaNumero(numero))
        print("\n")
    elif resposta == 3:
        numero = int(input("Digite um número: "))
        print (f"O valor é {retornaSinal(numero)}")
        print("\n")
    elif resposta == 4:
        letra = input("Digite uma letra: ")
        nota1 = float(input("Digite a Nota 1: "))
        nota2 = float(input("Digite a Nota 2: "))
        nota3 = float(input("Digite a Nota 3: "))
        print(f"A média é {mediaAritmetica(nota1,nota2,nota3,letra):.2f}!")
        print("\n")
    elif resposta == 5:
        idade_em_anos = int (input("Digite sua idade em Anos: "))
        idade_em_meses = int (input("Digite sua idade em Meses: "))
        idade_em_dias =int (input("Digite sua idade em Dias: "))
        print(f"Sua idade em Dias é {idadeEmDias(idade_em_anos,idade_em_meses,idade_em_dias)}")
        print("\n")
    elif resposta == 6:
        num=[]
        resposta = ''
        while resposta != 'nao':
            num.append(int(input("Digite um número inteiro: ")))
            resposta = input("Deseja continuar? Sim(sim) ou Não(nao)?: ")
        resultado = retornaOrdemNumeros(num)
        print(str(resultado))
        print("\n")
    elif resposta == 7:
        segundos = int(input("Digite os segundos para serem transformados: "))
        print(converterSegundos(segundos))
        print("\n")
    elif resposta == 8:
        numero_usuario = int(input("Digite um número Inteiro para descobrir se ele é perfeito ou não: "))
        print (numPerfeito(numero_usuario))
        print("\n")
    elif resposta == 9:
        sexo = input("Digite seu sexo, Masculino (M) ou  Feminino (F): ")
        altura = float(input("Digite sua altura, Ex: 1.92: "))
        print(f"Seu peso ideal é {funcaoIMC(altura,sexo)}")
        print("\n")
    elif resposta == 10:
        x = float(input("Digite o comprimento do lado X: "))
        y = float(input("Digite o comprimento do lado y: "))
        z = float(input("Digite o comprimento do lado z: "))

        triangulo_tipo = eTrianguloOuNao(x,y,z)

        if triangulo_tipo == False:
            print("Não é um triângulo válido colega!")
            print("\n")
        else:
            print(f"É um triângulo {triangulo_tipo}")
            print("\n")
    elif resposta == 0:
        print ("Saindo do programa!")
        print("\n")
    else:
        print("Coloque um valor decente!")