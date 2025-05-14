from .errors.ErrorsServer import *
from flask import jsonify
from ..hooks.Compiler import *


# def get():
#     pass

class CodeController():
    def __init__(self):
        pass
    
    def post(self, codigo: str, lenguaje: str):
        """
        Realiza la compilacion de un codigo fuente en base a lenguaje
        especificado y devuelve el resultado de la compilacion.

        Parameters:
        codigo (str): Codigo fuente a compilar
        lenguaje (str): Lenguaje en el que esta escrito el codigo
        """
       
        resultado = Compilador.Compilar(codigo, lenguaje)
        if resultado.get('status') == 'OK':
            return jsonify({
                'data': resultado.get('data'),
                'message' : 'OK',
                'status' : 200
            })
        else:
            return jsonify({
                'data': resultado.get('data'),
                'message' : 'Error',
                'status' : 500
            })

# def put():
#     pass