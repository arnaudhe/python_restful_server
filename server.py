import sys

sys.path.append("back")
sys.path.append("front")

import cgi
import time
import threading
import os.path

from BaseHTTPServer           import BaseHTTPRequestHandler, HTTPServer
from urlparse                 import urlparse, parse_qs
from service_provider         import ServicesProvider
from restful_server_exception import *

class HTTPHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        path  = urlparse(self.path).path
        print("GET " + path)
        
        try:
            sp = ServicesProvider()
            contents = sp.get('back.router').do_GET(path)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(contents)
        except RestfulServerException as e:
            print 'HTTP error : {}'.format(e.get_message())
            self.send_response(e.get_code())
            self.end_headers()
            self.wfile.write('HTTP error : {}'.format(e.get_message()))

    def do_POST(self):

        print("Just received a POST request")

        form = cgi.FieldStorage(fp      = self.rfile,
                                headers = self.headers,
                                environ = {'REQUEST_METHOD' : 'POST'})
        args = {}

        for i in form:
            args[i] = form.getvalue(i)

        try:
            sp = ServicesProvider()
            contents = sp.get('back.router').do_POST(self.path, args)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(contents)
        except RestfulServerException as e:
            print 'HTTP error : {}'.format(e.get_message())
            self.send_response(e.get_code())
            self.end_headers()
            self.wfile.write('HTTP error : {}'.format(e.get_message()))

    def do_DELETE(self):

        print("Just received a DELETE request")

        try:
            sp = ServicesProvider()
            contents = sp.get('back.router').do_DELETE(self.path)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(contents)
        except RestfulServerException as e:
            print 'HTTP error : {}'.format(e.get_message())
            self.send_response(e.get_code())
            self.end_headers()
            self.wfile.write('HTTP error : {}'.format(e.get_message()))

    def do_PATCH(self):

        print("Just received a PATCH request")

        args = cgi.FieldStorage(fp      = self.rfile,
                                headers = self.headers,
                                environ = {'REQUEST_METHOD' : 'PATCH'})

        try:
            sp = ServicesProvider()
            contents = sp.get('back.router').do_PATCH(self.path, args)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(contents)
        except RestfulServerException as e:
            print 'HTTP error : {}'.format(e.get_message())
            self.send_response(e.get_code())
            self.end_headers()
            self.wfile.write('HTTP error : {}'.format(e.get_message()))

    def do_PUT(self):

        print("Just received a PUT request")

        args = cgi.FieldStorage(fp      = self.rfile,
                                headers = self.headers,
                                environ = {'REQUEST_METHOD' : 'PUT'})

        try:
            sp = ServicesProvider()
            contents = sp.get('router').do_PUT(self.path, args)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(contents)
        except RestfulServerException as e:
            print 'HTTP error : {}'.format(e.get_message())
            self.send_response(e.get_code())
            self.end_headers()
            self.wfile.write('HTTP error : {}'.format(e.get_message()))

class RestfulServer(HTTPServer, object):

    def __init__(self, port):
        super(RestfulServer, self).__init__(('0.0.0.0', port), HTTPHandler)
        self.sp = ServicesProvider(self)

    def start(self):
        thread = threading.Thread(target = self.serve_forever)
        thread.daemon = True
        thread.start()

    def stop(self):
        self.shutdown()

    def get_root_path(self):
        return os.path.dirname(__file__)

    def get_front_path(self):
        return os.path.join(os.path.dirname(__file__), 'front')

    def get_back_path(self):
        return os.path.join(os.path.dirname(__file__), 'back')

if __name__ == "__main__":
    server = RestfulServer(8000)
    try:
        server.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('SigTerm received, shutting down server')
        sys.exit(0)