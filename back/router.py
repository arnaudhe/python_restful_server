import sys
import re
import json

from restful_server_exception import *

class Router():

    routes = [{'method' : 'GET'   , 'path' : '(?P<ressource>\/.+\.(?:png|jpeg|jpg|css|js))$' , 'service' : 'front.ressource', 'function' : 'get'},
              {'method' : 'GET'   , 'path' : '\/sentences$'                                  , 'service' : 'back.sentences' , 'function' : 'get_all'},
              {'method' : 'GET'   , 'path' : '\/sentences\/(?P<id>[0-9]+)$'                  , 'service' : 'back.sentences' , 'function' : 'get'},
              {'method' : 'POST'  , 'path' : '\/sentences$'                                  , 'service' : 'back.sentences' , 'function' : 'add'},
              {'method' : 'DELETE', 'path' : '\/sentences\/(?P<id>[0-9]+)$'                  , 'service' : 'back.sentences' , 'function' : 'delete'},
              {'method' : 'POST'  , 'path' : '\/sentences\/(?P<id>[0-9]+)\/increment$'       , 'service' : 'back.sentences' , 'function' : 'increment'},
              {'method' : 'GET'   , 'path' : '\/$'                                           , 'service' : 'front.home'     , 'function' : 'get'}]

    def __init__(self, services):
        self.services = services

    def call_method(o, name):
        getattr(o, name)()

    def do_GET(self, path):
        for route in self.routes:
            url_args = re.match(route['path'], path)
            if ((url_args) and (route['method'] == 'GET')):
                try:
                    return getattr(self.services.get(route['service']), route['function'])(**url_args.groupdict())
                except AttributeError:
                    raise RestfulServerBadRequest()
        raise RestfulServerNotFound()

    def do_POST(self, path, header_args):
        for route in self.routes:
            url_args = re.match(route['path'], path)
            if ((url_args) and (route['method'] == 'POST')):
                try:
                    return getattr(self.services.get(route['service']), route['function'])(**url_args.groupdict(), header_args)
                except AttributeError:
                    raise RestfulServerBadRequest()
        raise RestfulServerNotFound()

    def do_DELETE(self, path):
        for route in self.routes:
            url_args = re.match(route['path'], path)
            if ((url_args) and (route['method'] == 'DELETE')):
                try:
                    return getattr(self.services.get(route['service']), route['function'])(**url_args.groupdict())
                except AttributeError:
                    raise RestfulServerBadRequest()
        raise RestfulServerNotFound()

    def do_PATCH(self, path, header_args):
        for route in self.routes:
            url_args = re.match(route['path'], path)
            if ((url_args) and (route['method'] == 'PATCH')):
                try:
                    return getattr(self.services.get(route['service']), route['function'])(**url_args.groupdict(), header_args)
                except AttributeError:
                    raise RestfulServerBadRequest()
        raise RestfulServerNotFound()

    def do_PUT(self, path, header_args):
        for route in self.routes:
            url_args = re.match(route['path'], path)
            if ((url_args) and (route['method'] == 'PUT')):
                try:
                    return getattr(self.services.get(route['service']), route['function'])(**url_args.groupdict(), header_args)
                except AttributeError:
                    raise RestfulServerBadRequest()
        raise RestfulServerNotFound()
