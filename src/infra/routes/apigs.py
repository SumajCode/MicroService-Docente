from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

from src.infra.controllers.DocenteController import DocenteController
from src.infra.controllers.MateriaController import MateriaController
from src.infra.controllers.EvaluacionController import EvaluacionController
from src.infra.controllers.MatriculaController import MatriculaController

# * Se usaran middlewares para mejorar la seguridad de las rutas y para separar
# * por clase o modulo como matricula y docente al igual que para post/puts/patch de gets

def crearApp():
    app = Flask(__name__)
    CORS(app)
    app.src.config.from_object('src.config.conf.BaseConf')

    @app.route('/')
    def home():
        """
        Root route of the API

        Returns a JSON response with the status of the API

        :return: JSON response with the status of the API
        """
        return jsonify({
            'dta': f"{app.config['APP_NAME']+ '-' + app.config['APP_VERSION']} is running", 
            'message' : 'OK', 
            'status' : 200
        })

    @app.route('/crearDocente', methods=['POST', 'GET'])
    def crearDocente():
        return DocenteController().crear(request)

    @app.route('/crearEvaluacion', methods=['POST', 'GET'])
    def crearEvaluacion():
        return EvaluacionController().crear(request)

    @app.route('/crearMateria', methods=['POST', 'GET'])
    def crearMateria():
        return MateriaController().crear(request)

    @app.route('/crearMatriculas', methods=['POST', 'GET'])
    def recolectarDatos():
        return MatriculaController().crear(request)

    @app.route('/obtenerDocentes', methods=['GET'])
    def obtenerDocentes():
        return DocenteController().listar()

    @app.route('/obtenerMatriculados', methods=['GET'])
    def obtenerMatriculados():
        return MatriculaController().listar(request)

    @app.route('/obtenerMaterias', methods=['GET'])
    def obtenerMaterias():
        return MateriaController().listar()

    @app.route('/obtenerMateria', methods=['GET'])
    def obtenerMateria():
        return MateriaController().listar()

    # appplication.route('/obtenerMatriculados', methods=['GET'])
    # def obtenerDocentes():
    #     return DocenteController().listar()
    return app

application = crearApp()

if __name__ == '__main__' :
    application.run()