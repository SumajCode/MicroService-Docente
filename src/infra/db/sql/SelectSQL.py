class SelectSQL:
    def __init__(self, nombreTabla: str):
        self.nombreTabla = nombreTabla
    
    def seleccionar(self, columnas: list = None):
        """
        Generates a SQL SELECT query to retrieve data from a specified table.

        Args:
            columnas (list, optional): List of column names to include in the SELECT query. 
                                    If not provided or None, all columns are selected.

        Returns:
            str: SQL SELECT query string.

        Raises:
            Exception: If an error occurs during query generation, returns an error message.
        """

        try:
            if self.nombreTabla:
                if columnas is None:
                    return f"SELECT * FROM {self.nombreTabla}"
                return f"SELECT {', '.join(columnas)} FROM {self.nombreTabla}"
            return ""
        except Exception as excep:
            return f"Error encontrado: {excep}"
        
    def seleccionarCon(self, columnas: list, condiciones: dict):
        try:
            if self.nombreTabla is not None:
                if condiciones is None:
                    return self.seleccionar(columnas)
                return None
            return None
        except Exception as e:
            return f"Ocurrio un error{e}"

    def seleccionGroupBy(self, columnas: list, columnaAgrupar: str):
        """
        Genera una consulta SQL para seleccionar registros en una tabla y agruparlos por una columna en particular.
        
        Args:
            columnas (list): Lista de columnas que se desean seleccionar.
            columnaAgrupar (str): Nombre de la columna por la que se agrupar n los registros.
        Returns:
            str: Consulta SQL para seleccionar y agrupar los registros.
        """
        try:
            if columnaAgrupar is not None:
                return f"{self.seleccionar(columnas)}\nGROUP BY({columnaAgrupar})"
            return self.seleccionar(columnas)
        except Exception as excep:
            return f"Error encontrado: {excep}"

    def ordenarPor(
            self,
            columnas: list,
            columnaOrden: str,
            ascen=False,
            descen=False,
            columnaAgrupar: str=None):
        """
        Genera una consulta SQL para ordenar registros en una tabla por una columna en particular.
        
        Args:
            columnas (list): Lista de columnas que se desean seleccionar.
            columnaOrden (str): Nombre de la columna por la que se ordenar n los registros.
            ascen (bool, optional): Indica si se ordena de manera ascendente. Defaults to False.
            descen (bool, optional): Indica si se ordena de manera descendente. Defaults to False.
            columnaAgrupar (str, optional): Nombre de la columna por la que se agrupan los registros. Defaults to None.
        
        Returns:
            str: Consulta SQL para ordenar los registros.
        """
        consulta = self.seleccionar(columnas)
        try:
            if columnaAgrupar is not None:
                consulta = self.seleccionGroupBy(columnas, columnaAgrupar)
            if descen:
                return f"{consulta}\nORDER BY({columnaOrden}) ASC"
            if ascen:
                return f"{consulta}\nORDER BY({columnaOrden}) DESC"
            return consulta
        except Exception as excep:
            return f"Error encontrado: {excep}"
        
    def paginacion(self, numPag: int=0):
        return numPag