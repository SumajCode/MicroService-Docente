from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import Blueprint

from infra.routes.DocentesRoutes import blueprint as blueDocente
from infra.routes.MateriasRoutes import blueprint as blueMateria
from infra.routes.MatriculasRoutes import blueprint as blueMatricula

# * Se usaran middlewares para mejorar la seguridad de las rutas y para separar
# * por clase o modulo como matricula y docente al igual que para post/puts/patch de gets

def crearApp():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.conf.BaseConf')
    padreBlueprint = Blueprint('apidocentes', __name__, url_prefix='/apidocentes/v1')
    
    @padreBlueprint.route('/')
    def home():
        """
        Root route of the API

        Returns a JSON response with the status of the API

        :return: JSON response with the status of the API
        """
        return jsonify({
            'data': f"{app.config['APP_NAME']+ '-' + app.config['APP_VERSION']} is running", 
            'message' : 'OK', 
            'status' : 200
        })
    
    padreBlueprint.register_blueprint(blueDocente)
    padreBlueprint.register_blueprint(blueMateria)
    padreBlueprint.register_blueprint(blueMatricula)
    app.register_blueprint(padreBlueprint)
    
    return app