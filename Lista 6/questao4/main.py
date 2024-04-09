from func import *


atleta_nome = input("Digite o nome do Atleta: ")
while atleta_nome != '':
    (primeiro_salto,segundo_salto,terceiro_salto,quarto_salto,quinto_salto) = entradaSalto()


    print(f'''
    Atleta: {atleta_nome}
    Primeiro Salto: {primeiro_salto} m
    Segundo Salto: {segundo_salto} m
    Terceiro Salto: {terceiro_salto} m
    Quarto Salto: {quarto_salto} m
    Quinto Salto: {quinto_salto} m

    Resultado final:
    Atleta: {atleta_nome}
    Saltos: {primeiro_salto}-{segundo_salto}-{terceiro_salto}-{quarto_salto}-{quinto_salto}
    Média dos saltos: {mediaSalto(primeiro_salto+segundo_salto+terceiro_salto+quarto_salto+quinto_salto):.2f} m''')

    atleta_nome = input("\nDigite o nome do Atleta: ")





