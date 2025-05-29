from infra.controllers.Controller import Controller
from scripts.docs.ReadingDocs import ReadingDocs
from infra.models.MatriculaModel import MatriculaModel

class MatriculaController(Controller):

    def __init__(self):
        super().__init__()
        modelo = MatriculaModel()
        self.nombreTabla = modelo.nombreTabla
        self.columnas = modelo.getNombreColumnas()

    def listar(self, request):
        try:
            # * Mediante un inner join obtener la lista de matriculados en un curso
            return request
        except Exception as excep:
            return excep

    def crear(self, request):
        try:
            nombreArchivo = ''
            if request is not None:
                archivo = None
                if 'archivo' in request.files:
                    archivoTemporal = request.files['archivo']
                    nombreArchivo = archivoTemporal.filename(archivo)
                else:
                    nombreArchivo = request.args.get('path')
            if len(nombreArchivo) > 5:
                readingDocs = ReadingDocs()
                if nombreArchivo.split('.')[-1] == 'xlsx':
                    return self.get(datosObtenidos=readingDocs.leerXLS(nombreArchivo))
                if nombreArchivo.split('.')[-1] == 'pdf':
                    return self.get(datosObtenidos=readingDocs.leerPDF(nombreArchivo))
            return "Error"
        except Exception as excep:
            return excep

    # def modificar(self):
    #     pass

    def eliminar(self):
        pass