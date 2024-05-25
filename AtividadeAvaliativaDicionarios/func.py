import json

def keyExisteOuNao(isbn, livros_biblioteca):
    if isbn in livros_biblioteca:
        return True
    else:
        return False
    
def pesquisarLivro(titulo,livros):
    resultados = ''
    for isbn,livro in livros.items():
        if titulo.lower() in livro['titulo'].lower():
            resultados += f"\nISBN:{isbn}\nTítulo:{livro['titulo']}\nAutor:{livro['autor']}\nGênero:{livro['genero']}\nPreço de Compra:{livro['preco_compra']}\nPreço de Venda:{livro['preco_venda']}\nQuantidade de Estoque:{livro['qtd_estoque']}\n"
    if resultados == '':
        return False
    else:
        return resultados
    

def livrosSemEstoque(livros):
    lista_livros_sem_estoque = ''
    for isbn, dados_livro in livros.items():
        if int(dados_livro['qtd_estoque']) == 0:
            lista_livros_sem_estoque += f"\n{isbn} - {dados_livro['titulo']}"
    return lista_livros_sem_estoque

def excluirLivros(isbn,livros):
    del livros[isbn]

def adicionarLivroBiblioteca(dados_livro, livros_biblioteca):
    isbn,titulo,autor,genero,preco_compra,preco_venda,qtd_estoque = dados_livro.split(',')
    livros_biblioteca[isbn] = {'titulo':titulo,'autor':autor,'genero':genero,'preco_compra':preco_compra,'preco_venda':preco_venda,'qtd_estoque':qtd_estoque}

def carregarLivros(nomeArquivo):
    arquivo = open(nomeArquivo,'r')
    conteudo = arquivo.read().strip(' ')
    livros = {}
    if conteudo:
        livros = json.loads(conteudo)
    arquivo.close()
    return livros

def salvarLivros(nomeArquivo,livros):
    arquivo = open(nomeArquivo,'w')
    livrosJson = json.dumps(livros,indent=4)
    arquivo.write(livrosJson)
    arquivo.close()