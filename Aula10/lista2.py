import func2
dicionario = {}

usuario_objetos = input("Digite o nome dos objetos separados por vírgula: ")

lista = usuario_objetos.lower()
lista = lista.replace(' ','')
lista = lista.rsplit(',')

for objeto in lista:
    func2.contarObjetos(dicionario,objeto)

for objeto,quantidade_objeto in dicionario.items():
    print(f"{objeto} - {quantidade_objeto['quantidade']}")



print(f"Total de objetos: {func2.contarTotalObjetos(dicionario)}")