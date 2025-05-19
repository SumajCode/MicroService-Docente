from werkzeug.exceptions import HTTPException

class APIHTTPExceptionsServer(HTTPException):

    def __init__(self):
        pass

    def serverError(self):
        self.code = 500
        self.description = 'Error interno del servidor.'

    def implementError(self):
        self.code = 501
        self.description = 'Metodo no implementado.'

    def infiniteLoopError(self):
        self.code = 508
        self.description = 'Bucle infinito detectado.'
