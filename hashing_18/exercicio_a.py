class TabelaHash:
    def __init__(self):
        self.tabela = {'key1': [], 'key2': []}

    def inserir(self, chave, valor):
        if chave not in self.tabela:
            self.tabela[chave] = []
        self.tabela[chave].append(valor)

    def buscar(self, chave):
        return self.tabela.get(chave, [])

    def remover(self, chave, valor):
        if chave in self.tabela:
            try:
                self.tabela[chave].remove(valor)
                if not self.tabela[chave]:
                    del self.tabela[chave]
            except ValueError:
                pass


hash_table = TabelaHash()
hash_table.inserir('key1', 'valor1')
hash_table.inserir('key1', 'valor2')
hash_table.inserir('key2', 'valor3')

print(hash_table.buscar('key1'))  
print(hash_table.buscar('key2'))  

hash_table.remover('key1', 'valor1')
print(hash_table.buscar('key1'))  
