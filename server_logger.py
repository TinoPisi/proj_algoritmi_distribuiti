from Pyro5.api import expose, behavior, serve
from material import Material
import time
import maskpass



@expose
@behavior(instance_mode="single")
class Logger(object):
    def __init__(self):
        self.personale = ["Valentino", "Dante", "Francesco", "Andrea", "Simone"]

    def login_function(self, name):
        for user in self.personale:
            if user == name:
                return True
            else:
                return False
    
serve(
    {
        Logger: "zp.logger"
    },
    use_ns=True)
