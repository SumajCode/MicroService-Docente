from werkzeug.exceptions import HTTPException

class InvalidAccess(HTTPException):
    code = 403
    description = 'Acceso del usuario no autorizado al sistema.'

class InvalidUser(HTTPException):
    code = 401
    description = 'Autenticación del usuario necesaria.'

class NotFound(HTTPException):
    code = 404
    description = 'Recurso solicitado no encontrado.'

class BadRequest(HTTPException):
    code = 400
    description = 'Solicitud incorrecta.'

class MethodNotAllowed(HTTPException):
    code = 405
    description = 'Tipo de método no aceptable.'

class PetitionFailed(HTTPException):
    code = 412
    description = 'El servidor no cumple con las condiciones que requiere.'

class PayloadLarge(HTTPException):
    code = 413
    description = 'El contenido de la solicitud es demasiado grande.'
