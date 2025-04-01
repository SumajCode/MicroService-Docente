class Column:
    def __init__(self, name: str, type: str, primary_key = False, auto_increment= False, foreign_key = False, column_foreing = "", id_reference = ""):
        self.name = name
        self.type = type
        self.primary_key = primary_key
        self.auto_increment = auto_increment
        self.foreign_key = foreign_key
        self.column_foreing = column_foreing
        self.id_reference = id_reference
    
    
    def column_sql(self):
        if self.primary_key and self.foreign_key:
            return f"{self.name} {self.type} PRIMARY KEY, {f"FOREIGN KEY {self.name} REFERENCES {self.column_foreing}({self.id_reference})" if self.primary_key else ""}"
        if self.foreign_key:
            return f"{self.name} {self.type}, {f"FOREIGN KEY {self.name} REFERENCES {self.column_foreing}({self.id_reference})" if self.primary_key else ""}"
        return f"{self.name} {self.type}{" PRIMARY KEY" if self.primary_key else ""}{" AUTO_INCREMENT" if self.auto_increment else ""}"
    