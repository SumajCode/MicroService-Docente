from scripts.execute import Ejecutar
from scripts.formater import Formater
from infra.db.Query import eliminarDeTabla

class RespuestaDelete:

    def __init__(self):
        self.ejecutor = Ejecutar()
        self.formater = Formater()

    def rdelete(self, datos):
        try:
            if datos['idEliminar'] and datos['nombreTabla']:
                return self.formater.json(self.ejecutor.ejecutarConsulta(
                    eliminarDeTabla(
                        datos['nombreTabla'], 
                        datos['idEliminar'])
                    )
                )
            return None
        except Exception as excep:
            return self.formater.json({
                'message' : str(excep),
                'status' : 500
            })