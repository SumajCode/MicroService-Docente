from ..infra.db.Query import CrearDB

def crearDB():
    print("Primero se creara la db")
crearDB()

from .execute import Ejecutar
from ..infra.models.DocenteModel import DocenteModel

ejecutar = Ejecutar()

@ejecutar.crearTabla()
def crearTablaDocente():
    return DocenteModel().consultaCrearTabla()