from dataclasses import dataclass


@dataclass
class Studente:
    matricola: int
    cognome: str
    nome: str
    CDS: str
    iscrizioni: []

    def __str__(self):
        return f'{self.nome}, {self.cognome} ({self.matricola})'

    def addCorso(self, corso):
        self.iscrizioni.append(corso)

    def __eq__(self, other):
        return self.matricola == other.matricola