def particiona(lst, inicio, fim):
    pivo = inicio
    esq = inicio + 1
    dir = fim
    
    while esq <= dir:
        while esq <= fim and lst[esq] <= lst[pivo]:
            esq += 1
        while lst[dir] > lst[pivo]:
            dir -= 1
        if esq < dir:
            lst[esq], lst[dir] = lst[dir], lst[esq]
    
    lst[dir], lst[pivo] = lst[pivo], lst[dir]
    return dir

def quick_sort(lst, inicio, fim):
    if inicio < fim:
        pivo_index = particiona(lst, inicio, fim)
        quick_sort(lst, inicio, pivo_index - 1)
        quick_sort(lst, pivo_index + 1, fim)

def inserir_em_ordem(lst):
    quick_sort(lst, 0, len(lst) - 1)
    return lst

def imprimir():
    lista_ordenada = [1, 2, 3, 4, 5]
    print("elementos já ordenados:", inserir_em_ordem(lista_ordenada))
    lista_inversa = [5, 4, 3, 2, 1]
    print("elementos na ordem inversa:", inserir_em_ordem(lista_inversa))
    lista_duplicada = [4, 5, 3, 4, 2, 2, 1, 3]
    print(" elementos duplicados:", inserir_em_ordem(lista_duplicada))
    lista_aleatoria = [8, 3, 7, 2, 5, 1, 6, 4]
    print(" elementos aleatórios sem repetição:", inserir_em_ordem(lista_aleatoria))

imprimir()
