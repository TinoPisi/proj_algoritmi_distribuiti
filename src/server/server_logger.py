from Pyro5.api import expose, behavior, serve


@expose
@behavior(instance_mode="single")
class Logger(object):
    def __init__(self):
        self.personale = ["Valentino", "Dante", "Francesco", "Andrea", "Simone"]

    def login_function(self, name, psw):
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
