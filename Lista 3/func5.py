def salarioVendedor(salario_minimo, qtd_camisetas):
    return salario_minimo + (qtd_camisetas*0.50)

def classeVendedor(salario_vendedor):
    if salario_vendedor <=  1000:
        return 'A'

    elif salario_vendedor <= 1500:
        return 'B'
    
    elif salario_vendedor <= 2000:

        return 'C'
    elif salario_vendedor > 2000:
        return 'D'