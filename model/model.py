from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio
import mysql.connector

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile
        self.lista_auto=[]

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """
        try:
            cnx=get_connection()  # usa la funzione che legge i dati da connector.cnf
            if cnx is None:
                raise Exception("Connessione al database fallita")

            cursor = cnx.cursor()
            query = "SELECT id, modello, marca, targa, anno, prezzo_giornaliero FROM automobile"
            cursor.execute(query)

            for row in cursor:
                id = row[0]
                modello = row[1]
                marca = row[2]
                targa = row[3]
                anno = row[4]
                prezzo = row[5]
                auto = Automobile(id, modello, marca, targa, anno, prezzo)
                self.lista_auto.append(auto)

            cursor.close()
            cnx.close()

            return self.lista_auto

        except Exception as e:
            print(f"Errore durante la lettura delle automobili: {e}")

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        lista_auto = []
        try:
            cnx = get_connection()
            if cnx is None:
                raise Exception("Connessione al database non riuscita.")

            cursor = cnx.cursor()
            query = ("SELECT id, modello, marca, targa, anno, prezzo_giornaliero "
                     "FROM automobile WHERE modello LIKE %s")
            cursor.execute(query, (f"%{modello}%",))

            for row in cursor:
                id = row[0]
                modello_restituito = row[1]
                marca = row[2]
                targa = row[3]
                anno = row[4]
                prezzo = row[5]
                auto = Automobile(id, modello_restituito, marca, targa, anno, prezzo)
                lista_auto.append(auto)

            cursor.close()
            cnx.close()
            return lista_auto

        except Exception as e:
            raise Exception(f"Errore durante la ricerca per modello: {e}")