class Jogador:
    def __init__(self, nome, qualidade):
        self.nome = nome
        self.qualidade = qualidade

class Equipe:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def calcular_media_qualidade(self):
        if not self.jogadores:
            return 0

        total_qualidade = sum(jogador.qualidade for jogador in self.jogadores)
        media_qualidade = total_qualidade / len(self.jogadores)
        return media_qualidade

    def exibir_composicao(self):
        print(f"Composição da equipe '{self.nome}':")
        for jogador in self.jogadores:
            print(f"{jogador.nome} - Qualidade: {jogador.qualidade}")

# Teste das funcionalidades
equipe = Equipe("Equipe A")

# Adiciona alguns jogadores à equipe
jogador1 = Jogador("Jogador1", 80)
jogador2 = Jogador("Jogador2", 75)
jogador3 = Jogador("Jogador3", 90)

equipe.adicionar_jogador(jogador1)
equipe.adicionar_jogador(jogador2)
equipe.adicionar_jogador(jogador3)

# Exibe a composição da equipe
equipe.exibir_composicao()

# Calcula e exibe a média de qualidade da equipe
media_qualidade = equipe.calcular_media_qualidade()
print(f"Média de qualidade da equipe: {media_qualidade:.2f}")
