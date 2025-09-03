class InsertSQL:
    def __init__(self, tabla: str):
        self.tabla = tabla

    def formatoSQLInsertar(self, columnas: list, valores: list) -> list:
        """
        Generates a SQL INSERT INTO statement for a specified table with the given column names and values.

        Args:
            columnas (list): A list of column names.
            valores (list): A list of values to be inserted into the table.

        Returns:
            str: The SQL INSERT INTO statement as a string.
        """
        query = f"INSERT INTO {self.tabla} (" + ",".join(columnas) + ") VALUES "
        return query + ",".join(["(" + ",".join(value) + ")" for value in valores])

    def insertarEnTabla(self, datos: dict):
        """
        Generates a SQL INSERT query to insert data into a specified table.

        Args:
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
            return self.formatoSQLInsertar(columnas, [valores])
        except Exception as excep:
            return f"Error encontrado: {excep}"

    def insertarTodoEnTabla(self, datos: dict):
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
            return self.formatoSQLInsertar(columnas, valores)
        except Exception as excep:
            return f"Error encontrado: {excep}"
