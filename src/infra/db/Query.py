from ..conn import *
from ..formater import Formater

def foreignKey(columnas: list):
    resultado = []
    for column in columnas:
        if column.llaveForanea:
            resultado.append(f"FOREIGN KEY ({column.columnaTablaRelacion}) REFERECES {column.referenciaTabla}(id)")
    return ",\n".join(resultado)

def index(columnas: list, nombreTabla: str):
    resultado = []
    for column in columnas:
        if column.indexado:
            if BaseConf.SQL_ACTIVE:
                resultado.append(f"INDEX ({column.nombreColumna})")
            if BaseConf.POSTGRES_ACTIVE:
                resultado.append(f"CREATE INDEX index_{nombreTabla}_{column.nombreColumna} ON ({column.nombreColumna})")
    if BaseConf.SQL_ACTIVE:
        return ",\n".join(resultado)
    if BaseConf.POSTGRES_ACTIVE:
        return ";\n".join(resultado)

def insertarEnTabla(nombreTabla: str, datos: dict):
    try:
        columnas = datos.keys()
        valores = ["\""+str(value)+"\"" if isinstance(value,str) else str(int(value)) for value in datos.values()]
        return Formater().formatoSQLInsertar(nombreTabla, columnas, [valores])
    except Exception as e:
        return f"Error encontrado: {e}"

def seleccionar(nombreTabla: str, columnas: list = None):
    try:
        if nombreTabla:
            if columnas is None:
                return f"SELECT * FROM {nombreTabla}"
            return f"SELECT {', '.join(columnas)} FROM {nombreTabla}"
        return ""
    except Exception as e:
        return f"Error encontrado: {e}"

def seleccionGroupBy(nombreTabla: str, columnas: list, columnaAgrupar: str, ascen=False, descen=False):
    try:
        if columnaAgrupar != None:
            return f"{seleccionar(nombreTabla, columnas)}\nGROUP BY({columnaAgrupar})"
        return seleccionar(nombreTabla, columnas)
    except Exception as e:
        return f"Error encontrado: {e}"

def ordenarPor(nombreTabla: str, columnas: list, columnaOrden: str, ascen=False, descen=False, columnaAgrupar: str=None):
    consulta = seleccionar(nombreTabla, columnas)
    try:
        if columnaAgrupar != None:
            consulta += f"\nGROUP BY({columnaAgrupar})"
        if descen:
            return f"{consulta}\nORDER BY({columnaOrden}) ASC"
        if ascen:
            return f"{consulta}\nORDER BY({columnaOrden}) DESC"
        return consulta
    except Exception as e:
        return f"Error encontrado: {e}"

def paginacion(numPag: int):
    pass

def actualizar(id, nombreTabla: str, datos: dict):
    try:
        if id != None or nombreTabla != None or datos != None:
            consulta = f"UPDATE {nombreTabla}\n"
            for columna, valor in datos.items():
                consulta += f"SET {columna} = {"\""+str(valor)+"\"" if isinstance(valor,str) else str(int(valor))},\n"
            return consulta
    except Exception as e:
        return f"Error encontrado: {e}"
    pass

def eliminar(id):
    
    pass

