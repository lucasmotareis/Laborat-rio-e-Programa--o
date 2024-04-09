from func import *


salario_semanas = int(input("Quantas semanas se passaram?: "))

lista_comissao_funcionario = []

funcionario_salario = float(input("Digite quantos R$ o vendedor vendeu na semana?: (Digite -1 para sair):  "))
while funcionario_salario != -1:
    lista_comissao_funcionario.append((funcionario_salario*0.09)+(200*salario_semanas))
    funcionario_salario = float(input("Digite quantos R$ o vendedor vendeu na semana?: (Digite -1 para sair):  "))

(a,b,c,d,e,f,g,h,i) = funcionariosCategorias(lista_comissao_funcionario)

print(f'''a. $200 - $299// {a}
b. $300 - $399// {b}
c. $400 - $499// {c}
d. $500 - $599// {d}
e. $600 - $699// {e}
f. $700 - $799// {f}
g. $800 - $899// {f}
h. $900 - $999// {h}
i. $1000 em diante// {i}''')
