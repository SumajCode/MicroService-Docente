class DataType:

    def String(length=1):
        if length > 1:
            return f" VARCHAR({str(length)})"
        else:
            return " TEXT"

    def Json():
        return " JSON"
    
    def TinyText():
        return " TINYTEXT"
    
    def Enum(list_values: list):
        if len(list_values) > 2:
            values = []
            for i in list_values:
                values.append(f"'{i}'" if i.isdigit() == False else i)
            return f" ENUM({','.join(values)})"
        
    def Set(list_values: list):
        if len(list_values) > 2:
            values = []
            for i in list_values:
                values.append(f"'{i}'" if i.isdigit() == False else i)
            return f" SET({','.join(values)})"
    def Integer():
        return " BIGINT"
