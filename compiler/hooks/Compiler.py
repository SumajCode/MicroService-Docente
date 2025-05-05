import traceback
import sys

class Compilador:
    def __init__(self):
        pass

    def Compilar(self, codigo: str, lenguaje: str):
        """
        Compila el codigo fuente en base al lenguaje especificado y devuelve
        el resultado de la compilacion.

        Parameters:
        codigo (str): Codigo fuente a compilar
        lenguaje (str): Lenguaje en el que esta escrito el codigo

        Returns:
        dict: Diccionario con dos claves: 'status' y 'data'. La clave 'status'
        puede tener dos valores: 'OK' o 'Error'. La clave 'data' contendra el
        resultado de la compilacion en caso de exito o el mensaje de error en
        caso de fallo.
        """
        resultado = {'status': None, 'data': None}
        if lenguaje == "python":
            try:
                resultado['status'] = 'OK'
                resultado['data'] = exec(compile(codigo, '<String>', 'exec'))
                return resultado
            except Exception:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                resultado['status'] = 'Error'
                resultado['data'] = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
                return resultado
        # else:
        #     pass

    def CompilarConArgumentos(self, codigo: str, lenguaje: str, argumentos: list):
        pass

    def CompilarConArgumentosYEntrada(self, codigo: str, lenguaje: str, argumentos: list, entrada: list):
        pass