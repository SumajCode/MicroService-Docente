from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

from ..controllers.DocenteController import DocenteController
from ..controllers.MateriaController import MateriaController
from ..controllers.EvaluacionController import EvaluacionController
from ..controllers.MatriculaController import MatriculaController

# * Se usaran middlewares para mejorar la seguridad de las rutas y para separar
# * por clase o modulo como matricula y docente al igual que para post/puts/patch de gets

def crearApp():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('api.src.config.conf.BaseConf')
    return app

app = crearApp()

@app.route('/')
def home():
    return jsonify({
        'data': f"{app.config['APP_NAME']+ '-' + app.config['APP_VERSION']} is running", 
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
    return MatriculaController().listar()

@app.route('/obtenerMaterias', methods=['GET'])
def obtenerMaterias():
    return MateriaController().listar()

@app.route('/obtenerMateria', methods=['GET'])
def obtenerMateria():
    return MateriaController().listar()

# @app.route('/obtenerMatriculados', methods=['GET'])
# def obtenerDocentes():
#     return DocenteController().listar()

if __name__ == '__main__' :
    app.run()