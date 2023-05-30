from Pyro5.api import expose, behavior, serve
import sys
from material import Material
import time

material = ["chair", "bike", "flashlight", "laptop", "couch"]

@expose
@behavior(instance_mode="single")
class Piazzale(object):
    def __init__(self):
        self.contents = []
        for obj in material:
            self.contents.append(Material(obj, "Valentino"))
        
    def list_contents(self):
        result = []
        for obj in self.contents:
            result.append(obj.name)
        return result

    def take(self, name, item):
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
        try:
            self.contents.append(Material(item, name))
            print("{0}: {2} inserito da {1}.".format(time.strftime("%d/%m/%Y %H.%M"), name, item))
            result = True
        except:
            print("ERRORE PRELIEVO. INPUT: {0}; UTENTE {1}; ORARIO: {2}".format(item, name, time.strftime("%d/%m/%Y %H.%M")))
            result = False
        return result

    
    def get_material_info(self, name, item):
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
