from flask import jsonify
from flask_cors import CORS

from flask_openapi.openapi import OpenAPI
from infra.routes.DocentesRoutes import blueprint as blueDocente
from infra.routes.MateriasRoutes import blueprint as blueMateria
from infra.routes.MatriculasRoutes import blueprint as blueMatricula

# * Se usaran middlewares para mejorar la seguridad de las rutas y para separar
# * por clase o modulo como matricula y docente al igual que para post/puts/patch de gets

def crearApp():
    app = OpenAPI(__name__)
    CORS(app)
    app.config.from_object('config.conf.BaseConf')
    
    @app.get('/', doc_ui=False)
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

    app.register_api(blueDocente)
    app.register_api(blueMateria)
    app.register_api(blueMatricula)
    
    @app.get('/routes', summary='Routes', tags=None)
    def routes():
        routes = []
        for rule in app.url_map.iter_rules():
            if not 'swagger' in rule.rule:
                routes.append(rule.rule)
        return jsonify({
            'data': routes,
            'message' : 'OK',
            'status' : 200
        })
    return app
