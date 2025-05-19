from .Controller import Controller
from ..models.DocenteModel import DocenteModel

class DocenteController(Controller):

    def __init__(self):
        modelo = DocenteModel()
        self.nombreTabla = modelo.nombreTabla
        self.columnas = modelo.getNombreColumnas()
        pass

    def listar(self):
        self.get()

    def crear(self, request):
        datosImportantes = {}
        datosDocente = self.columnas
        for i  in datosDocente:
            datosImportantes[i] = request.form.get[i]
        return self.post({'tabla': self.nombreTabla, 'datos': datosImportantes})

    def modificar(self, request):

        pass

    def eliminar(self):
        pass