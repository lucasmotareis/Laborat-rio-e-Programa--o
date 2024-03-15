from math import floor

def ordenaAlfabetica(lista):
    new_list = lista[:]
    par=[]
    impar=[]
    for i in new_list:
        if floor(i) %2 == 0:
            par.append(i)
        else:
            impar.append(i)
    return f"Os números pares são: {par}\nOs números ímpares são: {impar}"

