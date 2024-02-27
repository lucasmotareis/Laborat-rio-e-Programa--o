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


num=[]
num.append(int(input("Digite o primeiro número inteiro: ")))
num.append(int(input("Digite o segundo número inteiro: ")))
num.append(int(input("Digite o terceiro número inteiro: ")))


resultado = retornaOrdemNumeros(num)

print(str(resultado[0]),",",str(resultado[1]),",",str(resultado[2]))


#Prof, depois o senhor pode me ensinar mais ou menos a pilha de chamada do QuickSort? Entendi mais ou menos.
#Tava lendo um livro e apareceu essa lógica, só que ele usa "List Comprehension" e o 'for' que ainda não aprendi corretamente.
#Então fiz do meu jeito, o código original é esse:
# def quicksort(array):
#   if len(array) < 2:
#     # base case, arrays with 0 or 1 element are already "sorted"
#     return array
#   else:
#     # recursive case
#     pivot = array[0]
#     # sub-array of all the elements less than the pivot
#     less = [i for i in array[1:] if i <= pivot]
#     # sub-array of all the elements greater than the pivot
#     greater = [i for i in array[1:] if i > pivot]
#     return quicksort(less) + [pivot] + quicksort(greater)

# print(quicksort([10, 5, 2, 3]))

#Livro Entendendo Algoritmos, Aditya Bhargava
