from src.infra.controllers.errors.ErrorsClients import APIHTTPExceptionsClient
from src.infra.controllers.errors.ErrorsServer import APIHTTPExceptionsServer

from src.scripts.formater import Formater
from src.scripts.execute import Ejecutar
from src.infra.db.Query import insertarEnTabla

class RespuestaPost:

    def __init__(self):
        self.ejecutor = Ejecutar()
        self.formater = Formater()

    def rpost(self, data):
        """
        Maneja la respuesta para una peticion POST.

        Devuelve un JSON con los datos de la respuesta de la consulta, si no
        hubo errores en la consulta. Si hubo errores, devuelve un JSON con
        el mensaje de error y el codigo de estado.

        :param data: Diccionario con los datos de la peticion.
        :type data: dict
        :return: Un JSON con los datos de la respuesta de la consulta.
        :rtype: json
        """
        try:
            data = self.ejecutor.ejecutarConsulta(insertarEnTabla(data['tabla'], data['datos']))
            return self.formater.json(data)
        except APIHTTPExceptionsClient and APIHTTPExceptionsServer as excep:
            return self.formater.json({
                'message' : excep.description,
                'status' : excep.code
            })