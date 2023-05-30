from Pyro5.api import expose, behavior, serve


@expose
@behavior(instance_mode="single")
class Logger(object):
    def __init__(self):
        """
        Funzione constructor che inizializza una lista di nomi come account autorizzati
        """
        self.personale = ["Valentino", "Dante", "Francesco", "Andrea", "Simone"]

    def login_function(self, name, psw):
        """
        La funzione verifica se il nome e la password forniti corrispondono a qualsiasi utente in un elenco e restituisce 
        un valore booleano di conseguenza.

        :param name: Il nome utente inserito dall'utente che tenta di accedere
        :param psw: "psw" è l'abbreviazione di "password". È uno dei parametri del metodo "login_function", che accetta
        due parametri: "nome" e "psw". Il metodo controlla se c'è un utente nella lista "personale" con il "nome" dato e
        :return: un valore booleano (True o False) a seconda che il nome e la password immessi corrispondano a qualsiasi utente nell'elenco di
        personale.
        """
        result = False
        for user in self.personale:
            if user == name and name == psw:
                result = True
        return result
    
serve(
    {
        Logger: "zp.logger"
    },
    use_ns=True)
