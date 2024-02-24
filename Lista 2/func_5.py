def idadeEmDias(anos,meses,dias):
    idade_em_dias = (anos*360)+((meses*30)-(30-dias))
    return idade_em_dias
#uma dúvida, quando o mês é contado, geralmente ele é contado inteiro(os 30 dias completos).
#por causa disso não sei se é correto colocar mesCompleto+Dias, e sim mesCompleto-(30-dias), que creio dar 
#a idade verdadeira do cabra. Mas não sei se tá certo.

idade_em_anos = int (input("Digite sua idade em Anos: "))
idade_em_meses = int (input("Digite sua idade em Meses: "))
idade_em_dias =int (input("Digite sua idade em Dias: "))
print(f"Sua idade em Dias é {idadeEmDias(idade_em_anos,idade_em_meses,idade_em_dias)}")
