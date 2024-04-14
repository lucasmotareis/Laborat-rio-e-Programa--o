from func import *


lista_colaboradores_completa = []

print('''
Projeção de Gastos com Abono
============================      
      ''')

colaborador_nome = input("Digite o nome do colaborador: ")
colaborador_salario = float(input("Digite o salário do colaborador: "))
while colaborador_salario != 0:
    colaborador_abono = colaborador_salario*0.20
    if colaborador_abono < 100:
        colaborador_abono = 100.0
    lista_colaboradores_completa.append([colaborador_nome,colaborador_salario,colaborador_abono])
    colaborador_nome = input("Digite o nome do colaborador: ")
    colaborador_salario = float(input("Digite o salário do colaborador: "))


colaboradores_processados = len(lista_colaboradores_completa)
valor_total_a_ser_gasto = valorTotalASerGasto(lista_colaboradores_completa)
colaboradores_abono_minimo = numFuncionariosLascados(lista_colaboradores_completa)
(nome_maior_abono, valor_maior_abono) = (maiorAbono(lista_colaboradores_completa))
media_abono = mediaAbono(lista_colaboradores_completa)
soma_salario = somaSalario(lista_colaboradores_completa)
soma_abono = somaAbono(lista_colaboradores_completa )
qtd_abono_acima_media = colaboradoresAbonoAcimaMedia(lista_colaboradores_completa)

print('''
Colaborador\tSalário\t\tAbono
===========\t===========\t=============
      ''')
for i in lista_colaboradores_completa:
    print(f"{i[0]:10}\tR${i[1]:10}\tR${i[2]:10}")

print(f'''
===========\t===============\t=============       
   TOTAL\tR$ {soma_salario}\tR$ {soma_abono}
      
Foram Processados {colaboradores_processados} colaboradores
Total gasto com salários e abonos: R$ {valor_total_a_ser_gasto}
Valor mínimo pago a {colaboradores_abono_minimo} colaboradores
Maior abono pago a {nome_maior_abono} com o valor de R$ {valor_maior_abono}
Média do abono salarial: R$ {media_abono:.2f}
Foram pagos abonos acima da média a {qtd_abono_acima_media} colaborador(es).
      ''')
