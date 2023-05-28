import sys
import Pyro5.errors
from Pyro5.api import Proxy
from person import Person
#from server_logger import Worker

sys.excepthook = Pyro5.errors.excepthook

warehouse = Proxy("PYRONAME:zp.piazzale")
logger = Proxy("PYRONAME:zp.logger")
#janet = Person("Janet")

def selection_menu():
    option = int(input("Benvenuto nel sistema di ZP: \n 1: Deposita materiale; \n "
                       "2: Preleva materiale; \n 3: Ottieni informazioni; \n 0: Termina \nScelta: ").strip())
    return option

logged = False
while not logged:
    name = input("Inserire lo username: ").strip()
    worker = Person(logger, name)
    if worker.name == "":
        print("Username e/o Password errate")
    else:
        print(worker.name)
        logged = True

option = selection_menu()
while option != 0:
    match option:
        case 1:
            worker.deposit(warehouse)
            pass
        case 2:
            worker.retrieve(warehouse)
            pass
        case 3:
            worker.info(warehouse)
            pass
    option = selection_menu()
