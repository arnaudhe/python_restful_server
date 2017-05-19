from sentences_collection     import SentencesCollection
from front_ressource          import FrontRessource, FrontRessourceRoot
from router                   import Router
from restful_server_exception import *

class Singleton(type):

    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class ServicesProvider(object):

    __metaclass__ = Singleton

    services      = {}

    def __init__(self, server):
        self.services['server']          = server
        self.services['front.home']      = FrontRessourceRoot(self)
        self.services['front.ressource'] = FrontRessource(self)
        self.services['back.sentences']  = SentencesCollection()
        self.services['back.router']     = Router(self)

    def has(self, service):
        if (service in self.services):
            return True
        else:
            return False

    def get(self, service):
        if (self.has(service)):
            return self.services[service]
        else:
            raise RestfulServerInternalServerError()

if __name__ == "__main__":
    sp = ServicesProvider()
    print (sp)
    print sp.has('router')
    print sp.has('front.home')
    print sp.has('bibi')
    sp2 = ServicesProvider()
    print (sp2)