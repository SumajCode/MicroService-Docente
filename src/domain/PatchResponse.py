from infra.db.Query import actualizar

from scripts.execute import Ejecutar
from scripts.formater import Formater

class RespuestaPatch:

    def __init__(self):
        self.ejecutor = Ejecutar()
        self.formater = Formater()

    def rpatch(self, datos):
        """
        Recibe un diccionario con claves 'idEditar', 'nombreTabla' y 'datos'. 
        Llama a la funcion 'actualizar' de la clase 'Query' y ejecuta la consulta 
        con los datos suministrados. Devuelve un objeto JSON con la respuesta 
        de la consulta.
        
        datos (dict): Diccionario con claves 'idEditar', 'nombreTabla' y 'datos'.

        Returns:
            dict: Diccionario con la respuesta de la consulta.
        """
        try:
            if datos['idEditar'] is not None and datos['nombreTabla'] is not None and datos['datos'] is not None:
                return self.formater.json(self.ejecutor.ejecutarConsulta(
                    actualizar(
                        datos['idEditar'], 
                        datos['nombreTabla'], 
                        datos['datos']))
                )
            return None
        except Exception as excep:
            return self.formater.json({
                'message' : str(excep),
                'status' : 500
            })