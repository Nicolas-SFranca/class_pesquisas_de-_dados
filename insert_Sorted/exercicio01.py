import time
import random

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
    start_time = time.time()
    ordenados = [i for i in range(1, 1000)]
    print("Números Ordenados:", ordenados)
    ordenados = inserir_em_ordem(ordenados)
    print("Tempo de execução para números ordenados: %s segundos" % (time.time() - start_time))
    
    start_time = time.time()
    inversos = [i for i in range(1000, 0, -1)]
    print("Números Inversos:", inversos)
    inversos = inserir_em_ordem(inversos)
    print("Tempo de execução para números inversos: %s segundos" % (time.time() - start_time))
    
    start_time = time.time()
    duplicados = [i // 2 for i in range(2000)]
    print("Números Duplicados:", duplicados)
    duplicados = inserir_em_ordem(duplicados)
    print("Tempo de execução para números duplicados: %s segundos" % (time.time() - start_time))
    
    start_time = time.time()
    aleatorios = [random.randint(1, 1000) for _ in range(1000)]
    print("Números Aleatórios:", aleatorios)
    aleatorios = inserir_em_ordem(aleatorios)
    print("Tempo de execução para números aleatórios: %s segundos" % (time.time() - start_time))

imprimir()
