from src.infra.controllers.Controller import Controller
from src.scripts.docs.ReadingDocs import ReadingDocs
from src.infra.models.MatriculaModel import MatriculaModel

class MatriculaController(Controller):

    def __init__(self):
        super().__init__()
        modelo = MatriculaModel()
        self.readingDocs = ReadingDocs()
        self.nombreTabla = modelo.nombreTabla
        self.columnas = modelo.getNombreColumnas()

    def listar(self, request):
        """
        Listar todas las matrículas, con detalles específicos.

        Args:
            request: El request que podría contener filtros o configuraciones
            adicionales para personalizar la lista de matrículas.

        Returns:
            Un objeto JSON con la lista de matrículas basadas en los criterios
            proporcionados en el request.
        """

        return self.rget()

    def getMatriculados(self, request):
        """
        Devuelve una lista de matriculados seg n el archivo cargado.

        Args:
            request (flask.Request): El request que contiene el archivo
                a procesar.

        Returns:
            dict: Contiene la lista de matriculados en la clave
                'datosObtenidos', y opciones y condiciones vac as en las
                claves 'opciones' y 'condiciones' respectivamente.
        """
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
                if nombreArchivo.split('.')[-1] == 'xlsx':
                    return self.rget({
                        'datosObtenidos':self.readingDocs.leerXLS(nombreArchivo),
                        'opciones':None,
                        'condiciones':None})
                if nombreArchivo.split('.')[-1] == 'pdf':
                    return self.rget({
                        'datosObtenidos':self.readingDocs.leerPDF(nombreArchivo),
                        'opciones':None,
                        'condiciones':None})
            return "Error"
        except Exception as excep:
            return excep

    def crear(self, request):
        pass

    # def modificar(self):
    #     pass

    def eliminar(self):
        pass