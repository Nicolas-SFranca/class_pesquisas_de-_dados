def inserir_em_ordem(lista):
    for i in range(1, len(lista)):
        temp = lista[i]
        j = i - 1
        while j >= 0 and temp < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = temp
    return lista

def imprimir():
    lista_ordenada = [1, 2, 3, 4, 5]
    print("Teste com elementos já ordenados:", inserir_em_ordem(lista_ordenada))
    lista_inversa = [5, 4, 3, 2, 1]
    print("Teste com elementos na ordem inversa:", inserir_em_ordem(lista_inversa))
    lista_duplicada = [4, 5, 3, 4, 2, 2, 1, 3]
    print("Teste com elementos duplicados:", inserir_em_ordem(lista_duplicada))
    lista_aleatoria = [8, 3, 7, 2, 5, 1, 6, 4]
    print("Teste com elementos aleatórios sem repetição:", inserir_em_ordem(lista_aleatoria))
imprimir()

