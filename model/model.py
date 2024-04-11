from database.corso_DAO import CorsoDAO
from database.studente_DAO import StudenteDAO
from model.studente import Studente
from model.corso import Corso


class Model:
    """
    classe modello con lista di corsi e di studenti
    """
    def __init__(self):
        self._studenti = list()
        self._corsi = list()
        self.initialize()

    def initialize(self):
        """
        chiama le funzioni per popolare il modello
        :return:
        """
        self.addCorsi()
        self.addStudenti()
        self.addIscrizioni()
        self.addIscritti()

    def addCorsi(self):
        """
        crea gli oggetti Corso e li restituisce
        :return:
        """
        cDAO = CorsoDAO()
        crs = cDAO.get_methods()
        for c in crs:
            self._corsi.append(Corso(c['codins'], c['crediti'], c['nome'], c['pd'], []))
        return self._corsi

    def addStudenti(self):
        """
        crea gli ogetti Studente e li restituisce
        """
        sDAO = StudenteDAO()
        std = sDAO.get_methods()
        for s in std:
            st = Studente(s['matricola'], s['cognome'], s['nome'], s['CDS'], [])
            self._studenti.append(st)
        return self._studenti

    def addIscrizioni(self):
        sDAO = StudenteDAO()
        for s in self._studenti:
            for codins in sDAO.get_iscrizioni(s.matricola):        #estraggo i corsi a cui è iscritto
                corso = self.cercaCorso(codins)     #trovo l'oggetto corso
                s.addCorso(corso)      #aggiungo il corso alle iscrizioni
        return self._studenti

    def addIscritti(self):
        cDAO = CorsoDAO()
        for c in self._corsi:
            matricole = cDAO.get_iscritti(c.codins)     #iscritti ad un corso
            for m in matricole:
                st = self.cercaStudente(m)      #oggetto Studente
                c.addIscritto(st)       #aggiungo alla lista di studenti
        return self._corsi

    def cercaCorso(self, codins):
        for c in self._corsi:
            if c.codins == codins:
                return c

    def cercaStudente(self, matricola):
        for st in self._studenti:
            if st.matricola == matricola:
                return st

    @property
    def studenti(self):
        return self._studenti

    @property
    def corsi(self):
        return self._corsi

if __name__ == '__main__':
    model = Model()
    studenti = model.addStudenti()
    for s in studenti:
        print(s)
