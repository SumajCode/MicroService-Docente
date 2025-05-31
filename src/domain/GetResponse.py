from infra.controllers.errors.ErrorsClients import APIHTTPExceptionsClient
from infra.controllers.errors.ErrorsServer import APIHTTPExceptionsServer

from scripts.execute import Ejecutar
from scripts.formater import Formater
from infra.db.Query import ordenarPor

class RespuestaGet:

    def __init__(self):
        self.ejecutor = Ejecutar()
        self.formater = Formater()
    
    def getDatosDB(self, opciones):
        if opciones['columnas'] is not None:
            temporalDatos = self.ejecutor.ejecutarConsulta(ordenarPor(
                    opciones['tabla'],
                    opciones['columnas'],
                    opciones['columnaOrden'],
                    opciones['asc'],
                    opciones['desc'],
                    opciones['columnaAgrupar']
                ))
        return self.formater.json(self.formater.formatoResSQL(opciones['columnas'], temporalDatos))

    def getDatosDBJoin(self, opciones, condiciones):
        datos=[]
        if opciones['columnas'] is not None:
            # temporalDatos = self.ejecutor.ejecutarConsulta(seleccionarJoin(
            #         opciones['tabla'],
            #         opciones['columnas'],
            #         opciones['columnaOrden'],
            #         opciones['asc'],
            #         opciones['desc'],
            #         opciones['columnaAgrupar']
            #     ))
            pass
        return self.formater.json(self.formater.formatoResSQL(opciones['columnas']
                                                            #   , temporalDatos
                                                              ))

    def rget(self, datos):
        try:
            datosObtenidos = datos['datosObtenidos']
            opciones = datos['opciones']
            condiciones = datos['condiciones']
            if datosObtenidos is None and 'tabla' in opciones.keys():
                return self.getDatosDB(opciones)
            # if condiciones is not None:
            #     return self.getDatosDBJoin(opciones, condiciones)
            return self.formater.json(datosObtenidos)
        except (APIHTTPExceptionsClient and APIHTTPExceptionsServer) as excep:
            return self.json({
                'message' : excep.description,
                'status' : excep.code
            })