def somaCpf(cpf):
    soma = 0
    cpf = cpf.replace('.','-')
    cpf = cpf.rsplit('-')
    for i in cpf:
        soma += int(i)
    return soma