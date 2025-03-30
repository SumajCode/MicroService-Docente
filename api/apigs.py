import json
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

from hooks.docs.reading_docs import read_xls

def create_app():
    app = Flask(__name__)
    app.config.from_object('conf.BaseConf')
    return app

app = create_app()

@app.route('/')
def home():
    return f"{app.config['APP_NAME']+ '-' + app.config['APP_VERSION']} is running SIN DEBUG"

@app.route('/recolectarDatos', methods=['GET'])
def recolectarDatos():
    return jsonify({'data': read_xls(request.args['path'])})

if __name__ == '__main__' :
    app.run()