class UpdateSQL:
    def __init__(self, nombreTabla: str):
        self.nombreTabla = nombreTabla

    def actualizar(self, idModel, datos: dict):
        """
        Genera una consulta SQL para actualizar un registro en una tabla.
        
        Args:
            idModel (int): Id del registro a actualizar.
            datos (dict): Diccionario con los datos a actualizar en el registro.
        
        Returns:
            str: Consulta SQL para actualizar el registro.
        """
        try:
            if idModel or self.nombreTabla or datos:
                consulta = f"UPDATE {self.nombreTabla}\nSET "
                valores = []
                for columna, valor in datos.items():
                    valores.append(f"{columna} = {"\""+str(valor)+"\"" if isinstance(valor,str) else str(int(valor))}")
                consulta += f"{', '.join(valores)} \nWHERE id = {idModel}"
                print(consulta)
                return consulta
            return None
        except Exception as excep:
            return f"Error encontrado: {excep}"