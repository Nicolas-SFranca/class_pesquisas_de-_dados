import time
import random

def merge_sort(ordenar):
    if len(ordenar) <= 1:
        return ordenar
    meio = len(ordenar) // 2
    left_lista = ordenar[:meio]
    right_lista = ordenar[meio:]
    left_lista = merge_sort(left_lista)
    right_lista = merge_sort(right_lista)
    print("esquerda",left_lista)
    print("direita",right_lista)
    return merge(left_lista, right_lista)

def merge(left_lado, right_lado):
    temp = []
    p1 = p2 = 0
    while p1 < len(left_lado) and p2 < len(right_lado):
        if left_lado[p1] < right_lado[p2]:
            temp.append(left_lado[p1])
            p1 += 1
        else:
            temp.append(right_lado[p2])
            p2 += 1
    while p1 < len(left_lado):
        temp.append(left_lado[p1])
        p1 += 1
    while p2 < len(right_lado):
        temp.append(right_lado[p2])
        p2 += 1
    return temp

def imprimir():
    start_time = time.time()
    ordenados = [i for i in range(1, 1000)]
    print("Números Ordenados:", ordenados)
    ordenados = merge_sort(ordenados)
    print("Tempo de execução para números ordenados: %s segundos" % (time.time() - start_time))
    
    start_time = time.time()
    inversos = [i for i in range(1000, 0, -1)]
    print("Números Inversos:", inversos)
    inversos =merge_sort(inversos)
    print("Tempo de execução para números inversos: %s segundos" % (time.time() - start_time))
    
    start_time = time.time()
    duplicados = [i // 2 for i in range(2000)]
    print("Números Duplicados:", duplicados)
    duplicados = merge_sort(duplicados)
    print("Tempo de execução para números duplicados: %s segundos" % (time.time() - start_time))
    
    start_time = time.time()
    aleatorios = [random.randint(1, 1000) for _ in range(1000)]
    print("Números Aleatórios:", aleatorios)
    aleatorios=merge_sort(aleatorios)
    print("Tempo de execução para números aleatórios: %s segundos" % (time.time() - start_time))

imprimir()


