class BaseConf():
    APP_NAME = "YalaSoft XD"
    APP_VERSION = "1.0.0"
    API_URL = "http://127.0.0.1"
    SECRET_KEY = ""
    DEBUG = True
    TESTING = False

    POSTGRES_USER = ""
    POSTGRES_PASSWORD = ""
    POSTGRES_HOST = ""
    POSTGRES_PORT = ""
    POSTGRES_DB = ""
    POSTGRES_ACTIVE = False

    SQL_USER = ""
    SQL_PASSWORD = ""
    SQL_HOST = ""
    SQL_PORT = ""
    SQL_DB = ""
    SQL_ACTIVE = False

    SMTP_HOST = ""
    SMTP_PORT = ""
    SMTP_USER = ""
    SMTP_PASSWORD = ""

    GOOGLE_AUTENTICATION_CLIENT_ID = ""
    GOOGLE_AUTHENTICATION_CLIENT_SECRET = ""

    CODE_COMPILATOR_CLIENT_ID = ""
    CODE_COMPILATOR_CLIENT_SECRET = ""

    CODE_IA_API_KEY = ""
    CODE_IA_CLIENT_ID = ""
    CODE_IA_CLIENT_SECRET = ""

    PUBLISHER_URL = ""
    PUBLISHER_USER = ""
    PUBLISHER_PASSWORD = ""

class DevConf(BaseConf):
    pass

class ProdConf(BaseConf):
    DEBUG = False
    TESTING = False
    pass