from infra.db.Query import *

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
        breakLine = ",\n"
        parametrosTabla = []
        for i in self.columnas:
            parametrosTabla.append(i.columnaSQL())
        llavesForaneas = foreignKey(self.columnas)
        indexs = index(self.columnas, self.nombreTabla)
        postgreIndexs = ""
        if len(llavesForaneas) > 0:
            parametrosTabla.extend(llavesForaneas)
        if len(indexs) > 0:
            if BaseConf.POSTGRES_ACTIVE is False:
                parametrosTabla.extend(indexs)
            else:
                breakLine.join(indexs)
        
        return f"""
CREATE TABLE {self.nombreTabla} (
{breakLine.join(parametrosTabla)}
);
{postgreIndexs}"""
    
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