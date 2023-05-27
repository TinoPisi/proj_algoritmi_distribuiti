import time
from material import Material


class Person(object):
    def __init__(self, name):
        self.name = name

    def visit(self, warehouse):
        print("This is {0}.".format(self.name))
        self.deposit(warehouse)
        self.retrieve(warehouse)
        print("Thank you, come again!")

    def deposit(self, warehouse):
        print("Il piazzale contiene:", warehouse.list_contents())
        item = input("Cosa vuoi aggiungere? ").strip()
        if item:
            result = warehouse.store(self.name, item)
        if result:
            print("{0} depositato con successo - {1}".format(item, time.strftime("%H.%M %d/%m/%Y")))
        else:
            print("Errore durante l'inserimento. Controllare l'input e riprovare")
    
    def info(self, warehouse):
        print("Il piazzale contiene:", warehouse.list_contents())
        item = input("Digita il materiale di cui vuoi le informazioni: ").strip()
        if item:
            result = warehouse.get_material_info(self.name, item)
        
        if result:
            for r in result:
                print(r)
    
    def retrieve(self, warehouse):
        print("Il piazzale contiene:", warehouse.list_contents())
        item = input("Digita qualcosa che vuoi prelevare: ").strip()
        if item:
            result = warehouse.take(self.name, item)
        if result:
            print("{0} prelevato con successo - {1}".format(item, time.strftime("%H.%M %d/%m/%Y")))
        else:
            print("Oggetto non presente")
