from domain.GetResponse import RespuestaGet
from scripts.formater import Formater
from scripts.execute import Ejecutar
from infra.db.sql.SelectSQL import SelectSQL
from features.controllers.enums.EnumControllers import OptionsGet

class GetController(RespuestaGet):
    def __init__(self, mode: str = OptionsGet.ONE):
        self.mode = mode
        super().__init__(self, Formater(), Ejecutar(), SelectSQL())

    def __call__(self, *args, **kwargs):
        try:
            match self.mode:
                case OptionsGet.ONE:
                    return self.rget(*args, **kwargs)
                case OptionsGet.ALL:
                    return self.rallpost(*args, **kwargs)
        except ValueError as excep:
            return self.formater.json({'message' : str(excep), 'status' : 500})