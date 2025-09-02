class DeleteSQL:
    def __init__(self, nombreTabla: str):
        self.nombreTabla = nombreTabla
    
    def eliminarDeTabla(self, idEliminar: int = 0):
        """
        Genera una consulta SQL para eliminar un registro en una tabla.
        
        Args:
            idEliminar (int): Id del registro a eliminar.
        
        Returns:
            str: Consulta SQL para eliminar el registro.
        """
        try:
            if idEliminar or self.nombreTabla:
                return f"DELETE FROM {self.nombreTabla}\nWHERE id = {idEliminar}"
            return None
        except Exception as excep:
            return f"Error encontrado: {excep}"