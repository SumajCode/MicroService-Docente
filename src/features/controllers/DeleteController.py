from domain.DeleteResponse import RespuestaDelete
from scripts.formater import Formater
from scripts.execute import Ejecutar
from infra.db.sql.DeleteSQL import DeleteSQL
from features.controllers.enums.EnumControllers import OptionsDelete

class GetController(RespuestaDelete):
    def __init__(self, mode: str = OptionsDelete.ONE):
        self.mode = mode
        super().__init__(self, Formater(), Ejecutar(), DeleteSQL())

    def __call__(self, *args, **kwargs):
        try:
            match self.mode:
                case OptionsDelete.ONE:
                    return self.rget(*args, **kwargs)
                case OptionsDelete.ALL:
                    return self.rallpost(*args, **kwargs)
        except ValueError as excep:
            return self.formater.json({'message' : str(excep), 'status' : 500})