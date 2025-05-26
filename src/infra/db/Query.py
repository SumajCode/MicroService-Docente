from infra.db.conn import *
from infra.db.Column import Columna

breakLine = "\n"
scapeValue = "\""

def formatoSQLInsertar(tabla: str, columnas: list, valores: list) -> list:
    """
    Generates a SQL INSERT INTO statement for a specified table with the given column names and values.

    Args:
        tabla (str): The name of the table to insert data into.
        columnas (list): A list of column names.
        valores (list): A list of values to be inserted into the table.

    Returns:
        str: The SQL INSERT INTO statement as a string.
    """
    query = f"INSERT INTO {tabla} (" + ",".join(columnas) + ") VALUES "
    return query + ",".join(["(" + ",".join(value) + ")" for value in valores])

def foreignKey(columnas: list[Columna]):
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
            consulta += f" ON DELETE CASCADE ON UPDATE CASCADE"
            resultado.append(consulta)
    return resultado

def index(columnas: list, nombreTabla: str):
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
                consultaIndex = f"CREATE INDEX"
                consultaIndex += f" index_{nombreTabla}_{column.nombreColumna}"
                consultaIndex += f" ON ({column.nombreColumna})"
                resultado.append(consultaIndex)
    return resultado
    
def insertarEnTabla(nombreTabla: str, datos: dict):
    """
    Generates a SQL INSERT query to insert data into a specified table.

    Args:
        nombreTabla (str): Name of the table to insert data into.
        datos (dict): Dictionary of column names and their respective values to be inserted.

    Returns:
        string: SQL INSERT query as a string.
    """
    try:
        columnas = datos.keys()
        valores = [scapeValue+str(value)+scapeValue if isinstance(value,str) else str(int(value)) for value in datos.values()]
        return formatoSQLInsertar(nombreTabla, columnas, [valores])
    except Exception as excep:
        return f"Error encontrado: {excep}"

def seleccionar(nombreTabla: str, columnas: list = None):
    """
    Generates a SQL SELECT query to retrieve data from a specified table.

    Args:
        nombreTabla (str): Name of the table to select data from.
        columnas (list, optional): List of column names to include in the SELECT query. 
                                   If not provided or None, all columns are selected.

    Returns:
        str: SQL SELECT query string.

    Raises:
        Exception: If an error occurs during query generation, returns an error message.
    """

    try:
        if nombreTabla:
            if columnas is None:
                return f"SELECT * FROM {nombreTabla}"
            return f"SELECT {', '.join(columnas)} FROM {nombreTabla}"
        return ""
    except Exception as excep:
        return f"Error encontrado: {excep}"

def seleccionGroupBy(nombreTabla: str, columnas: list, columnaAgrupar: str):
    """
    Genera una consulta SQL para seleccionar registros en una tabla y agruparlos por una columna en particular.
    
    Args:
        nombreTabla (str): Nombre de la tabla en la que se encuentran los registros.
        columnas (list): Lista de columnas que se desean seleccionar.
        columnaAgrupar (str): Nombre de la columna por la que se agrupar n los registros.
        ascen (bool, optional): Indica si se ordena de forma ascendente. Defaults to False.
        descen (bool, optional): Indica si se ordena de forma descendente. Defaults to False.
    
    Returns:
        str: Consulta SQL para seleccionar y agrupar los registros.
    """
    try:
        if columnaAgrupar is not None:
            return f"{seleccionar(nombreTabla, columnas)}{breakLine}GROUP BY({columnaAgrupar})"
        return seleccionar(nombreTabla, columnas)
    except Exception as excep:
        return f"Error encontrado: {excep}"

def ordenarPor(
        nombreTabla: str,
        columnas: list,
        columnaOrden: str,
        ascen=False,
        descen=False,
        columnaAgrupar: str=None):
    """
    Genera una consulta SQL para ordenar registros en una tabla por una columna en particular.
    
    Args:
        nombreTabla (str): Nombre de la tabla en la que se encuentran los registros.
        columnas (list): Lista de columnas que se desean seleccionar.
        columnaOrden (str): Nombre de la columna por la que se ordenar n los registros.
        ascen (bool, optional): Indica si se ordena de manera ascendente. Defaults to False.
        descen (bool, optional): Indica si se ordena de manera descendente. Defaults to False.
        columnaAgrupar (str, optional): Nombre de la columna por la que se agrupan los registros. Defaults to None.
    
    Returns:
        str: Consulta SQL para ordenar los registros.
    """
    consulta = seleccionar(nombreTabla, columnas)
    try:
        if columnaAgrupar is not None:
            consulta = seleccionGroupBy(nombreTabla, columnas, columnaAgrupar)
        if descen:
            return f"{consulta}{scapeValue}ORDER BY({columnaOrden}) ASC"
        if ascen:
            return f"{consulta}{scapeValue}ORDER BY({columnaOrden}) DESC"
        return consulta
    except Exception as excep:
        return f"Error encontrado: {excep}"

def paginacion(numPag: int):
    pass

def actualizar(idModel, nombreTabla: str, datos: dict):
    """
    Genera una consulta SQL para actualizar un registro en una tabla.
    
    Args:
        idModel (int): Id del registro a actualizar.
        nombreTabla (str): Nombre de la tabla en la que se encuentra el registro.
        datos (dict): Diccionario con los datos a actualizar en el registro.
    
    Returns:
        str: Consulta SQL para actualizar el registro.
    """
    try:
        if idModel is not None or nombreTabla is not None or datos is not None:
            consulta = f"UPDATE {nombreTabla}{scapeValue}"
            for columna, valor in datos.items():
                consulta += f"SET {columna} = {breakLine+str(valor)+breakLine if isinstance(valor,str) else str(int(valor))},{scapeValue}"
                consulta += f" WHERE id = {idModel}"
            return consulta
    except Exception as excep:
        return f"Error encontrado: {excep}"
    pass

def eliminar(id):
    
    pass

