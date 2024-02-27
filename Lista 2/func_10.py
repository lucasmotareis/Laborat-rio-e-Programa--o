def eTrianguloOuNao(x, y, z):
    if x<(y+z) and y<(x+z) and z<(x+y):
        if x == y and x == z:
            tipoTriangulo = 'Equilátero'
        elif (x == y or x == z or y == z):
            tipoTriangulo = 'Isósceles'
        else:
            tipoTriangulo = 'Escaleno'
    else:
        tipoTriangulo = False    
    return tipoTriangulo

x = float(input("Digite o comprimento do lado X: "))
y = float(input("Digite o comprimento do lado y: "))
z = float(input("Digite o comprimento do lado z: "))

triangulo_tipo = eTrianguloOuNao(x,y,z)

if triangulo_tipo == False:
    print("Não é um triângulo válido colega!")
else:
    print(f"É um triângulo {triangulo_tipo}")