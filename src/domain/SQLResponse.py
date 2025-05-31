from src.scripts.execute import Ejecutar
from src.scripts.formater import Formater

class RespuestaSQL:

    def __init__(self):
        self.ejecutor = Ejecutar()
        self.formater = Formater()
    
    def rgetSQL(self, query):
        return self.formater.json(self.ejecutor.ejecutarConsulta(query))
    
    def deleteAndGetSQL(self, querys):
        respuesta = self.ejecutor.ejecutarConsulta(querys[0])
        self.ejecutor.ejecutarConsulta(querys[1])
        return self.formater.json(respuesta)