# GeneracionSoftware
# Flask Microservice API

Este proyecto es una API microservicio desarrollada con Flask, diseñada para proporcionar una estructura modular y fácil de mantener para el desarrollo de aplicaciones web.

## Estructura del Proyecto

```
APIMicroservice/
├── .venv/                     # Entorno virtual
├── api/                       # Directorio principal de la aplicación
│   ├── controllers/           # Controladores de rutas
│   ├── hooks/                 # Middleware y hooks
│   ├── db/                    # Módulos de base de datos
│   │   ├── conn.py            # Configuración de conexión a DB
│   │   ├── orm.py             # ORM para modelos
│   │   └── execute.py         # Funciones para ejecutar consultas
│   ├── docs/                  # Documentación de la API
│   ├── models/                # Modelos de datos
│   ├── test/                  # Pruebas unitarias y de integración
│   ├── apigs.py               # Punto de entrada principal
│   ├── conf.py                # Archivo de configuración
│   ├── init.py                # Inicialización del paquete
│   └── requirements.txt       # Dependencias del proyecto
```

## Archivo de Configuración

El proyecto utiliza un archivo de configuración (`conf.py`) que contiene todas las variables necesarias para el funcionamiento de la aplicación. La configuración se maneja a través de una clase `BaseConf`:

```python
# conf.py
class BaseConf():
    APP_NAME = "YalaSoft XD"
    SECRET_KEY = ""
    DEBUG = True
    TESTING = False

    # Configuración de PostgreSQL
    POSTGRES_USER = ""
    POSTGRES_PASSWORD = ""
    POSTGRES_HOST = ""
    POSTGRES_PORT = ""
    POSTGRES_DB = ""
    POSTGRES_ACTIVE = False

    # Configuración de SQL Server
    SQL_USER = ""
    SQL_PASSWORD = ""
    SQL_HOST = ""
    SQL_PORT = ""
    SQL_DB = ""
    SQL_ACTIVE = False

    # Configuración SMTP
    SMTP_HOST = ""
    SMTP_PORT = ""
    SMTP_USER = ""
    SMTP_PASSWORD = ""

    # Otros servicios
    GOOGLE_AUTENTICATION_CLIENT_ID = ""
    GOOGLE_AUTHENTICATION_CLIENT_SECRET = ""
    CODE_COMPILATOR_CLIENT_ID = ""
    CODE_COMPILATOR_CLIENT_SECRET = ""
    CODE_IA_CLIENT_ID = ""
    CODE_IA_CLIENT_SECRET = ""
```

## Inicialización de la Aplicación

La aplicación se inicializa a través del archivo `apigs.py`, que crea la instancia de Flask y carga la configuración:

```python
# apigs.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.src.config.from_object('api.conf.BaseConf')
    return app

app = create_app()

@app.route('/')
def home():
    return "hola"

if __name__ == '__main__':
    app.run(debug=True)
```

## Comandos para el Desarrollo

### Configuración Inicial

```bash
# Crear un entorno virtual
python -m venv .venv

# Activar el entorno virtual (Windows)
.venv\Scripts\activate

# Activar el entorno virtual (Linux/Mac)
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecutar la Aplicación en Modo Debug

```bash
# Desde la raíz del proyecto
python -m api.apigs

# O directamente si estás en el directorio api
python apigs.py
```

### Variables de Entorno (opcional)

Para mayor seguridad, puedes establecer variables de entorno para valores sensibles:

```bash
# Windows (PowerShell)
$env:SECRET_KEY="tu-clave-secreta"
$env:POSTGRES_USER="usuario-db"

# Linux/Mac
export SECRET_KEY="tu-clave-secreta"
export POSTGRES_USER="usuario-db"
```

### Pruebas

```bash
# Ejecutar todas las pruebas
python -m unittest discover -s api/test

# Ejecutar una prueba específica
python -m unittest api.test.test_nombre
```

## Acceso a Variables de Configuración

Puedes acceder a las variables de configuración dentro de tus rutas y funciones a través del objeto `app.config`:

```python
@app.route('/config-info')
def config_info():
    return {
        'app_name': app.config['APP_NAME'],
        'debug_mode': app.config['DEBUG']
    }
```

## Personalización de la Configuración

Para utilizar diferentes configuraciones según el entorno (desarrollo, pruebas, producción), puedes:

1. Crear clases adicionales que hereden de `BaseConf`:
```python
class DevConfig(BaseConf):
    DEBUG = True

class ProdConfig(BaseConf):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
```

2. Cargar la configuración según una variable de entorno:
```python
config_class = {
    'development': 'api.conf.DevConfig',
    'production': 'api.conf.ProdConfig'
}.get(os.environ.get('FLASK_ENV', 'development'))

app.src.config.from_object(config_class)
```

## Extensiones Útiles para Flask

- **Flask-RESTful**: Para crear APIs RESTful
- **Flask-SQLAlchemy**: ORM para simplificar el acceso a bases de datos
- **Flask-Migrate**: Para migraciones de base de datos
- **Flask-JWT-Extended**: Para autenticación con tokens JWT
- **Flask-Cors**: Para manejar CORS (Cross-Origin Resource Sharing)

## Problemas Comunes

- **Error de importación**: Asegúrate de que el módulo esté en el `sys.path` de Python
- **Error de configuración**: Verifica la ruta correcta al importar objetos de configuración
- **Variables no disponibles**: Confirma que la configuración se ha cargado correctamente

## Contribución

Las contribuciones son bienvenidas. Por favor, asegúrate de seguir las prácticas de código limpio y añadir pruebas para cualquier nueva funcionalidad.
