def contadoring_sort(vetor):
    valor_max = max(vetor)
    
    contador = [0] * (valor_max + 1)
 
    for num in vetor:
        contador[num] += 1
    

    index = 0
    for i in range(len(contador)):
        while contador[i] > 0:
            vetor[index] = i
            index += 1
            contador[i] -= 1

vetor = [4, 2, 2, 8, 3, 3, 1]
print("vetoray original:", vetor)
contadoring_sort(vetor)
print("vetoray ordenado:", vetor)
