from infra.db.orm.conn import BaseConf
from infra.db.orm.Column import Columna
from infra.db.orm.Table import Tabla

class Query:
    def __init__(self):
        pass

    def foreignKey(self, columnas: list[Columna]):
        """
        Generates a SQL FOREIGN KEY string for a list of columns.

        Args:
            columnas (list): A list of Columna objects.

        Returns:
            str: The FOREIGN KEY string.
        """
        resultado = []
        for column in columnas:
            if column.llaveForanea:
                consulta = f"CONSTRAINT fk_{column.nombreColumna}"
                consulta += f" FOREIGN KEY ({column.nombreColumna})"
                consulta += f" REFERENCES {column.referenciaTabla}(id)"
                consulta += " ON DELETE CASCADE ON UPDATE CASCADE"
                resultado.append(consulta)
        return resultado

    def index(self, columnas: list, nombreTabla: str):
        """
        Create the index string for a list of columns.

        Args:
            columnas (list): A list of Columna objects.
            nombreTabla (str): The name of the table.

        Returns:
            str: The index string.
        """
        resultado = []
        for column in columnas:
            if column.indexado:
                if BaseConf.SQL_ACTIVE:
                    consultaIndex = f"INDEX index_{nombreTabla}_{column.nombreColumna}"
                    consultaIndex += f" ({column.nombreColumna})"
                    resultado.append(consultaIndex)
                if BaseConf.POSTGRES_ACTIVE:
                    consultaIndex = "CREATE INDEX"
                    consultaIndex += f" index_{nombreTabla}_{column.nombreColumna}"
                    consultaIndex += f" ON ({column.nombreColumna})"
                    resultado.append(consultaIndex)
        return resultado

    def consultaCrearTabla(self, tabla: Tabla):
        """
        Generates a SQL CREATE TABLE statement for the table.

        This method constructs a SQL statement to create a table with the specified
        columns, including any foreign keys and indexes if applicable based on the
        active database configuration.

        Returns:
            str: The SQL CREATE TABLE statement.
        """

        parametrosTabla = []
        for i in tabla.columnas:
            parametrosTabla.append(i.columnaSQL())
        llavesForaneas = self.foreignKey(tabla.columnas)
        indexs = self.index(tabla.columnas, tabla.nombreTabla)
        postgreIndexs = ""
        if len(llavesForaneas) > 0:
            parametrosTabla.extend(llavesForaneas)
        if len(indexs) > 0:
            if BaseConf.POSTGRES_ACTIVE is False:
                parametrosTabla.extend(indexs)
            else:
                ";\n".join(indexs)
        return f"""
    CREATE TABLE {tabla.nombreTabla} (
    {",\n".join(parametrosTabla)}
    );
    {postgreIndexs}"""

    def agregarColumnaTabla(self, modelo: Tabla, ejecutarConsulta):
        nombreTabla = modelo.nombreTabla
        columnasActuales = modelo.getNombreColumnas()
        columnasDB = []
        consulta = ejecutarConsulta(f"DESCRIBE {nombreTabla};")
        for columna in consulta:
            columnasDB.append(columna['Field'])
        columnasAdicion=[]
        for nombre in columnasDB:
            if nombre in columnasActuales:
                columnasActuales.remove(nombre)
        if len(columnasActuales) > 0:
            columnasActuales = [f"ADD COLUMN {modelo.getColumnaPorNombre(columna).columnaSQL()}" for columna in columnasActuales]
            columnasAdicion.extend(columnasActuales)
            consulta = f"ALTER TABLE {nombreTabla} \n"
            consulta += " NULL,\n".join(columnasAdicion)
            ejecutarConsulta(consulta)
            return "Columnas nuevas agregadas."
        return "No tiene columnas nuevas."