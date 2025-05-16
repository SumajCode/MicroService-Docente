from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

from ..hooks.docs.ReadingDocs import ReadingDocs
from controllers import *

def crearApp():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('api.conf.BaseConf')
    return app

app = crearApp()

@app.route('/')
def home():
    DocenteController().post(dict) # tiene controllar respuesta de error y aceptada

@app.route('/recolectarDatos/xls', methods=['POST'])
def recolectarDatosXLS():
    return jsonify({
        'data': ReadingDocs.leerXLS(request.form.get['file']),
        'message' : 'OK',
        'status' : 200
    })

@app.route('/recolectarDatos/pdf', methods=['POST'])
def recolectarDatosPDF():
    return jsonify({
        'data': ReadingDocs.leerPDF(request.form.get['file']),
        'message' : 'OK',
        'status' : 200
    })


if __name__ == '__main__' :
    app.run()