def negativoPositivo(num):
    if num >= 0:
        x = True
    else:
        x=False
    return x

def imprimaNumero(num):
    if num >= 0:
        x = f"O valor {num} informado é positivo"
    else:
        x= f"O valor {num} informado é negativo"
    return x

def retornaSinal(num):
    if num % 2 == 0:
        x = 'Par'
    else:
        x= 'Ímpar'
    return x

def mediaAritmetica(nota1,nota2,nota3,tipo_media):
    if tipo_media == 'A':
        media = (nota1+nota2+nota3)/3
    elif tipo_media == 'B':
        media = (nota1*5)+(nota2*3)+(nota3*2)/3
    return media

def idadeEmDias(anos,meses,dias):
    idade_em_dias = (anos*360)+((meses*30)-(30-dias))
    return idade_em_dias

def retornaOrdemNumeros(num):
    if len(num) < 2:
        return num
    else:
        pivo = num[0]
        i=1
        menor_que_pivo = []
        maior_que_pivo = []
        while i < len(num):
            if num[i] <= pivo:
                menor_que_pivo.append(num[i])
            else:
                maior_que_pivo.append(num[i])
            i+=1
        return retornaOrdemNumeros(menor_que_pivo) + [pivo] + retornaOrdemNumeros(maior_que_pivo)
    
def converterSegundos(segundos):
    horas = segundos // 3600
    segundos = segundos%3600
    minutos = segundos // 60
    segundos = segundos%60
    segundo = segundos
    return f"{horas}:{minutos}:{segundo}"

def numPerfeito(num):
    if num % 2 == 0:
        i=0
        numero_perfeito = 0
        while num != numero_perfeito and numero_perfeito<=num:
            numero_perfeito = (2**(i-1))*(2**i - 1)
            i+=1
        if num == numero_perfeito:
            return True
        else:
            return False
    else:
        return False

def funcaoIMC (altura,sexo):
    if sexo == 'M':
        imc_ideal = 72.7*altura-58
    elif sexo == 'F':
        imc_ideal = 62.1*altura-44.7
    else:
        print("Escolha um sexo válido!")
        return False
    return imc_ideal

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