from flask import jsonify

from .errors.ErrorsClients import APIHTTPExceptionsClient
from .errors.ErrorsServer import APIHTTPExceptionsServer

from ...scripts.execute import Ejecutar
from ..db.Query import *

class Controller:

    def __init__(self):
        self.ejecutor = Ejecutar()

    def get(self, datosObtenidos=None, opciones: dict=None):
        datos = []
        try:
            if datosObtenidos is None and 'tabla' in opciones.keys():
                temporalDatos = self.ejecutor.ejecutarConsulta(ordenarPor(
                    opciones['tabla'],
                    opciones['columnas'],
                    opciones['columnaOrden'],
                    opciones['asc'],
                    opciones['desc'],
                    opciones['columnaAgrupar']
                ))
                if opciones['columnas'] is not None:
                    columnas = opciones['columnas']
                    for fila in temporalDatos:
                        datosEstructurados = {}
                        for nombreColumna in columnas:
                            datosEstructurados[nombreColumna] = fila[nombreColumna]
                        datos.append(datosEstructurados)
                return jsonify({
                    'data': datos,
                    'message' : 'OK',
                    'status' : 200
                })
            return jsonify({
                'data': datosObtenidos,
                'message' : 'OK',
                'status' : 200
            })
            
        except APIHTTPExceptionsClient and APIHTTPExceptionsServer as e:
            return jsonify({
                'message' : e.description,
                'status' : e.code
            })

    def post(self, data):
        try:
            data = self.ejecutor.ejecutarConsulta(insertarEnTabla(data['tabla'], data['datos']))
            return jsonify({
                'data': data,
                'message' : 'OK',
                'status' : 200
            })
        except APIHTTPExceptionsClient and APIHTTPExceptionsServer as e:
            return jsonify({
                'message' : e.description,
                'status' : e.code
            })

    def patch(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass