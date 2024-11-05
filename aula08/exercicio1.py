import time
import random
import math

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    for num in arr:
        count[num] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    return output

def busca_binaria_iterativa(lista, alvo):
    esquerda, direita = 0, len(lista) - 1
    comparacoes = 0
    
    while esquerda <= direita:
        comparacoes += 1
        meio = (esquerda + direita) // 2
        
        if lista[meio] == alvo:
            return meio, comparacoes
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
            
    return -1, comparacoes

def busca_binaria_recursiva(lista, alvo, esquerda, direita, comparacoes=0):
    if esquerda > direita:
        return -1, comparacoes
    
    comparacoes += 1
    meio = (esquerda + direita) // 2
    
    if lista[meio] == alvo:
        return meio, comparacoes
    elif lista[meio] < alvo:
        return busca_binaria_recursiva(lista, alvo, meio + 1, direita, comparacoes)
    else:
        return busca_binaria_recursiva(lista, alvo, esquerda, meio - 1, comparacoes)

def pesquisa_por_salto(lista, alvo):
    n = len(lista)
    salto = int(math.sqrt(n))
    prev = 0
    comparacoes = 0
    
    while lista[min(salto, n)-1] < alvo:
        comparacoes += 1
        prev = salto
        salto += int(math.sqrt(n))
        if prev >= n:
            return -1, comparacoes
    
    while lista[prev] < alvo:
        comparacoes += 1
        prev += 1
        if prev == min(salto, n):
            return -1, comparacoes
    
    if lista[prev] == alvo:
        return prev, comparacoes
    
    return -1, comparacoes

def pesquisa_fibonacci(lista, alvo):
    fib_m2 = 0  
    fib_m1 = 1  
    fib_m = fib_m2 + fib_m1  
    comparacoes = 0

    while fib_m < len(lista):
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    offset = -1

    while fib_m > 1:
        comparacoes += 1
        i = min(offset + fib_m2, len(lista) - 1)

        if lista[i] < alvo:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif lista[i] > alvo:
            fib_m = fib_m2
            fib_m1 -= fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i, comparacoes

    if fib_m1 and lista[offset + 1] == alvo:
        return offset + 1, comparacoes

    return -1, comparacoes

def busca_por_interpolacao(lista, alvo):
    esq = 0
    dir = len(lista) - 1
    comparacoes = 0

    while esq <= dir and lista[esq] <= alvo <= lista[dir]:
        comparacoes += 1
        if esq == dir:
            if lista[esq] == alvo:
                return esq, comparacoes
            return -1, comparacoes

        meio = esq + ((alvo - lista[esq]) * (dir - esq) // (lista[dir] - lista[esq]))

        if lista[meio] == alvo:
            return meio, comparacoes
        elif lista[meio] < alvo:
            esq = meio + 1
        elif lista[meio] > alvo:
            dir = meio - 1

    return -1, comparacoes

def teste_desempenho():
    lista = random.sample(range(1, 1000000), 100000)  # 100k números aleatórios
    lista = counting_sort(lista)  # Ordena a lista usando Counting Sort
    alvo = random.choice(lista)  # Escolhe um alvo aleatório da lista

    start_time = time.perf_counter()
    resultado_iterativo, comp_iterativo = busca_binaria_iterativa(lista, alvo)
    print(f"Resultado da busca iterativa: {resultado_iterativo}, Tempo: {time.perf_counter() - start_time:.6f} segundos, Comparações: {comp_iterativo}")

    start_time = time.perf_counter()
    resultado_recursivo, comp_recursivo = busca_binaria_recursiva(lista, alvo, 0, len(lista) - 1)
    print(f"Resultado da busca recursiva: {resultado_recursivo}, Tempo: {time.perf_counter() - start_time:.6f} segundos, Comparações: {comp_recursivo}")

    start_time = time.perf_counter()
    resultado_salto, comp_salto = pesquisa_por_salto(lista, alvo)
    print(f"Resultado da pesquisa por salto: {resultado_salto}, Tempo: {time.perf_counter() - start_time:.6f} segundos, Comparações: {comp_salto}")

    start_time = time.perf_counter()
    resultado_fibonacci, comp_fibonacci = pesquisa_fibonacci(lista, alvo)
    print(f"Resultado da pesquisa Fibonacci: {resultado_fibonacci}, Tempo: {time.perf_counter() - start_time:.6f} segundos, Comparações: {comp_fibonacci}")

    start_time = time.perf_counter()
    resultado_interpolacao, comp_interpolacao = busca_por_interpolacao(lista, alvo)
    print(f"Resultado da busca por interpolação: {resultado_interpolacao}, Tempo: {time.perf_counter() - start_time:.6f} segundos, Comparações: {comp_interpolacao}")

if __name__ == "__main__":
    teste_desempenho()
