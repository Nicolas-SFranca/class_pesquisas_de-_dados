class Produto:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

class Node:
    def __init__(self, produto):
        self.produto = produto
        self.esquerda = None
        self.direita = None

class ABB:
    def __init__(self):
        self.raiz = None

    def inserir(self, produto):
        if self.raiz is None:
            self.raiz = Node(produto)
        else:
            self._inserir_recursivo(self.raiz, produto)

    def _inserir_recursivo(self, node, produto):
        if produto.id < node.produto.id:
            if node.esquerda is None:
                node.esquerda = Node(produto)
            else:
                self._inserir_recursivo(node.esquerda, produto)
        else:
            if node.direita is None:
                node.direita = Node(produto)
            else:
                self._inserir_recursivo(node.direita, produto)

    def imprimir_ordem_simetrica(self, node):
        if node:
            self.imprimir_ordem_simetrica(node.esquerda)
            print(f"ID: {node.produto.id}, Nome: {node.produto.nome}, Descrição: {node.produto.descricao}, Preço: {node.produto.preco}")
            self.imprimir_ordem_simetrica(node.direita)

    def buscar(self, id):
        return self._buscar_recursivo(self.raiz, id)

    def _buscar_recursivo(self, node, id):
        if node is None or node.produto.id == id:
            return node
        if id < node.produto.id:
            return self._buscar_recursivo(node.esquerda, id)
        return self._buscar_recursivo(node.direita, id)

    def remover(self, id):
        self.raiz = self._remover_recursivo(self.raiz, id)

    def _remover_recursivo(self, node, id):
        if node is None:
            return node
        if id < node.produto.id:
            node.esquerda = self._remover_recursivo(node.esquerda, id)
        elif id > node.produto.id:
            node.direita = self._remover_recursivo(node.direita, id)
        else:
            if node.esquerda is None:
                return node.direita
            elif node.direita is None:
                return node.esquerda
            temp = self._minimo(node.direita)
            node.produto = temp.produto
            node.direita = self._remover_recursivo(node.direita, temp.produto.id)
        return node

    def _minimo(self, node):
        current = node
        while current.esquerda is not None:
            current = current.esquerda
        return current

abb = ABB()
abb.inserir(Produto(5, "Produto 5", " CAIXA DE CERVEJA", 50.0))
abb.inserir(Produto(10, "Produto 10", "FRALDA", 100.0))
abb.inserir(Produto(15, "Produto 15", " MONSTER", 12.0))
abb.inserir(Produto(3, "Produto 3", " AGUA SEM GAS", 3.0))
abb.inserir(Produto(7, "Produto 7", "KIT DE PANELA", 70.0))

print("Impressão em ordem simétrica:")
abb.imprimir_ordem_simetrica(abb.raiz)

resultado = abb.buscar(7)
print("\nBusca pelo ID 7:", f" Produto Encontrado: {resultado.produto.nome}" if resultado else "Não encontrado")
print("\nNome:", resultado.produto.nome if resultado else "Nao encontrado")
print("Descrição:", resultado.produto.descricao if resultado else "Nao encontrado")
print("Preço:", resultado.produto.preco if resultado else "Nao encontrado")


abb.remover(5)
print("\nImpressão em ordem simétrica após remover o produto com ID 5:")
abb.imprimir_ordem_simetrica(abb.raiz)


