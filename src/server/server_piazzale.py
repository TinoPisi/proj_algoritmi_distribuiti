from Pyro5.api import expose, behavior, serve
import sys
from material import Material
import time

material = ["trave", "arco", "bidone", "scala", "palo"]

@expose
@behavior(instance_mode="single")
class Piazzale(object):
    def __init__(self):
        """
        Questa funzione inizializza un oggetto con un elenco di oggetti Materiale creati da un determinato elenco di 
        materiali e un nome utente fisso.
        """
        self.contents = []
        for obj in material:
            self.contents.append(Material(obj, "Valentino"))
        
    def list_contents(self):
        """
        Questa funzione restituisce un elenco di nomi di Materiali nel piazzale.
        :return: Il metodo `list_contents` restituisce un elenco di nomi degli oggetti nell'elenco `contents`, ovvero i 
        Materiali memorizzati nel server.
        """
        result = []
        for obj in self.contents:
            result.append(obj.name)
        return result

    def take(self, name, item):
        """
        La funzione prende un elemento dal server_piazzale e stampa un messaggio sull'azione, restituendo True in caso di 
        successo e False in caso contrario.
        
        :param name: Il nome della persona che prende l'elemento dal piazzale
        :param item: Il parametro "item" è il nome dell'elemento che l'utente vuole prelevare 
        :return: un valore booleano, True o False, a seconda che l'elemento sia stato rimosso con successo dal server
        dei contenuti o meno.
        """
        try:
            for x in self.contents:
                if x.name == item:
                    remove = x
            self.contents.remove(remove)
            print("{0}: {2} ha prelevato {1}.".format(time.strftime("%d/%m/%Y %H.%M"), item, name))
            result = True
        except:
            print("ERRORE PRELIEVO. INPUT: {0}; UTENTE {1}; ORARIO: {2}".format(item, name, time.strftime("%d/%m/%Y %H.%M")))
            result = False
        return result

    def store(self, name, item):
        """
        The function stores an item with a given name and user, and returns True if successful or False if there is an error.
        
        :param name: The name of the person who is storing the item
        :param item: The item parameter is the name or identifier of the material being stored
        :return: a boolean value, either True or False, depending on whether the item was successfully added to the contents
        list or not.
        """
        try:
            self.contents.append(Material(item, name))
            print("{0}: {2} inserito da {1}.".format(time.strftime("%d/%m/%Y %H.%M"), name, item))
            result = True
        except:
            print("ERRORE PRELIEVO. INPUT: {0}; UTENTE {1}; ORARIO: {2}".format(item, name, time.strftime("%d/%m/%Y %H.%M")))
            result = False
        return result

    
    def get_material_info(self, name, item):
        """
        Questa funzione cerca un articolo specifico in un elenco e restituisce informazioni sui materiali relativi a 
        quell'articolo.

        :param name: Il nome della persona che sta cercando le informazioni materiali
        :param item: Il parametro item è una stringa che rappresenta il nome del materiale ricercato
        :return: un elenco di informazioni sui materiali che corrispondono al nome dell'elemento dato, ottenuto dai contenuti
        dell'oggetto. 
        La funzione stampa anche un messaggio che indica l'elemento cercato, il nome della persona che ha eseguito
        la ricerca e la data e l'ora della ricerca.
        """
        materials = []
        for x in self.contents:
             if x.name == item:
                 materials.append(x.get_info())
        print("{2}: Materiale cercato: {0}; Ricerca effettuata da: {1}".format(item, name,time.strftime("%d/%m/%Y %H.%M")))
        return materials
    
serve(
    {
        Piazzale: "zp.piazzale"
    },
    use_ns=True)
