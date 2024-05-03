from unidecode import unidecode

def nomesDeFilhos(nome):
    nome = unidecode(nome)
    nome = nome.lower()
    nome = nome.rsplit(' ')
    
    if nome[-1] == 'junior' or nome[-1] == 'filho' or nome[-1] == 'neto' or nome[-1] == 'sobrinho':
        return True
    return False