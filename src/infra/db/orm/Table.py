from infra.db.orm.Column import Columna

class Tabla:
    def __init__(self, nombreTabla: str, columnas: list[Columna]):
        self.nombreTabla = nombreTabla
        self.columnas = columnas
    
    def getNombreColumnas(self):
        """
        Retrieves the list of column names for the table.

        Returns:
            list: A list of strings representing the column names in the table.
        """
        return [columna.nombreColumna for columna in self.columnas]

    def getColumnas(self):
        """
        Retrieves the list of columns for the table.

        Returns:
            list: A list of `Columna` objects representing the columns in the table.
        """
        return self.columnas
    
    def getColumnaPorNombre(self, nombre: str):
        if nombre not in self.getNombreColumnas():
            return "No existe la columna."
        for columna in self.columnas:
            if columna.nombreColumna == nombre:
                return columna
        return None