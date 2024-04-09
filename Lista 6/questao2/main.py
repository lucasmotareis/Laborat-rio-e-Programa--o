from func import *

lista = []

valor_usuario = float(input("Digite a nota do aluno: "))
while valor_usuario != -1:
    lista.append(valor_usuario)
    valor_usuario = float(input("Digite a nota do aluno: "))
(qtd_valor, lista_ordem, lista_inversa, soma_das_notas, media_das_notas, notas_acima_da_media, notas_abaixo_de_sete) = (qtdValor(lista),imprimeNaOrdem(lista),imprimeInverso(lista),somaDosValores(lista),mediaDosValores(lista),valoresAcimaMedia(lista),valoresAbaixoDeSete(lista))


print("a: ",qtd_valor)
print("b: ",lista_ordem)
print("c: ",lista_inversa)
print("d: ",soma_das_notas)
print("e: ",media_das_notas)
print("f: ",notas_acima_da_media)
print("g: ",notas_abaixo_de_sete)
print('''
      
      ********OBRIGADO POR ADICIONAR AS NOTAS**********   
                    SEE YOU SPACE COWBOY
      
      ''')