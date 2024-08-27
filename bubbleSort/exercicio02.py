import random
import time

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
    start_time = time.time()
    ordenados = [i for i in range(1, 101)]
    ordenados = bubblesort(ordenados)
    print("Números Ordenados:", ordenados)
    print("Tempo de execução para números ordenados: %s segundos" % (time.time() - start_time))
    
    start_time = time.time()
    inversos = [i for i in range(100, 0, -1)]
    inversos = bubblesort(inversos)
    print("Números Inversos:", inversos)
    print("Tempo de execução para números inversos: %s segundos" % (time.time() - start_time))
    
    start_time = time.time()
    duplicados = [i // 2 for i in range(200)]
    duplicados = bubblesort(duplicados)
    print("Números Duplicados:", duplicados)
    print("Tempo de execução para números duplicados: %s segundos" % (time.time() - start_time))
    
    start_time = time.time()
    aleatorios = [random.randint(1, 100) for _ in range(100)]
    aleatorios = bubblesort(aleatorios)
    print("Números Aleatórios:", aleatorios)
    print("Tempo de execução para números aleatórios: %s segundos" % (time.time() - start_time))

imprimir()
