import func

arquivo = 'AtividadeAvaliativaDicionarios/livros.json'
livros = func.carregarLivros(arquivo)

while True:
    entrada = int(input("""
                        Digite a opção desejada:
                        1-Registrar novos livros
                        2-Listar livros
                        3-Excluir livro
                        4-Pesquisar livros
                        5-Relatório de livros sem estoque                   
                        6- Sair
                        > 
                        """))
    if entrada == 1:
        dados_livro = input("Cadastre um livro: isbn,titulo,autor,genero,preco_compra,preco_venda,qtd_estoque (0 - para sair):")
        if dados_livro == '0':
            break
        isbn,titulo,autor,genero,preco_compra,preco_venda,qtd_estoque = dados_livro.split(',')
        if func.keyExisteOuNao(isbn,livros) == True:
            print("Este livro já está cadastrado!!")
        else:
            func.adicionarLivroBiblioteca(dados_livro, livros)
            func.salvarLivros(arquivo,livros)
    elif entrada == 2:
        print("\nOs livros são: ")
        for isbn,livro in livros.items():
            print(f"{isbn} - {livro['titulo']} - {livro['qtd_estoque']}")

    elif entrada == 3:
        excluir_livro = input("Digite o ISBN do livro para exlui-lo: ")
        if func.keyExisteOuNao(excluir_livro, livros) == True:
            func.excluirLivros(excluir_livro,livros)
            func.salvarLivros(arquivo,livros)
            print("O livro foi exclúido com sucesso!")
        else:
            print("O livro não existe! Não é possível exluí-lo!")
    elif entrada == 4:
        pesquisar_livro = input("Digite o título do livro a ser pesquisado: ")
        resultados = func.pesquisarLivro(pesquisar_livro,livros)
        if resultados == False:
            print("O livro não existe!!")
        else:
            print(resultados)
    
    elif entrada == 5:
        livro_sem_estoque = func.livrosSemEstoque(livros)
        print(livro_sem_estoque)
    
    elif entrada == 6:
        print("Saindo do aplicativo!")
        break


