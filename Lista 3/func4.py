def menu():
    return print('''
[1] Pode votar?
[2] Ver Categoria
[3] Pode alistar?
[4] Encerrar programa 
>>>>''')

def podeVotar():
    idade  = int(input("Digite sua idade: "))
    nacionalidade = input("Digite sua nacionalidade: ")
    if idade >= 16 and nacionalidade == 'brasileiro':
        return True
    else:
        return False
    
def categoriaUsuario():
    idade  = int(input("Digite a idade de uma pessoa: "))
    if idade <= 11:
        return 'Criança'
    elif idade <=20:
        return 'Adolescente'
    elif idade <= 30:
        return 'Jovem'
    elif idade <= 59:
        return 'Adulto'
    elif idade >= 60:
        return 'Idoso'
    
def podeAlistar():
    sexo = input("Digite seu Sexo, Masculino(M) ou Feminino(F): ")
    idade = int(input("Digite a idade de uma pessoa: "))
    if sexo == 'M' and idade >= 18:
        return True
    else:
        return False