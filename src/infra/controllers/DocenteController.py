from infra.controllers.Controller import Controller
from infra.models.DocenteModel import DocenteModel

class DocenteController(Controller):

    def __init__(self):
        super().__init__()
        modelo = DocenteModel()
        self.nombreTabla = modelo.nombreTabla
        self.columnas = modelo.getNombreColumnas()

    def listar(self):
        return self.get(opciones={
                'tabla': 'socio',#self.nombreTabla,
                'columnas':['ci_socio', 'nombre_socio', 'apellidos_socio', 'fecha_afiliacion'],
                'columnaOrden':None,
                'asc':None,
                'desc':None,
                'columnaAgrupar':None
            })

    def crear(self, request):
        datosImportantes = {}
        datos = request.get_json() if request.is_json else request.form
        for i  in self.columnas:
            if i in datos:
                print(datos.get(i))
                datosImportantes[i] = datos.get(i)
        return self.post({'tabla': self.nombreTabla, 'datos': datosImportantes})

    def modificar(self, request):
        pass

    def eliminar(self):
        pass