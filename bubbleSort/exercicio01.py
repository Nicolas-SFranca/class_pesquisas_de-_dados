def bubblesort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return lista
def imprimir():
    lista_ordenada = [1, 2, 3, 4, 5]
    print("elementos já ordenados:", bubblesort(lista_ordenada))
    lista_inversa = [5, 4, 3, 2, 1]
    print("elementos na ordem inversa:", bubblesort(lista_inversa))
    lista_duplicada = [4, 5, 3, 4, 2, 2, 1, 3]
    print("elementos duplicados:", bubblesort(lista_duplicada))
    lista_aleatoria = [8, 3, 7, 2, 5, 1, 6, 4]
    print("elementos aleatórios sem repetição:", bubblesort(lista_aleatoria))
imprimir()
