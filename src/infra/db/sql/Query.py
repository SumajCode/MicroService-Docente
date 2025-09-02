from infra.db.orm.conn import BaseConf
from infra.db.orm.Column import Columna

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
            consulta += " ON DELETE CASCADE ON UPDATE CASCADE"
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
                consultaIndex = "CREATE INDEX"
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
        valores = []
        for value in datos.values():
            if isinstance(value,str) and not value.isdigit():
                valores.append("\""+str(value)+"\"")
            else:
                valores.append(str(int(value)))
        return formatoSQLInsertar(nombreTabla, columnas, [valores])
    except Exception as excep:
        return f"Error encontrado: {excep}"

def insertarTodoEnTabla(nombreTabla: str, datos: dict):
    try:
        columnas = datos['columns']
        valores = []
        for item in datos['data']:
            preList = []
            for value in item.values():
                if isinstance(value,str) and not value.isdigit():
                    preList.append("\""+str(value)+"\"")
                else:
                    preList.append(str(int(value)))
            valores.append(preList)
        return formatoSQLInsertar(nombreTabla, columnas, valores)
    except Exception as excep:
        return f"Error encontrado: {excep}"
