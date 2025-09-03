from scripts.execute import Ejecutar
from scripts.formater import Formater
from infra.db.sql.DeleteSQL import DeleteSQL

class RespuestaDelete:

    def __init__(self):
        self.ejecutor = Ejecutar()
        self.formater = Formater()
        self.deleteSQL = DeleteSQL()

    def rdelete(self, datos):
        try:
            if datos['idEliminar'] and datos['nombreTabla']:
                return self.formater.json(self.ejecutor.ejecutarConsulta(
                    self.deleteSQL.eliminarDeTabla(
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