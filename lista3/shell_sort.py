def shell_sort(lst, pulos):
    while pulos > 0:
        for i in range(pulos, len(lst)):
            valor_atual = lst[i]
            j = i
            
            while j >= pulos and lst[j - pulos] > valor_atual:
                lst[j] = lst[j - pulos]
                j -= pulos
            
            lst[j] = valor_atual
        
        pulos //= 2
    return lst
def inserir_em_ordem(lst):
    return shell_sort(lst, len(lst) // 2)
def imprimir():
    lista_ordenada = [1, 2, 3, 4, 5]
    print("elementos já ordenados:", inserir_em_ordem(lista_ordenada))
    lista_inversa = [5, 4, 3, 2, 1]
    print("elementos na ordem inversa:", inserir_em_ordem(lista_inversa))
    lista_duplicada = [4, 5, 3, 4, 2, 2, 1, 3]
    print("elementos duplicados:", inserir_em_ordem(lista_duplicada))
    lista_aleatoria = [8, 3, 7, 2, 5, 1, 6, 4]
    print("elementos aleatórios sem repetição:", inserir_em_ordem(lista_aleatoria))

imprimir()
