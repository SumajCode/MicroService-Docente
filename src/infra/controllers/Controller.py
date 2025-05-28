from flask import jsonify

from src.infra.controllers.errors.ErrorsClients import APIHTTPExceptionsClient
from src.infra.controllers.errors.ErrorsServer import APIHTTPExceptionsServer

from src.scripts.execute import Ejecutar
from src.infra.db.Query import ordenarPor, insertarEnTabla

class Controller:

    def __init__(self):
        self.ejecutor = Ejecutar()

    def get(self, datosObtenidos=None, opciones: dict=None):
        datos = []
        try:
            if datosObtenidos is None and 'tabla' in opciones.keys():
                print("if none")
                temporalDatos = self.ejecutor.ejecutarConsulta(ordenarPor(
                    opciones['tabla'],
                    opciones['columnas'],
                    opciones['columnaOrden'],
                    opciones['asc'],
                    opciones['desc'],
                    opciones['columnaAgrupar']
                ))
                if opciones['columnas'] is not None:
                    print("if none columns")
                    columnas = opciones['columnas']
                    for fila in temporalDatos:
                        datosEstructurados = {}
                        for nombreColumna in columnas:
                            datosEstructurados[nombreColumna] = fila[nombreColumna]
                        datos.append(datosEstructurados)
                    print("Jsonify datos de tabla")
                    return jsonify({
                        'data': datos,
                        'message' : 'OK',
                        'status' : 200
                    })
                return jsonify({
                    'data': temporalDatos,
                    'message' : 'OK',
                    'status' : 200
                })
            print("jsonify datos obtenidos")
            return jsonify({
                'data': datosObtenidos,
                'message' : 'OK',
                'status' : 200
            })
        except (APIHTTPExceptionsClient and APIHTTPExceptionsServer) as excep:
            return jsonify({
                'message' : excep.description,
                'status' : excep.code
            })

    def post(self, data):
        try:
            data = self.ejecutor.ejecutarConsulta(insertarEnTabla(data['tabla'], data['datos']))
            return jsonify({
                'data': data,
                'message' : 'OK',
                'status' : 200
            })
        except APIHTTPExceptionsClient and APIHTTPExceptionsServer as excep:
            return jsonify({
                'message' : excep.description,
                'status' : excep.code
            })

    def patch(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass