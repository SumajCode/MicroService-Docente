from infra.controllers.Controller import Controller
from infra.models.DocenteModel import DocenteModel
from infra.db.querys.QuerysBuild import eliminarDocenteYMateria, consultaParaDocenteMaterias, consultaPorId

class DocenteController(Controller):

    def __init__(self):
        super().__init__()
        modelo = DocenteModel()
        self.nombreTabla = modelo.nombreTabla
        self.columnas = modelo.getNombreColumnas()

    def listar(self):
        """
        Listar todos los docentes, excepto los campos create_at y update_at.

        Returns:
            Un objeto JSON con la lista de docentes.
        """
        return self.rget({
            'datosObtenidos':None,
            'opciones':{
                'tabla': self.nombreTabla,
                'columnas':self.columnas[1:-2],
                'columnaOrden':None,
                'asc':None,
                'desc':None,
                'columnaAgrupar':None
            },
            'condiciones':None})

    def listarId(self, request):
        """
        Listar un docente específico, excepto los campos create_at y update_at.

        Args:
            request: El request que contiene el identificador del docente.

        Returns:
            Un objeto JSON con el docente especificado.
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
        id = int(id)
        if id > 0:
            print(id)
            return self.getSQL(consultaPorId(id, self.columnas[1:-2], self.nombreTabla))

    def listarMaterias(self, request):
        """
        Lista todas las materias asociadas a un docente específico.

        Args:
            request: Objeto de solicitud que contiene el identificador del docente.

        Returns:
            Un objeto JSON con la lista de materias asociadas al docente especificado.
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
        id = int(id)
        if id > 0:
            return self.getSQL(consultaParaDocenteMaterias(id))

    def crear(self, request):
        """
        Crea un nuevo registro de docente en la base de datos.

        Este método toma los datos del docente del request, filtra las columnas
        relevantes, y luego los inserta en la tabla correspondiente.

        Args:
            request: El request que contiene los datos del docente, en formato JSON
            o formulario.

        Returns:
            La respuesta del método post que indica el resultado de la operación de
            inserción.
        """

        datosImportantes = {}
        datos = request.get_json() if request.is_json else request.form
        for i  in self.columnas:
            if i in datos:
                print(datos.get(i))
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
        """
        Elimina un docente.

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
        id = int(id)
        if id > 0:
            return self.getSQL(eliminarDocenteYMateria(id))

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