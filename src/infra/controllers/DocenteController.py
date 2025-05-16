from errors.ErrorsClients import *
class DocenteController:

    def __init__(self):
        pass

    def get(self, id: int):
        try:
            # logica crear usuario
            return jsonify({
                'data': f"{app.config['APP_NAME']+ '-' + app.config['APP_VERSION']} is running", 
                'message' : 'OK', 
                'status' : 200
            })
        except Exception as e:
            return jsonify({
                'message' : 'Acceso denegado.', 
                'status' : 401
            })

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass