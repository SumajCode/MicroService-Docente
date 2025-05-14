from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from ..controllers.CodeController import CodeController

def createApp():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('api.conf.BaseConf')
    return app

app = createApp()

# @app.errorhandler(HTTPException)
# def handle_error(e):
#     return jsonify({
#         'data': e.description, 
#         'message' : e.name, 
#         'status' : e.code
#     }), e.code

@app.route('/')
def home():
    return jsonify({
        'data': f"{app.config['APP_NAME']+ '-' + app.config['APP_VERSION']} is running", 
        'message' : 'OK', 
        'status' : 200
    })

@app.route('/compilarCodigo', methods=['POST'])
def compilarCodigo(): 
    """Compila el codigo fuente en base al lenguaje especificado y devuelve el resultado de la compilacion.

    Parameters:
    data (str): Codigo fuente a compilar
    lang (str): Lenguaje en el que esta escrito el codigo

    Returns:
    dict: Diccionario con dos claves: 'status' y 'data'. La clave 'status'
    puede tener dos valores: 'OK' o 'Error'. La clave 'data' contendra el
    resultado de la compilacion en caso de exito o el mensaje de error en
    caso de fallo.
    """
    
    return CodeController.post(request.form.get('data'), request.form.get('lang'))

@app.route('/evaluarCodigo')
def compiler():
    return 
# @app.route('/error')
# def handleErrors():
#     if () :
#         raise ServerError()

if __name__ == '__main__' :
    app.run()