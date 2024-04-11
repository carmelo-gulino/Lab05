# Add whatever it is needed to interface with the DB Table corso
from database.DB_connect import get_connection


class CorsoDAO:
    def __init__(self):
        pass

    def get_methods(self):
        """
        restituisce i corsi sottoforma di dizionario
        :return:
        """
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM corso"""
        cursor.execute(query)
        crs = cursor.fetchall()
        cursor.close()
        return crs

    def get_iscritti(self, codins):
        """
        ottengo tutti gli iscritti ad un corso
        :param matricola:
        :return:
        """
        cnx = get_connection()
        cursor = cnx.cursor(prepared=True)
        query = """select matricola from iscrizione where codins=%s"""
        cursor.execute(query, (codins,))
        iscr = [r[0] for r in cursor]
        cursor.close()
        return iscr

if __name__ == '__main__':
    dao = CorsoDAO()
    corsi = dao.get_methods()
    for s in corsi:
        print(s)