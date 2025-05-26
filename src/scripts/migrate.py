from scripts.createDB import crearBaseDatos

def crearDB():
    """
    Crea la base de datos utilizando la configuración especificada.

    Esta función imprime un mensaje indicando el inicio del proceso de creación
    de la base de datos, llama a `crearBaseDatos()` para llevar a cabo la 
    creación, y luego imprime el resultado de la operación.

    Returns:
        str: Un mensaje indicando el éxito o el error en la creación de la base 
        de datos.
    """

    print("Primero se creara la db")
    print(crearBaseDatos())
crearDB()

from scripts.execute import Ejecutar
from infra.models.DocenteModel import DocenteModel
from infra.models.MateriaModel import MateriaModel
from infra.models.MatriculaModel import MatriculaModel
from infra.models.EvaluacionModel import EvaluacionModel

ejecutar = Ejecutar()

@ejecutar.crearTabla()
def crearTablaDocente():
    """
    Crea la tabla docente en la base de datos.

    Returns:
        DocenteModel: Un objeto que representa la tabla docente.
    """
    return DocenteModel()


@ejecutar.crearTabla()
def crearTablaMateria():
    """
    Crea la tabla docente en la base de datos.

    Returns:
        DocenteModel: Un objeto que representa la tabla docente.
    """
    return MateriaModel()

@ejecutar.crearTabla()
def crearTablaMatricula():
    """
    Crea la tabla docente en la base de datos.

    Returns:
        DocenteModel: Un objeto que representa la tabla docente.
    """
    return MatriculaModel()

@ejecutar.crearTabla()
def crearTablaEvaluacion():
    """
    Crea la tabla docente en la base de datos.

    Returns:
        DocenteModel: Un objeto que representa la tabla docente.
    """
    return EvaluacionModel()