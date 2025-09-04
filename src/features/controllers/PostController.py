from domain.PostResponse import RespuestaPost
from scripts.formater import Formater
from scripts.execute import Ejecutar
from infra.db.sql.InsertSQL import InsertSQL
from features.controllers.enums.EnumControllers import OptionsPost

class PostController(RespuestaPost):
    def __init__(self, mode: str = OptionsPost.ONE):
        self.mode = mode
        super().__init__(self, Formater(), Ejecutar(), InsertSQL())
    
    def __call__(self, *args, **kwargs):
        try:
            match self.mode:
                case OptionsPost.ONE:
                    return self.rpost(*args, **kwargs)
                case OptionsPost.ALL:
                    return self.rallpost(*args, **kwargs)
        except ValueError as excep:
            return self.formater.json({'message' : str(excep), 'status' : 500})

