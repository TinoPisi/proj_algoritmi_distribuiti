import sys
import os
import Pyro5.errors
from Pyro5.api import Proxy
from server.person import Person

sys.excepthook = Pyro5.errors.excepthook

piazzale = Proxy("PYRONAME:zp.piazzale")
logger = Proxy("PYRONAME:zp.logger")

def selection_menu():
    """
    La funzione stampa un menu con 3 voci e ritorna la scelta dell'utente come un integer.
    :return: valore intero con la voce selezionata dall'utente.
    """
    check_value = True
    while check_value:
        try:
            option = int(input("Benvenuto nel sistema di ZP: \n 1: Deposita materiale; \n "
                            "2: Preleva materiale; \n 3: Ottieni informazioni; \n 0: Termina \nScelta: ").strip())
            check_value = False
        except:
            print("ERRORE: valore errato")
    return option

logged = False
while not logged:
    name = input("Inserire lo username: ").strip()
    worker = Person(logger, name)
    if worker.name == "":
        print("Username e/o Password errate")
    else:
        print("Utente loggato: {0}".format(worker.name))
        logged = True

option = selection_menu()
while option != 0:
    match option:
        case 1:
            worker.deposit(piazzale)
            pass
        case 2:
            worker.retrieve(piazzale)
            pass
        case 3:
            worker.info(piazzale)
            pass
    option = selection_menu()