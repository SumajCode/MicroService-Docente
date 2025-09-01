from features.controllers.Controller import Controller
from infra.models.EvaluacionModel import EvaluacionModel

class EvaluacionController(Controller):

    def __init__(self):
        super().__init__()
        modelo = EvaluacionModel()
        self.nombreTabla = modelo.nombreTabla
        self.columnas = modelo.getNombreColumnas()

    def listar(self):
        return None

    def crear(self):
        datosImportantes = {}
        # datos = request.get_json() if request.is_json else request.form
        # for i  in self.columnas:
        #     if i in datos:
        #         datosImportantes[i] = datos.get(i)
        return self.post({'tabla': self.nombreTabla, 'datos': datosImportantes})

    def modificar(self):
        pass

    def eliminar(self):
        pass