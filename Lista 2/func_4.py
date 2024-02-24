def mediaAritmetica(nota1,nota2,nota3,tipo_media):
    if tipo_media == 'A':
        media = (nota1+nota2+nota3)/3
    elif tipo_media == 'B':
        media = (nota1*5)+(nota2*3)+(nota3*2)/3
    return media

letra = input("Digite uma letra: ")
nota1 = float(input("Digite a Nota 1: "))
nota2 = float(input("Digite a Nota 2: "))
nota3 = float(input("Digite a Nota 3: "))
print(f"A média é {mediaAritmetica(nota1,nota2,nota3,letra):.2f}!")
