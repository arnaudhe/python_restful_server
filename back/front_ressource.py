import sys
import os.path

from restful_server_exception import *

class FrontRessource():

    def __init__(self, services):
        self.services = services

    def add(self, header_args):
        raise RestfulServerMethodNotAllowed()

    def update(self, url_args, header_args):
        raise RestfulServerMethodNotAllowed()

    def delete(self, url_args, header_args):
        raise RestfulServerMethodNotAllowed()

    def get(self, url_args):
        try:
            filename = self.services.get('server').get_front_path() + url_args['ressource']
            f = open(filename)
        except IOError:
            raise RestfulServerNotFound()
        else:
            with f:
                return f.read()

class FrontRessourceRoot():

    VIEW_PATH = 'index.html'

    def __init__(self, services):
        self.services = services

    def get(self, url_args):
        try:
            filename = os.path.join(self.services.get('server').get_front_path(), self.VIEW_PATH)
            f = open(filename)
        except IOError:
            raise RestfulServerNotFound()
        else:
            with f:
                return f.read()
