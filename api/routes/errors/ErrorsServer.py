from werkzeug.exceptions import HTTPException

class ServerError(HTTPException):
    status = 500
    description = 'Error interno del servidor.'

class ImplementError(HTTPException):
    status = 501
    description = 'Metodo no implementado.'

class InfiniteLoopError(HTTPException):
    status = 508
    description = 'Bucle infinito detectado.'
