class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def lst_cria():
    return None

def lst_insere(lst, v):
    novo = Lista(v)
    if lst is None:
        return novo
    atual = lst
    while atual.prox is not None:
        atual = atual.prox
    atual.prox = novo
    return lst

def lst_imprime(lst):
    atual = lst
    while not lst_vazia(atual):
        print(atual.info, end=" -> ")
        atual = atual.prox
    print("None")

def lst_vazia(lst):
    return lst is None

def lst_selection_sort(lst):
    if lst_vazia(lst) or lst.prox is None:
        return lst
    
    sorted_lst = lst_cria()
    
    while not lst_vazia(lst):
        menor, menor_ant, menor_atual = lst, None, lst
        
        while menor_atual.prox is not None:
            if menor_atual.prox.info < menor.info:
                menor = menor_atual.prox
                menor_ant = menor_atual
            menor_atual = menor_atual.prox
        
        if menor_ant is None:
            lst = menor.prox
        else:
            menor_ant.prox = menor.prox
        
        sorted_lst = lst_insere(sorted_lst, menor.info)
    
    return sorted_lst

def testar_selection_sort_encadeada():
    lista_ordenada = lst_cria()
    for valor in [1, 2, 3, 4, 5]:
        lista_ordenada = lst_insere(lista_ordenada, valor)
    print("elementos já ordenados:")
    lst_imprime(lista_ordenada)
    lista_ordenada = lst_selection_sort(lista_ordenada)
    lst_imprime(lista_ordenada)

    lista_inversa = lst_cria()
    for valor in [5, 4, 3, 2, 1]:
        lista_inversa = lst_insere(lista_inversa, valor)
    print("elementos na ordem inversa:")
    lst_imprime(lista_inversa)
    lista_inversa = lst_selection_sort(lista_inversa)
    lst_imprime(lista_inversa)

    lista_duplicada = lst_cria()
    for valor in [4, 5, 3, 4, 2, 2, 1, 3]:
        lista_duplicada = lst_insere(lista_duplicada, valor)
    print("elementos duplicados:")
    lst_imprime(lista_duplicada)
    lista_duplicada = lst_selection_sort(lista_duplicada)
    lst_imprime(lista_duplicada)
    lista_aleatoria = lst_cria()
    for valor in [8, 3, 7, 2, 5, 1, 6, 4]:
        lista_aleatoria = lst_insere(lista_aleatoria, valor)
    print("elementos sem repetição:")
    lst_imprime(lista_aleatoria)
    lista_aleatoria = lst_selection_sort(lista_aleatoria)
    lst_imprime(lista_aleatoria)

testar_selection_sort_encadeada()
