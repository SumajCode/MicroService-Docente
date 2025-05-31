from src.domain.GetResponse import RespuestaGet
from src.domain.PostResponse import RespuestaPost
from src.domain.DeleteResponse import RespuestaDelete
from src.domain.SQLResponse import RespuestaSQL
from src.domain.PatchResponse import RespuestaPatch

class Controller(RespuestaGet, RespuestaPost, RespuestaDelete, RespuestaSQL, RespuestaPatch):

    def __init__(self):
        super().__init__()

    def get(self, datos):
        return self.rget(datos)

    def post(self, datos):
        return self.rpost(datos)

    def getSQL(self, query):
        return self.rgetSQL(query)

    def patch(self, datos):
        return self.rpatch(datos)

    def put(self):
        pass

    def delete(self, datos):
        return self.rdelete(datos)
    
    def deleteAndGet(self, querys):
        return self.deleteAndGetSQL(querys)