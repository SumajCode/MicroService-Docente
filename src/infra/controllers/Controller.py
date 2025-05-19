from flask import jsonify

from .errors.ErrorsClients import APIHTTPExceptionsClient
from .errors.ErrorsServer import APIHTTPExceptionsServer

from ...scripts.execute import Ejecutar
from ..db.Query import *

class Controller:

    def __init__(self):
        self.ejecutor = Ejecutar()

    def get(self, datosObtenidos=None, opciones: dict=None):
        datos = {}
        try:
            if datosObtenidos is None and 'tabla' in opciones:
                temporalDatos = self.ejecutor.ejecutar(ordenarPor(
                    opciones['tabla'],
                    opciones['columnas'],
                    opciones['columnaOrden'],
                    opciones['ascen'],
                    opciones['descen'],
                    opciones['columnaAgrupar']
                ))
                columnas = opciones['columnas']
                # for i in temporalDatos:

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
            data = self.ejecutor.ejecutar(insertarEnTabla(data['tabla'], data['datos']))
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