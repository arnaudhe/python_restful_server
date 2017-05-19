import sys
import os.path
import json
import abc
import make_json_serializable

from restful_ressource        import RestfulRessource
from restful_server_exception import *

class RestfulRessourceCollection():
    __metaclass__ = abc.ABCMeta

    _name      = ''
    _save_file = ''
    _list      = []
    _schema    = {}

    def load(self):
        if (os.path.isfile(self._save_file)):
            with open(self._save_file, 'r') as save_file:
                self._list = [RestfulRessource(attr) for attr in json.loads(save_file.read())]

    def save(self):
        with open(self._save_file, 'w') as save_file:
            save_file.write(json.dumps(self))

    def __init__(self, name, schema):

        self._name      = name
        self._schema    = schema
        self._save_file = os.path.join(os.path.dirname(__file__), '{}_save.json'.format(self._name))

        self.load()

    def add(self, url_args, header_args):
        ressource = RestfulRessource(self._schema)
        print ressource
        ressource.update(header_args)
        self._list.append(ressource)
        self.save()
        print str(self)
        return self.get_all(url_args)

    def update(self, url_args, header_args):
        id = int(url_args['id'])
        if id < len(self._list):
            self._list[id].update(header_args)
            self.save()
            return self.get_all(url_args)
        else:
            raise RestfulServerNotFound()

    def delete(self, url_args):
        id = int(url_args['id'])
        if id < len(self._list):
            self._list.pop(id)
            self.save()
            return self.get_all(url_args)
        else:
            raise RestfulServerNotFound()
        
    def get(self, url_args):
        id = int(url_args['id'])
        if id < len(self._list):
            return json.dumps(self._list[id])
        else:
            raise RestfulServerNotFound()

    def to_json(self):
        return self._list

    def __str__(self):
        return str([str(ressource) for ressource in self._list])

    def get_all(self, url_args):
        return json.dumps(self._list)
