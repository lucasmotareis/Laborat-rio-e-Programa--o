def funcionariosCategorias(funcionario_salario):
    (a,b,c,d,e,f,g,h,i) = (0,0,0,0,0,0,0,0,0)
    for salario_semanal in funcionario_salario:
        if salario_semanal <= 299:
            a += 1 
        elif salario_semanal <=399:
            b+=1
        elif salario_semanal <= 499:
            c+=1
        elif salario_semanal <= 599:
            d+=1
        elif salario_semanal <= 699:
            e+=1
        elif salario_semanal <= 799:
            f+=1
        elif salario_semanal <= 899:
            g+=1
        elif salario_semanal <= 999:
            h+=1
        elif salario_semanal >= 1000:
            i+=1
    return a,b,c,d,e,f,g,h,i
        