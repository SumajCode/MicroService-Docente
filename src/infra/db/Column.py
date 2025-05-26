class Columna:
    def __init__(
            self,
            nombreColumna: str,
            tipoColumna: str,
            llavePrimaria = False,
            autoIncremental= False,
            llaveForanea = False,
            referenciaTabla = "",
            indexado=False):
        self.nombreColumna = nombreColumna
        self.tipoColumna = tipoColumna
        self.llavePrimaria = llavePrimaria
        self.autoIncremental = autoIncremental
        self.llaveForanea = llaveForanea
        self.referenciaTabla = referenciaTabla
        self.indexado = indexado

    def columnaSQL(self):
        """
        Generates a SQL string representing the column definition.

        Returns:
            str: SQL string representing the column definition.
        """
        consulta = f"{self.nombreColumna} {self.tipoColumna}"
        consulta += " AUTO_INCREMENT" if self.autoIncremental else ""
        consulta += " PRIMARY KEY" if self.llavePrimaria else ""
        return consulta

    def getNombreColumna(self):
        """
        Retrieves the name of the column.

        Returns:
            str: The name of the column.
        """
        return self.nombreColumna

    def getLlaveForanea(self):
        """
        Retrieves whether the column is a foreign key or not.

        Returns:
            bool: Whether the column is a foreign key or not.
        """
        return self.llaveForanea

    def getReferenciaTabla(self):
        """
        Retrieves the name of the table referenced by the foreign key, if applicable.

        Returns:
            str: The name of the table referenced by the foreign key, if applicable.
        """
        return self.referenciaTabla

    def getIndexado(self):
        """
        Retrieves whether the column is indexed or not.

        Returns:
            bool: Whether the column is indexed or not.
        """
        return self.indexado