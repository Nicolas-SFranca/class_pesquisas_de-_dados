def selection_sort(data):
    n = len(data)
    for i in range(n-1):
        menor_id = i
        for j in range(i+1, n):
            if data[j] < data[menor_id]:
                menor_id = j
        data[i], data[menor_id] = data[menor_id], data[i]
    return data

def testar_selection_sort():
    lista_ordenada = [1, 2, 3, 4, 5]
    print("Teste com elementos já ordenados:")
    print(selection_sort(lista_ordenada))

    lista_inversa = [5, 4, 3, 2, 1]
    print("Teste com elementos na ordem inversa:")
    print(selection_sort(lista_inversa))

    lista_duplicada = [4, 5, 3, 4, 2, 2, 1, 3]
    print("Teste com elementos duplicados:")
    print(selection_sort(lista_duplicada))

    lista_aleatoria = [8, 3, 7, 2, 5, 1, 6, 4]
    print("Teste com elementos sem repetição:")
    print(selection_sort(lista_aleatoria)
testar_selection_sort()
