class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self._ano = ano
        self._like = 0

    @property
    def nome(self):
        return self._nome.title()

    @property
    def like(self):
        return self._like

    def dar_like(self):
        self._like += 1