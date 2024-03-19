import random

def listaAleatoria(numero):
    new_list = [random.randint(1, numero) for i in range(numero)]
    new_list.sort()
    return new_list

def pesquisa_binaria(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
      # ... check the middle element
      mid = (low + high) // 2
      guess = list[mid]
      # Found the item.
      if guess == item:
        return mid
      # The guess was too high.
      if guess > item:
        high = mid - 1
      # The guess was too low.
      else:
        low = mid + 1
    return None
   




def pesquisa_lenta(lista_ordernada, valor_a_encontrar):
  for i in range(len(lista_ordernada)):
    if valor_a_encontrar == lista_ordernada[i]:
      return i
  return None







