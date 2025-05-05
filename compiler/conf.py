class BaseConf():
    APP_NAME = "YalaSoft XD"
    APP_VERSION = "1.0.0"
    HOST = "http://127.0.0.1"
    PORT_API = 5000
    SECRET_KEY = ""
    DEBUG = True
    TESTING = False

    MONGODB_USER = ""
    MONGODB_PASSWORD = ""
    MONGODB_HOST = ""
    MONGODB_PORT = ""
    MONGODB_DB = ""
    MONGODB_ACTIVE = False

    # SMTP_HOST = ""
    # SMTP_PORT = ""
    # SMTP_USER = ""
    # SMTP_PASSWORD = ""

    # GOOGLE_AUTENTICATION_CLIENT_ID = ""
    # GOOGLE_AUTHENTICATION_CLIENT_SECRET = ""

    # CODE_URL_API_COMPILATOR = "https://ce.judge0.com"
    # CODE_COMPILATOR_CLIENT_ID = ""
    # CODE_COMPILATOR_CLIENT_SECRET = ""

    CODE_IA_API_KEY = ""
    CODE_IA_CLIENT_ID = ""
    CODE_IA_CLIENT_SECRET = ""

    PUBLISHER_URL = "" # En aca va el url de la api para guardar codigo
    PUBLISHER_USER = ""
    PUBLISHER_PASSWORD = ""

class DevConf(BaseConf):
    pass

class ProdConf(BaseConf):
    DEBUG = False
    TESTING = False
    pass