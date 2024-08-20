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

ordenar = [34, 44,44, 22, 25, 18, 11, 15]
print(merge_sort(ordenar))
