from infra.routes.apigs import crearApp
from config.conf import BaseConf

applicacion = crearApp()

if __name__ == '__main__':
    if BaseConf.ENV_DEV:
        applicacion.run(host=BaseConf.HOST, port=BaseConf.PORT_API)
    applicacion.run()