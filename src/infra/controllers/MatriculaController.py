import requests
import os
from werkzeug.utils import secure_filename
from infra.controllers.Controller import Controller
from scripts.docs.ReadingDocs import ReadingDocs
from infra.models.MatriculaModel import MatriculaModel
from config.conf import BaseConf

class MatriculaController(Controller):

    def __init__(self):
        super().__init__()
        modelo = MatriculaModel()
        self.readingDocs = ReadingDocs()
        self.nombreTabla = modelo.nombreTabla
        self.columnas = modelo.getNombreColumnas()
        self.urlEstudiantes = BaseConf.URL_NEIGHBORG

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
        estudiantesDatos = requests.get(self.urlEstudiantes+"/estudiantes/")
        estudiantesDatos = estudiantesDatos.json().get('data')
        requestLocal = request.get_json() if request.is_json else None
        idMateria = ''
        datosTemporales = None
        if requestLocal is not None:
            idMateria = requestLocal.get('id_materia')
        else:
            idMateria = request.args.get('id_materia')
        if idMateria != '':
            datosTemporales = self.rget({
                'datosObtenidos':None,
                'opciones':{
                    'tabla': self.nombreTabla,
                    'columnas':self.columnas[1:],
                    'columnaOrden':None,
                    'asc':None,
                    'desc':None,
                    'columnaAgrupar':None
                },
                'condiciones':None})
            datosTemporales = datosTemporales.get_json()['data']
        if len(datosTemporales) > 0:
            datosFiltro = [item['id_estudiante'] for item in datosTemporales]
            datosFiltrados = [item for item in estudiantesDatos if item['id_estudiante'] in datosFiltro]
            return self.rget({
            "datosObtenidos": datosFiltrados,
            "opciones": None,
            "condiciones": None})
        return self.rget({
            "datosObtenidos": estudiantesDatos,
            "opciones": None,
            "condiciones": None})

    def crearMatriculados(self, request):
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
            materia = ''
            if request is not None:
                if 'archivo' in request.files:
                    archivoTemporal = request.files.get('archivo')

                    rutaTemporal = os.path.dirname(os.path.abspath(__file__))
                    rutaCompartida = os.path.abspath(os.path.join(rutaTemporal, "../../shared"))

                    ruta = os.path.join(rutaCompartida, secure_filename(archivoTemporal.filename))
                    archivoTemporal.save(ruta)
                    nombreArchivo = ruta
                    materia = request.form.get('id_materia')
                else:
                    nombreArchivo = request.args.get('path')
                    materia = request.args.get('id_materia')
            if len(nombreArchivo) > 5:
                predata = None
                if nombreArchivo.split('.')[-1] == 'xlsx':
                    predata = self.rget({
                        'datosObtenidos': self.readingDocs.leerXLS(nombreArchivo),
                        'opciones': None,
                        'condiciones': None}).get_json()
                    predata['data'] = {
                        'datos_matriculados': predata['data'],
                        'materia': materia}
                if nombreArchivo.split('.')[-1] == 'pdf':
                    predata = self.rget({
                        'datosObtenidos': self.readingDocs.leerPDF(nombreArchivo),
                        'opciones': None,
                        'condiciones': None}).get_json()
                    predata['data'] = {
                        'datos_matriculados': predata['data'],
                        'materia': materia}
                os.remove(nombreArchivo)
                return predata
            return "Error"    
        except Exception as excep:
            return excep

    def crear(self, request):
        datosImportantes = {}
        datos = request.get_json() if request.is_json else request.form
        for i  in self.columnas:
            if i in datos:
                datosImportantes[i] = datos.get(i)
        return self.rpost({'tabla': self.nombreTabla, 'datos': datosImportantes})

    def eliminar(self, request):
        """
        Elimina todos los docentes.

        Returns:
            Un objeto JSON vac o con un mensaje de error.
        """
        id = 0
        if request.is_json: 
            datos = request.get_json()
            id = datos.get('id') if datos else 0
        if id == 0:
            if request.form:
                id = request.form.get('id')
            else:
                id = request.args.get('id')
        if id > 0:
            return self.rdelete({
                'nombreTabla': self.nombreTabla,
                'idEliminar': id
            })