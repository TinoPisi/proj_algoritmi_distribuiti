# This is the code that visits the warehouse.
import sys
import Pyro5.errors
from Pyro5.api import Proxy
from person import Person


sys.excepthook = Pyro5.errors.excepthook

warehouse = Proxy("PYRONAME:zp.piazzale")
janet = Person("Janet")

def selection_menu():
    option = int(input("Benvenuto nel sistema di ZP: \n 1: Deposita materiale; \n "
                       "2: Preleva materiale; \n 3: Ottieni informazioni; \n 0: Termina \nScelta: ").strip())
    return option

option = selection_menu()
while option != 0:
    match option:
        case 1:
            janet.deposit(warehouse)
            pass
        case 2:
            janet.retrieve(warehouse)
            pass
        case 3:
            janet.info(warehouse)
            pass
    option = selection_menu()
