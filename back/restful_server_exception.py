HTTP_CODES =   {100 : 'CONTINUE',                        \
                101 : 'SWITCHING PROTOCOLS',             \
                102 : 'PROCESSING',                      \
                200 : 'OK',                              \
                201 : 'CREATED',                         \
                202 : 'ACCEPTED',                        \
                203 : 'NON AUTHORITATIVE INFORMATION',   \
                204 : 'NO CONTENT',                      \
                205 : 'RESET CONTENT',                   \
                206 : 'PARTIAL CONTENT',                 \
                207 : 'MULTI STATUS',                    \
                208 : 'ALREADY REPORTED',                \
                226 : 'IM USED',                         \
                300 : 'MULTIPLE CHOICES',                \
                301 : 'MOVED PERMANENTLY',               \
                302 : 'FOUND',                           \
                303 : 'SEE OTHER',                       \
                304 : 'NOT MODIFIED',                    \
                305 : 'USE PROXY',                       \
                307 : 'TEMPORARY REDIRECT',              \
                308 : 'PERMANENT REDIRECT',              \
                400 : 'BAD REQUEST',                     \
                401 : 'UNAUTHORIZED',                    \
                402 : 'PAYMENT REQUIRED',                \
                403 : 'FORBIDDEN',                       \
                404 : 'NOT FOUND',                       \
                405 : 'METHOD NOT ALLOWED',              \
                406 : 'NOT ACCEPTABLE',                  \
                407 : 'PROXY AUTHENTICATION REQUIRED',   \
                408 : 'REQUEST TIMEOUT',                 \
                409 : 'CONFLICT',                        \
                410 : 'GONE',                            \
                411 : 'LENGTH REQUIRED',                 \
                412 : 'PRECONDITION FAILED',             \
                413 : 'REQUEST ENTITY TOO LARGE',        \
                414 : 'REQUEST URI TOO LONG',            \
                415 : 'UNSUPPORTED MEDIA TYPE',          \
                416 : 'REQUEST RANGE NOT SATISFIABLE',   \
                417 : 'EXPECTATION FAILED',              \
                422 : 'UNPROCESSABLE ENTITY',            \
                423 : 'LOCKED',                          \
                424 : 'FAILED DEPENDENCY',               \
                426 : 'UPGRADE REQUIRED',                \
                428 : 'PRECONDITION REQUIRED',           \
                429 : 'TOO MANY REQUESTS',               \
                431 : 'REQUEST HEADER FIELDS TOO LARGE', \
                500 : 'INTERNAL SERVER ERROR',           \
                501 : 'NOT IMPLEMENTED',                 \
                502 : 'BAD GATEWAY',                     \
                503 : 'SERVICE UNAVAILABLE',             \
                504 : 'GATEWAY TIMEOUT',                 \
                505 : 'HTTP VERSION NOT SUPPORTED',      \
                506 : 'VARIANT ALSO NEGOTIATES',         \
                507 : 'INSUFFICIENT STORAGE',            \
                508 : 'LOOP DETECTED',                   \
                510 : 'NOT EXTENDED',                    \
                511 : 'NETWORK AUTHENTICATION REQUIRED'}

class RestfulServerException(Exception):

    _code    = 0
    _message = ""

    def __init__(self, code):

        self._code  = int(code)
        
        if code in HTTP_CODES:
            self._message = '{} - {}'.format(code, HTTP_CODES[code])
        else:
            self._message = '{} - {}'.format(code, "Unknown HTTP code")

        # Call the base class constructor with the parameters it needs
        super(RestfulServerException, self).__init__(self._message)


    def get_code(self):
        return self._code

    def get_message(self):
        return self._message


class RestfulServerUnauthorized(RestfulServerException): 
    def __init__(self):
        super(RestfulServerUnauthorized, self).__init__(401)

class RestfulServerForbidden(RestfulServerException): 
    def __init__(self):
        super(RestfulServerForbidden, self).__init__(403)

class RestfulServerNotFound(RestfulServerException):
    def __init__(self):
        super(RestfulServerNotFound, self).__init__(404)

class RestfulServerMethodNotAllowed(RestfulServerException):
    def __init__(self):
        super(RestfulServerMethodNotAllowed, self).__init__(405)

class RestfulServerInternalServerError(RestfulServerException):
    def __init__(self):
        super(RestfulServerInternalServerError, self).__init__(500)

class RestfulServerNotImplemented(RestfulServerException): 
    def __init__(self):
        super(RestfulServerNotImplemented, self).__init__(501)
