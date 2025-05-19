from werkzeug.exceptions import HTTPException

class APIHTTPExceptionsClient(HTTPException):
    def __init__(self):
        pass

    def invalidAccess(self):
        self.code = 403
        self.description = 'Acceso del usuario no autorizado al sistema.'

    def invalidUser(self):
        self.code = 401
        self.description = 'Autenticación del usuario necesaria.'

    def notFound(self):
        self.code = 404
        self.description = 'Recurso solicitado no encontrado.'

    def badRequest(self):
        self.code = 400
        self.description = 'Solicitud incorrecta.'

    def methodNotAllowed(self):
        self.code = 405
        self.description = 'Tipo de método no aceptable.'

    def petitionFailed(self):
        self.code = 412
        self.description = 'El servidor no cumple con las condiciones que requiere.'

    def payloadLarge(self):
        self.code = 413
        self.description = 'El contenido de la solicitud es demasiado grande.'
