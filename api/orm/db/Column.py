class Columna:
    def __init__(self, nombreColumna: str, tipoColumna: str, llavePrimaria = False, autoIncremental= False, llaveForanea = False, columnaTablaRelacion = "", referennciaTablaID = ""):
        self.nombreColumna = nombreColumna
        self.tipoColumna = tipoColumna
        self.llavePrimaria = llavePrimaria
        self.autoIncremental = autoIncremental
        self.llaveForanea = llaveForanea
        self.columnaTablaRelacion = columnaTablaRelacion
        self.referennciaTablaID = referennciaTablaID
    
    
    def columnaSQL(self):
        if self.llavePrimaria and self.llaveForanea:
            return f"{self.nombreColumna} {self.tipoColumna} PRIMARY KEY, {f"FOREIGN KEY {self.nombreColumna} REFERENCES {self.columnaTablaRelacion}({self.referennciaTablaID})" if self.llavePrimaria else ""}"
        if self.llaveForanea:
            return f"{self.nombreColumna} {self.tipoColumna}, {f"FOREIGN KEY {self.nombreColumna} REFERENCES {self.columnaTablaRelacion}({self.referennciaTablaID})" if self.llavePrimaria else ""}"
        return f"{self.nombreColumna} {self.tipoColumna}{" PRIMARY KEY" if self.llavePrimaria else ""}{" AUTO_INCREMENT" if self.autoIncremental else ""}"
    