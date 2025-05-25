from ..scripts.createDB import crearBaseDatos

def crearDB():
    print("Primero se creara la db")
    print(crearBaseDatos())
crearDB()

from .execute import Ejecutar
from ..infra.models.DocenteModel import DocenteModel

ejecutar = Ejecutar()

@ejecutar.crearTabla()
def crearTablaDocente():
    return DocenteModel()

