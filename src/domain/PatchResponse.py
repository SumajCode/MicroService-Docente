from infra.controllers.errors.ErrorsClients import APIHTTPExceptionsClient
from infra.controllers.errors.ErrorsServer import APIHTTPExceptionsServer
from infra.db.Query import actualizar

from scripts.execute import Ejecutar
from scripts.formater import Formater

class RespuestaPatch:

    def __init__(self):
        self.ejecutor = Ejecutar()
        self.formater = Formater()

    def rpatch(self, datos):
        try:
            if datos['idEditar'] is not None and datos['nombreTabla'] is not None and datos['datos'] is not None:
                return self.formater.json(self.ejecutor.ejecutarConsulta(actualizar(datos['idEditar'], datos['nombreTabla'], datos['datos'])))
        except APIHTTPExceptionsClient and APIHTTPExceptionsServer as excep:
            return self.formater.json({
                'message' : excep.description,
                'status' : excep.code
            })