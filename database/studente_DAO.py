# Add whatever it is needed to interface with the DB Table studente
from database.DB_connect import get_connection


class StudenteDAO:
    def __init__(self):
        pass

    def get_methods(self):
        """
        restituisce gli studenti sottoforma di dizionario
        e aggiunge i corsi a cui sono iscritti
        :return:
        """
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM studente"""
        cursor.execute(query)
        std = cursor.fetchall()
        cursor.close()
        return std

    def get_iscrizioni(self, matricola):
        """
        ottengo tutte le iscrizioni di uno studente
        :param matricola:
        :return:
        """
        cnx = get_connection()
        cursor = cnx.cursor()
        query = """select codins from iscrizione where matricola = %s"""
        cursor.execute(query, (matricola,))
        iscr = [r[0] for r in cursor]
        cursor.close()
        return iscr

    def iscrivi(self, matricola, codins):
        """
        aggiunge matricola e codins alla relazione iscrizione nel database
        :param matricola:
        :param codins:
        :return:
        """
        cnx = get_connection()
        cursor = cnx.cursor()
        query = """insert into iscrizione (matricola, codins) values (%s, %s)"""
        cursor.execute(query, (matricola, codins))
        cnx.commit()
        cursor.close()

if __name__ == '__main__':
    dao = StudenteDAO()
    iscr = dao.get_iscrizioni()
    for s in iscr:
        print(s)
