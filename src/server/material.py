import uuid
import time

class Material(object):
    def __init__(self, name, name_person):
        """
        Questa funzione inizializza un oggetto Material con ID univoco, nome, data di arrivo e nome della persona che lo ha inserito.

        :param name: Il nome dell'oggetto da inizializzare
        :param name_person: Il nome della persona che sta inserendo i dati
        """
        self.id = uuid.uuid4()
        self.name = name
        self.arrive_date = time.strftime("%d/%m/%Y %H.%M")
        self.inserted_by = name_person

    def get_info(self):
        """
        Questa funzione restituisce una stringa contenente informazioni sul nome di un oggetto, id, data di arrivo e chi l'ha inserito.
        :return: Una stringa contenente nome, id, data di arrivo e nome della persona che ha inserito le informazioni. 
        La stringa viene formattata utilizzando i valori degli attributi corrispondenti dell'oggetto.
        """
        return str("{0} - {1} - {2}, Inserito da: {3}.".format(self.name, self.id, self.arrive_date, self.inserted_by))
