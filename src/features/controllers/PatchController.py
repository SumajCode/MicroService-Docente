from domain.PatchResponse import RespuestaPatch
from scripts.formater import Formater
from scripts.execute import Ejecutar
from infra.db.sql.UpdateSQL import UpdateSQL
from features.controllers.enums.EnumControllers import OptionsPatch

class PatchController(RespuestaPatch):
    def __init__(self, mode: str = OptionsPatch.ONE):
        self.mode = mode
        super().__init__(self, Formater(), Ejecutar(), UpdateSQL())

    def __call__(self, *args, **kwargs):
        try:
            match self.mode:
                case OptionsPatch.ONE:
                    return self.rget(*args, **kwargs)
                case OptionsPatch.ALL:
                    return self.rallpost(*args, **kwargs)
        except ValueError as excep:
            return self.formater.json({'message' : str(excep), 'status' : 500})