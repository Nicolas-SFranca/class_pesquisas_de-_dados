def heap_sort_max(a):
    for k in range(len(a) // 2 - 1, -1, -1):
        max_heapify(a, k, len(a))

    for n in range(len(a) - 1, 0, -1):
        a[0], a[n] = a[n], a[0]
        max_heapify(a, 0, n)

def max_heapify(a, i, n):
    maior = i
    l = 2 * i + 1  
    r = 2 * i + 2 

    if l < n and a[l] > a[maior]:
        maior = l

    if r < n and a[r] > a[maior]:
        maior = r

    if maior != i:
        a[i], a[maior] = a[maior], a[i]
        max_heapify(a, maior, n)

def heap_sort_min(a):
    for k in range(len(a) // 2 - 1, -1, -1):
        min_heapify(a, k, len(a))

    for n in range(len(a) - 1, 0, -1):
        a[0], a[n] = a[n], a[0]
        min_heapify(a, 0, n)

def min_heapify(a, i, n):
    menor = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and a[l] < a[menor]:
        menor = l

    if r < n and a[r] < a[menor]:
        menor = r

    if menor != i:
        a[i], a[menor] = a[menor], a[i]
        min_heapify(a, menor, n)

def remove_max(a): 
    a[0], a[-1] = a[-1], a[0]
    a.pop()
    heap_sort_max(a)
    return a

def insert_max(a, valor):
    a.append(valor)
    heap_sort_max(a)
    return a

def remove_min(a): 
    a[0], a[-1] = a[-1], a[0]
    a.pop()
    heap_sort_min(a)
    return a

def insert_min(a, valor):
    a.append(valor)
    heap_sort_min(a)
    return a

a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heap_sort_max(a)
print("Array ordenado (Max Heap):", a)
print("\nRemovendo o valor máximo: ", a[0])
a = remove_max(a)
print(a)

print("\nAdicionando um novo valor (Max Heap): ", 20)
a = insert_max(a, 20)
print(a)

b = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heap_sort_min(b)
print("\nArray ordenado (Min Heap):", b)
print("\nRemovendo o valor mínimo: ", b[0])
b = remove_min(b)
print(b)

print("\nAdicionando um novo valor (Min Heap): ", 20)
b = insert_min(b, 20)
print(b)
