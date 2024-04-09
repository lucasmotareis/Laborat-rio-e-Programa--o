def entradaSalto():
    notas = []
    i=1
    for i in range(5):
        notas.append(float(input(f"Digite a nota do salto {i+1}: ")))
    return [nota for nota in notas]

def mediaSalto(soma_saltos):
    return soma_saltos/5