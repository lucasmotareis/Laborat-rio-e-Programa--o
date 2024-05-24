def cadastrarUsuario(sistema_usuarios, login, nome,ultimo_acesso,maquina):
    return sistema_usuarios.update({login:{'nome':nome,'ultima_aparicao': ultimo_acesso, 'maquina':maquina}})

def usuarioDiaLogon(sistema_usuarios,pesquisar_data):
    usuarios_data_especifica = []
    achou = False
    for chave in sistema_usuarios:
        if pesquisar_data == sistema_usuarios[chave]['ultima_aparicao']:
            usuarios_data_especifica.append(chave)
            achou = True
    return False if achou == False else usuarios_data_especifica


def usuarioExisteOuNao(sistema_usuarios,chave_usuario):
    return sistema_usuarios.get(chave_usuario,False)

def trocarDadosUsuario(sistema_usuarios,campo_trocado,usuario_modificado):
    if campo_trocado == 'todos':
        nome_troca = input('Digite o novo nome: ')
        ultimo_acesso_troca = input('Digite o novo ultimo acesso: ')
        maquina_troca = input('Digite a nova máquina: ')
        sistema_usuarios[usuario_modificado].update({'nome':nome_troca,'ultima_aparicao': ultimo_acesso_troca,'maquina': maquina_troca})
    elif campo_trocado == 'nome':
        nome_troca = input('Digite o novo nome: ')
        sistema_usuarios[usuario_modificado].update({'nome': nome_troca})
    elif campo_trocado == 'ultimo acesso':
        ultimo_acesso_troca = input('Digite a nova ultima aparição: ')
        sistema_usuarios[usuario_modificado].update({'ultima_aparicao':ultimo_acesso_troca})
    elif campo_trocado == 'maquina':
        maquina_troca = input('Digite a nova maquina: ')
        sistema_usuarios[usuario_modificado].update({'maquina':maquina_troca})
    else:
        return False
    return True

def deletarUsuario(sistema_usuarios,chave_removida):
    return sistema_usuarios.pop(chave_removida,False)
