class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self._hash(chave)
        for par in self.tabela[indice]:
            if par[0] == chave:
                par[1] = valor
                return
        self.tabela[indice].append([chave, valor])

    def obter(self, chave):
        indice = self._hash(chave)
        for par in self.tabela[indice]:
            if par[0] == chave:
                return par[1]
        return None

    def remover(self, chave):
        indice = self._hash(chave)
        for i, par in enumerate(self.tabela[indice]):
            if par[0] == chave:
                del self.tabela[indice][i]
                return


tabela_hash = TabelaHash(10)
tabela_hash.inserir("chave1", "valor1")
tabela_hash.inserir("chave2", "valor2")
print(tabela_hash.obter("chave1"))  
tabela_hash.remover("chave1")
print(tabela_hash.obter("chave1"))  
