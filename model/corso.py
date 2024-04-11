from dataclasses import dataclass


@dataclass
class Corso:
    codins: str
    crediti: int
    nome: str
    pd: int
    studenti: []

    def __str__(self):
        return f'{self.nome} ({self.codins})'

    def addIscritto(self, st):
        self.studenti.append(st)