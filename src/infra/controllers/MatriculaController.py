from infra.controllers.Controller import Controller
from scripts.docs.ReadingDocs import ReadingDocs

class MatriculaController(Controller):

    def __init__(self):
        pass

    def listar(self, request):
        try:
            # * Mediante un inner join obtener la lista de matriculados en un curso
            pass
        except Exception as e:
            pass
         
    def crear(self, request):
        try:
            if request is not None:
                archivo = None
                nombreArchivo = ''
                if 'archivo' in request.files:
                    archivoTemporal = request.files['archivo']
                    nombreArchivo = archivoTemporal.filename()
                else:
                    nombreArchivo = request.args.get('path')
            if nombreArchivo.split('.')[-1] == 'xlsx':
                return self.get(datosObtenidos=ReadingDocs.leerXLS(nombreArchivo))
            if nombreArchivo.split('.')[-1] == 'pdf':
                return self.get(datosObtenidos=ReadingDocs.leerPDF(nombreArchivo))
        except Exception as e:
            return 

    # def modificar(self):
    #     pass

    def eliminar(self):
        pass