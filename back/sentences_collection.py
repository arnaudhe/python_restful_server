import sys
import os.path
import json

from restful_server_exception     import *
from restful_ressource_collection import RestfulRessourceCollection

class SentencesCollection(RestfulRessourceCollection):

    NAME   = 'sentences'
    SCHEMA = { 'sentence' : '-', 'person' : '-', 'date' : 'dd-mm-yyyy', 'vote' : 0}

    def __init__(self):
        super(SentencesCollection, self).__init__(self.NAME, self.SCHEMA)

    def increment(self, id):
        if id < len(self._list):
            self._list[id].set_attribute('vote', self._list[id].get_attribute('vote') + 1)
            return self.get_all()
        else:
            raise RestfulServerNotFound()