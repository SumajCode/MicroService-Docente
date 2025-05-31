from src.infra.controllers.Controller import Controller
from src.infra.models.MateriaModel import MateriaModel
from src.infra.db.querys.QuerysBuild import consultaParaMateriaDocentes, eliminarMatriculadosPorMateria

class MateriaController(Controller):

    def __init__(self):
        super().__init__()
        modelo = MateriaModel()
        self.nombreTabla = modelo.nombreTabla
        self.columnas = modelo.getNombreColumnas()

    def listar(self):
        """
        Listar todas las materias, excepto los campos create_at y update_at.

        Returns:
            Un objeto JSON con la lista de materias.
        """
        return self.rget({
            'datosObtenidos':None,
            'opciones':{
                'tabla':self.nombreTabla,
                'columnas':self.columnas[1:],
                'columnaOrden':None,
                'asc':None,
                'desc':None,
                'columnaAgrupar':None
            },
            'condiciones':None})

    def listarPorDocente(self, request):
        id = 0
        if request.is_json: 
            datos = request.get_json()
            id = datos.get('id') if datos else 0
        if id == 0:
            if request.form:
                id = request.form.get('id')
            else:
                id = request.args.get('id')
        id = int(id)
        if id > 0:
            print(id)
            return self.getSQL(consultaParaMateriaDocentes(id))

    def crear(self, request):
        """
        Crea un nuevo registro de materia en la base de datos.

        Este método toma los datos de la materia del request, filtra las columnas
        relevantes, y luego los inserta en la tabla correspondiente.

        Args:
            request: El request que contiene los datos de la materia, en formato JSON
                o formulario.

        Returns:
            La respuesta del método post que indica el resultado de la operación de
            inserción.
        """
        datosImportantes = {}
        datos = request.get_json() if request.is_json else request.form
        for i  in self.columnas:
            if i in datos:
                datosImportantes[i] = datos.get(i)
        return self.rpost({'tabla': self.nombreTabla, 'datos': datosImportantes})

    def modificar(self, request):
        datosImportantes = {}
        datos = request.get_json() if request.is_json else request.form
        for i  in self.columnas:
            if i in datos:
                datosImportantes[i] = datos.get(i)
        return self.patch({
            "idEditar":datosImportantes.pop("id"),
            "nombreTabla":self.nombreTabla,
            "datos":datosImportantes})

    def eliminar(self, request):
        id = 0
        if request.is_json: 
            datos = request.get_json()
            id = datos.get('id') if datos else 0
        if id == 0:
            if request.form:
                id = request.form.get('id')
            else:
                id = request.args.get('id')
        id = int(id)
        if id > 0:
            return self.getSQL(eliminarMatriculadosPorMateria(id))
    
    def eliminarTodo(self, request):
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