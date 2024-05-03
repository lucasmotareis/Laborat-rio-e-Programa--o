def tiraPrimeiraLetra(lista):
    
    for i in range(len(lista)):
        lista[i] = lista[i][:1]

    return '. '.join(lista)