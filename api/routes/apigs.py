from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

from hooks.docs.ReadingDocs import *

def crearApp():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('conf.BaseConf')
    return app

app = crearApp()

@app.route('/')
def home():
    return jsonify({
        'data': f"{app.config['APP_NAME']+ '-' + app.config['APP_VERSION']} is running", 
        'message' : 'OK', 
        'status' : 200
    })



@app.route('/recolectarDatos/xls', methods=['POST'])
def recolectarDatosXLS():
    return jsonify({
        'data': leerXLS(request.form.get['file']),
        'message' : 'OK',
        'status' : 200
    })

@app.route('/recolectarDatos/pdf', methods=['POST'])
def recolectarDatosPDF():
    return jsonify({
        'data': leerPDF(request.form.get['file']),
        'message' : 'OK',
        'status' : 200
    })


if __name__ == '__main__' :
    app.run()