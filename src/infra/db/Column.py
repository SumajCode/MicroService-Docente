class Columna:
    def __init__(self, nombreColumna: str, tipoColumna: str, llavePrimaria = False, autoIncremental= False, llaveForanea = False, columnaTablaRelacion = "", referenciaTabla = "", indexado=False):
        self.nombreColumna = nombreColumna
        self.tipoColumna = tipoColumna
        self.llavePrimaria = llavePrimaria
        self.autoIncremental = autoIncremental
        self.llaveForanea = llaveForanea
        self.columnaTablaRelacion = columnaTablaRelacion
        self.referenciaTabla = referenciaTabla
        self.indexado = indexado
    
    def columnaSQL(self):
        return f"{self.nombreColumna} {self.tipoColumna}{" AUTO_INCREMENT" if self.autoIncremental else ""}{" PRIMARY KEY" if self.llavePrimaria else ""}"
    
    def getNombreColumna(self):
        return self.nombreColumna
    
    def getLlaveForanea(self):
        return self.llaveForanea
    
    def getColumnaTablaRelacion(self):
        return self.columnaTablaRelacion
    
    def getReferenciaTabla(self):
        return self.referenciaTabla
    
    def getIndexado(self):
        return self.indexado