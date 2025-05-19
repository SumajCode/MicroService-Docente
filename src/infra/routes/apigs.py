from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

from ..controllers.DocenteController import DocenteController
# from ..controllers.MateriaController import MateriaController
# from ..controllers.EvaluacionController import EvaluacionController
from ..controllers.MatriculaController import MatriculaController

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

@app.route('/recolectarDatos', methods=['GET'])
def recolectarDatos():
    return MatriculaController().listar(request)

if __name__ == '__main__' :
    app.run()