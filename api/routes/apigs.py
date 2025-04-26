from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

from errors.ErrorsClients import *
from errors.ErrorsServer import *

from hooks.docs.reading_docs import read_xls

def createApp():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('conf.BaseConf')
    return app

app = createApp()

@app.errorhandler(HTTPException)
def handle_error(e):
    return jsonify({
        'data': e.description, 
        'message' : e.name, 
        'status' : e.code
    }), e.code

@app.route('/')
def home():
    return jsonify({
        'data': f"{app.config['APP_NAME']+ '-' + app.config['APP_VERSION']} is running", 
        'message' : 'OK', 
        'status' : 200
    })

@app.route('/recolectarDatos', methods=['POST'])
def recolectarDatos():
    return jsonify({
        'data': read_xls(request.args['path']), 
        'message' : 'OK',
        'status' : 200
    })

@app.route('/error')
def handleErrors():
    if () :
        raise ServerError()

if __name__ == '__main__' :
    app.run()