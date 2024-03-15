def mediaListas(lista):
    new_list = lista[:]
    for i in range(len(new_list)):
        media = 0
        for k in range(3):
            media+=new_list[i][k]
        new_list[i].append(media/3)
    media_geral = 0
    for i in range(len(new_list)):
        media_geral += new_list[i][3]
    new_list.append(media_geral/len(new_list))
    return new_list


