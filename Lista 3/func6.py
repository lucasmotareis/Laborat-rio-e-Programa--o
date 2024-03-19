

def vertebradoOuNao(tipo_animal_usuario):
    if tipo_animal_usuario == 'vertebrado':
        if aveOuMamifero() == 'ave' :
            if carnivoroOuOnivoro() == 'carnivoro':
                return f"O animal é uma águia"
            else:
                return f"O animal é uma pomba"
        else:
            if onivoroOuHerbivoro() == 'onivoro':
                return f"O animal é o homem"
            else:
                return f"O animal é uma vaca"
    else:
        if insetoOuNao() == 'inseto' :
            if hematofagoOuHerbivoro() == 'hematofago':
                return f"O animal é uma pulga"
            else:
                return f"O animal é uma lagarta"
        else:
            if hematofagoOuOnivoro() == 'hematofago':
                return f"O animal é uma sanguessuga"
            else:
                return f"O animal é uma minhoca"


def aveOuMamifero():
    return input("É ave ou mamífero?: ")

def carnivoroOuOnivoro():
    return input("É carnívoro ou onívoro?: ")

def hematofagoOuHerbivoro():
    return input("É hemátofago ou herbívoro?: ") 

def hematofagoOuOnivoro():
    return input("É hemátofago ou onívoro?: ") 


def onivoroOuHerbivoro():
    return input("É herbívaro ou onívoro?: ")

def insetoOuNao():
    return input("É inseto ou anelídeo?: ")
