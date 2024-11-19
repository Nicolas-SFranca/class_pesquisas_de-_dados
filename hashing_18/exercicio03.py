class Arquivo:
    def __init__(self, nome, caminho_arquivo, tamanho_arquivo):
        self.nome = nome
        self.caminho_arquivo = caminho_arquivo
        self.tamanho_arquivo = tamanho_arquivo

    def get_nome(self):
        return self.nome

    def get_caminho_arquivo(self):
        return self.caminho_arquivo

    def get_tamanho_arquivo(self):
        return self.tamanho_arquivo


class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def hash(self, nome):
        return hash(nome) % self.tamanho

    def adicionar(self, arquivo):
        indice = self.hash(arquivo.get_nome())
        for par in self.tabela[indice]:
            if par.get_nome() == arquivo.get_nome():
                par.caminho_arquivo = arquivo.get_caminho_arquivo()
                par.tamanho_arquivo = arquivo.get_tamanho_arquivo()
                return
        self.tabela[indice].append(arquivo)

    def buscar(self, nome):
        indice = self.hash(nome)
        for par in self.tabela[indice]:
            if par.get_nome() == nome:
                return par
        return None

    def remover(self, nome):
        indice = self.hash(nome)
        for i, par in enumerate(self.tabela[indice]):
            if par.get_nome() == nome:
                del self.tabela[indice][i]
                return

    def listar(self):
        arquivos = []
        for lista in self.tabela:
            for arq in lista:
                arquivos.append(f"{arq.get_nome()} - {arq.get_caminho_arquivo()} - {arq.get_tamanho_arquivo()} KB")
        return arquivos



tabela = TabelaHash(10)

tabela.adicionar(Arquivo("relatorio.pdf", "/documentos/relatorio.pdf", 150))
tabela.adicionar(Arquivo("imagem.png", "/imagens/imagem.png", 200))
tabela.adicionar(Arquivo("dados.csv", "/planilhas/dados.csv", 512))
tabela.adicionar(Arquivo("foto.jpg", "/imagens/foto.jpg", 2048))
tabela.adicionar(Arquivo("backup.zip", "/backup/backup.zip", 4096))


arquivo = tabela.buscar("relatorio.pdf")
if arquivo:
    print(f"Arquivo encontrado: {arquivo.get_nome()}, Caminho: {arquivo.get_caminho_arquivo()}, Tamanho: {arquivo.get_tamanho_arquivo()} KB")


todos_arquivos = tabela.listar()
for arq in todos_arquivos:
    print(arq)

tabela.remover("imagem.png")
print("Arquivo 'imagem.png' removido.")

print("Arquivos restantes:")
for arq in tabela.listar():
    print(arq)
