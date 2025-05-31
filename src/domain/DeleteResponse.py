from infra.controllers.errors.ErrorsClients import APIHTTPExceptionsClient
from infra.controllers.errors.ErrorsServer import APIHTTPExceptionsServer

from scripts.execute import Ejecutar
from scripts.formater import Formater
from infra.db.Query import eliminarDeTabla

class RespuestaDelete:

    def __init__(self):
        self.ejecutor = Ejecutar()
        self.formater = Formater()

    def rdelete(self, datos):
        try:
            if datos['idEliminar'] is not None and datos['nombreTabla'] is not None:
                return self.formater.json(self.ejecutor.ejecutarConsulta(eliminarDeTabla(datos['nombreTabla'], datos['idEliminar'])))
        except APIHTTPExceptionsClient and APIHTTPExceptionsServer as excep:
            return self.formater.json({
                'message' : excep.description,
                'status' : excep.code
            })