def mantemArtigos(lista):
    for i in range(len(lista)):
        if lista[i] == 'da' or lista[i] == 'de' or lista[i] == 'das' or lista[i] == 'do' or lista[i] == 'dos' or lista[i] == 'e':
            continue
        lista[i] = lista[i][:1]+ '.'

    return ' '.join(lista)