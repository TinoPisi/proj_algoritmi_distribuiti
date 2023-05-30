import time
import pwinput

class Person(object):

    def __init__(self, logger, name):
        """
        Questa funzione inizializza un oggeto con un attributo name che prova ad effettuare il login mediante 
        la funzione .login_funcion
        
        :param logger: È un progetto che ha il metodo login_function. Questo permette di autenticare l'utente con 
        le sue credenziali 
        :param name: Il parametro "name" è una stringa che viene passata come argomento al costruttore della classe.
        È utilizzato per inizializzare l'attributo "self.name". Contiene il nome dell'utente che vuole autenticarsi 
        """

        self.name = ""
        print("Inserire la password per l'utente {0}: ".format(name))
        psw = pwinput.pwinput()
        result = logger.login_function(name, psw)
        if result:
            self.name = name

    def deposit(self, piazzale):
        """
        La funzione permette all'utente di depositare un materiale e stampa un messaggio di successo o di errore a 
        seconda dell'esito dipendente dalla validità dell'input.
        
        :param piazzale: Il parametro "piazzale" è un oggetto che permette di interfacciarsi con il piazzale. 
        Si utilizza il metodo "deposit" per memorizzare un materiale all'interno del piazzale.
        """

        print("Il piazzale contiene:", piazzale.list_contents())
        item = input("Cosa vuoi aggiungere? ").strip()
        if item:
            result = piazzale.store(self.name, item)
        if result:
            print("{0} depositato con successo - {1}".format(item, time.strftime("%H.%M %d/%m/%Y")))
        else:
            print("Errore durante l'inserimento. Controllare l'input e riprovare")
    
    def info(self, piazzale):
        """
        La funzione "info" stampa il conenuto del piazzale e permette all'utente di cercare le informazioni relative ad
        uno, o più in caso di nomi uguali, materiali in esso memorizzati.

        :param piazzale: Il parametro "piazzale" è un oggetto che rappresenta il piazzale. È utilizzato nel metodo 
        "info" per recuereare le informazioni realtive al materiale.
        """

        print("Il piazzale contiene:", piazzale.list_contents())
        item = input("Digita il materiale di cui vuoi le informazioni: ").strip()
        if item:
            result = piazzale.get_material_info(self.name, item)
        print("Materiale trovato: ")
        if result:
            print(result)
            for r in result:
                print(r)
    
    def retrieve(self, piazzale):
        """
        La funzione recupera un materiale dal piazzale e stampa un messaggio di successo o di errore a seconda della
        effettiva presenza.
        
        :param piazzale: Il parametro "piazzale" è un oggetto che rappresenta il piazzale. È utilizzato nel metodo 
        "info" per recuereare le informazioni realtive al materiale. Utilizza il metodo "retrieve" per accedere alla lista
        dei materiali e ne rimuove quindi uno da esso.
        """
        print("Il piazzale contiene:", piazzale.list_contents())
        item = input("Digita qualcosa che vuoi prelevare: ").strip()
        if item:
            result = piazzale.take(self.name, item)
        if result:
            print("{0} prelevato con successo - {1}".format(item, time.strftime("%H.%M %d/%m/%Y")))
        else:
            print("Oggetto non presente")
    
    def login(self, logger):
        """
        The function prompts the user to input a username and strips any leading or trailing whitespace.
        
        :param logger: The logger parameter is a variable that represents a logging object. It is likely used to log information
        about the login process, such as whether it was successful or not, any errors that occurred, or any other relevant
        information
        """
        user = input("Digita il nome utente: ").strip()
    
