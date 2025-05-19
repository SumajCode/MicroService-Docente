from .Query import *

class Tabla:
    def __init__(self, nombreTabla: str, columnas: list):
        self.nombreTabla = nombreTabla
        self.columnas = columnas

    def consultaCrearTabla(self):
        """
        Generates a SQL CREATE TABLE statement for the table.

        This method constructs a SQL statement to create a table with the specified
        columns, including any foreign keys and indexes if applicable based on the
        active database configuration.

        Returns:
            str: The SQL CREATE TABLE statement.
        """

        valores = []
        for i in self.columnas:
            valores.append(i.columnaSQL())
        return f"""
CREATE TABLE {self.nombreTabla} (
    {",\n".join(valores)}
    {foreignKey(self.columnas)}
    {index(self.columnas, self.nombreTabla) if BaseConf.SQL_ACTIVE else ""});
{index(self.columnas, self.nombreTabla) if BaseConf.POSTGRES_ACTIVE else ""}"""
    
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