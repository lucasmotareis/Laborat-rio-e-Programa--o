import func1

sistema_usuarios={'mickey': {'nome':'Mickey Mouse','ultima_aparicao':'20/06/2021','maquina':'larc01'},
                  'donald': {'nome':'Donald Mouse','ultima_aparicao':'21/06/2021','maquina':'labinIV12'},
                   'minnie': {'nome':'Minnie Mouse','ultima_aparicao':'21/06/2021','maquina':'labinIV15'} }


while True:
    print("""
    Inserir usuário;
    1 - Inserir Usuário
    2 - Listar os nomes de todos os usuários;
    3 - Listar dados de um usuário;
    4 - Listar os nomes dos usuários com último acesso em uma data específica;
    5 - Alterar dados de um usuário, com as seguintes possibilidades (todos, nome, último acesso ou
    máquina);
    6 - Excluir um usuário.
    7 - Sair do Programa\n""")
    entrada_usuario = int((input("Digite o que deseja: ")))
    if entrada_usuario == 1:
        login = input('Digite o login: ')
        nome = input('Digite o nome: ')
        ultimo_acesso = input('Digite o ultimo acesso: ')
        maquina = input('Digite a máquina: ')
        func1.cadastrarUsuario(sistema_usuarios,login,nome,ultimo_acesso,maquina)
        print("Usuário adicionado com sucesso!")
    if entrada_usuario == 2:
        for chave, usuario in sistema_usuarios.items():
            print(f"{usuario['nome']}")
    elif entrada_usuario == 3:
        chave_usuario = input("Digite o login do usuário: ")
        if func1.usuarioExisteOuNao(sistema_usuarios,chave_usuario) == False:
            print("Usuário não existe!")
        else:
            usuario_dados = sistema_usuarios[chave_usuario]
            print(f'''
            Login: {chave_usuario}
            Nome: {usuario_dados['nome']}
            Ultima Aparição: {usuario_dados['ultima_aparicao']}
            Máquina: {usuario_dados['maquina']}
            ''')
    elif entrada_usuario == 4:
        pesquisar_data = input("Digite uma data para saber se algum usuário logou no dia: ")
        ultimo_login = func1.usuarioDiaLogon(sistema_usuarios,pesquisar_data)
        if ultimo_login == False:
            print('Não houve nenhum usuário que logou nessa data.')
        else:
            for chave in ultimo_login:
                print(f'''
                A ultima aparição do usuário {chave} foi na Data {pesquisar_data}
                Login: {chave}
                Nome: {sistema_usuarios[chave]['nome']}
                Ultima Aparição: {sistema_usuarios[chave]['ultima_aparicao']}
                Máquina: {sistema_usuarios[chave]['maquina']}
                ''')
        

    elif entrada_usuario == 5:
        campo_trocado = input("Digite o campo a ser trocado (todos, nome, ultimo acesso ou máquina): ")
        usuario_modificado = input("Digite o login do usuário desejada: ")
        if func1.usuarioExisteOuNao(sistema_usuarios,usuario_modificado) == False:
            print("Não existe nenhum login com esse nome!")
        else: 
            if func1.trocarDadosUsuario(sistema_usuarios,campo_trocado,usuario_modificado) == False:
                print("Campo Inválido, reiniciando Menu!")
            else:
                print("Troca feita com sucesso!")

    elif entrada_usuario == 6:
        chave_removida = input("Digite o login do usuário que deseja remover: ")
        if func1.deletarUsuario(sistema_usuarios,chave_removida) == False:
            print("Usuário não existe!")
        else:
            print("Usuário removido com sucesso.")        

    elif entrada_usuario == 7:
        break