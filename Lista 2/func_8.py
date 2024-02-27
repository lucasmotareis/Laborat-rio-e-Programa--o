#todo numéro perfeito é par, ainda não foi descorte um ímpar perfeito e se fosse descoberto
#ele seria enorme
#numero de Mersenne = 2**n − 1 | nem todo número de Mersenne é primo, assim como nem todo número primo é de Mersenne
#numero perfeito = 2**(n-1)*numero de Mersenne

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


numero_usuario = int(input("Digite um número Inteiro para descobrir se ele é perfeito ou não: "))
print (numPerfeito(numero_usuario))