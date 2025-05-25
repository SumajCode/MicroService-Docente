import os
from dotenv import load_dotenv

load_dotenv()

class BaseConf():

    def get_bool_env(var_name, default=False):
        val = os.getenv(var_name, str(default))
        return val.lower() in ('true', '1', 't', 'yes', 'y')

    APP_NAME = os.getenv("APP_NAME")
    APP_VERSION = os.getenv("APP_VERSION")
    HOST = os.getenv("HOST")
    PORT_API = os.getenv("PORT_API")
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = get_bool_env("DEBUG")
    TESTING = get_bool_env("TESTING")

    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_ACTIVE = get_bool_env("POSTGRES_ACTIVE")

    SQL_USER = os.getenv("SQL_USER")
    SQL_PASSWORD = os.getenv("SQL_PASSWORD")
    SQL_HOST = os.getenv("SQL_HOST")
    SQL_PORT = os.getenv("SQL_PORT")
    SQL_DB = os.getenv("SQL_DB")
    SQL_ACTIVE = get_bool_env("SQL_ACTIVE")

    SMTP_HOST = os.getenv("SMTP_HOST")
    SMTP_PORT = os.getenv("SMTP_PORT")
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

    GOOGLE_AUTENTICATION_CLIENT_ID = os.getenv("GOOGLE_AUTENTICATION_CLIENT_ID")
    GOOGLE_AUTHENTICATION_CLIENT_SECRET = os.getenv("GOOGLE_AUTHENTICATION_CLIENT_SECRET")

    # CODE_IA_API_KEY = os.getenv("CODE_IA_API_KEY")
    # CODE_IA_CLIENT_ID = os.getenv("CODE_IA_CLIENT_ID")
    # CODE_IA_CLIENT_SECRET = os.getenv("CODE_IA_CLIENT_SECRET")

    PUBLISHER_URL = os.getenv("PUBLISHER_URL") # url del servidor de contenido
    PUBLISHER_USER = os.getenv("PUBLISHER_USER")
    PUBLISHER_PASSWORD = os.getenv("PUBLISHER_PASSWORD")

class DevConf(BaseConf):
    pass

class ProdConf(BaseConf):
    DEBUG = False
    TESTING = False
    pass