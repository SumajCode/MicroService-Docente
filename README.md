# API Microservice

Microservicio RESTful desarrollado en Flask para la gestión de docentes, materias y matrículas. El proyecto está estructurado de forma modular y utiliza migraciones, variables de entorno y buenas prácticas para desarrollo profesional.

---

# Entorno de deploy

URL deploy de servicio de docente
[https://microservice-docente.onrender.com/apidocentes/v1](https://microservice-docente.onrender.com/apidocentes/v1)

---

## 🚀 Características

- Arquitectura modular y escalable
- Rutas agrupadas por recursos (docentes, materias, matrículas)
- Controladores y modelos desacoplados
- Migraciones automáticas de base de datos
- Configuración por variables de entorno
- Soporte para CORS y middlewares
- Entorno virtual recomendado

---

## 📁 Estructura del Proyecto

```
api/
├── README.md
├── __init__.py
├── src/
│   ├── main.py
│   ├── config/
│   │   └── conf.py
│   ├── domain/
│   ├── features/
│   ├── hooks/
│   ├── infra/
│   │   ├── controllers/
│   │   │   └── DocenteController.py
│   │   ├── db/
│   │   ├── models/
│   │   │   └── DocenteModel.py
│   │   └── routes/
│   │       ├── apigs.py
│   │       ├── DocentesRoutes.py
│   │       ├── MateriasRoutes.py
│   │       └── MatriculasRoutes.py
│   ├── scripts/
│   │   ├── migrate.py
│   │   └── ...
│   └── shared/
├── requirements.txt
└── .env
```

---

## ⚙️ Instalación y Configuración

### 1. Clona el repositorio y navega al directorio del proyecto

```bash
git clone https://github.com/SumajCode/MicroService-Docente.git
cd APIMicroservice/api
```

### 2. Crea y activa un entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configura las variables de entorno

Crea un archivo `.env` en la raíz de `api/` con, por ejemplo:

```env
FLASK_APP=src/main.py
FLASK_DEBUG=1
APP_NAME=APIMicroservice
APP_VERSION=1.0.0
HOST=localhost
PORT_API=4003
ENV_DEV=True
# Configuración de base de datos
SQL_USER = "sql5786286"
SQL_PASSWORD = "YUztaGWNrF"
SQL_HOST = "sql5.freesqldatabase.com"
SQL_PORT = 3306
SQL_DB = "sql5786286"
SQL_ACTIVE = True
# Hosts vecinos
URL_NEIGHBORG = "http://127.0.0.1:4002/api"
URL_NEIGHBORG_CONTENT = "http://127.0.0.1:4004/apicontenido/v1"
```

---

## 🗄️ Migraciones de Base de Datos

Antes de correr la aplicación, realiza las migraciones necesarias:

```bash
cd src
python -m scripts.migrate
```

---

## 🏃‍♂️ Ejecución del Servidor

Todos los comandos deben ejecutarse desde el directorio `src`:

```bash
cd src
flask run
```

La aplicación estará disponible en: [http://localhost:4003](http://localhost:4003)

---

## 🛣️ Visualizar Rutas Disponibles

```bash
cd src
flask routes
```

---

## 📦 Dependencias Principales

- Flask
- Flask-CORS
- python-dotenv
- (y otras listadas en `requirements.txt`)

---

## 🧩 Ejemplo de Código

### main.py

```python
from infra.routes.apigs import crearApp

applicacion = crearApp()

if __name__ == '__main__':
    applicacion.run()
```

### apigs.py

```python
from flask import Flask, jsonify, Blueprint
from flask_cors import CORS
from infra.routes.DocentesRoutes import blueprint as blueDocente
# ...otros imports...

def crearApp():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.conf.BaseConf')
    padreBlueprint = Blueprint('apidocentes', __name__, url_prefix='/apidocentes/v1')
    # ...rutas y blueprints...
    app.register_blueprint(padreBlueprint)
    return app
```

---

## 📚 Endpoints Principales

### Docentes

- `POST /apidocentes/v1/docente/crear` — Crea un nuevo docente.
  ```json
  {
    "nombre": "Juan",
    "apellidos": "Pérez",
    "celular": "12345678",
    "correo": "juan.perez@ejemplo.com",
    "nacimiento": "1990-01-01",
    "usuario": "juanp",
    "password": "secreto"
  }
  ```
- `PATCH /apidocentes/v1/docente/editar` — Edita los datos de un docente existente.
  ```json
  {
    "id": 1,
    "nombre": "Juan Carlos"
  }
  ```
- `DELETE /apidocentes/v1/docente/eliminar` — Elimina un docente por ID.
  ```json
  {
    "id": 1
  }
  ```
- `DELETE /apidocentes/v1/docente/eliminar/todo` — Elimina todos los docentes.
  ```json
  {}
  ```
- `POST /apidocentes/v1/docente/login` — Autentica a un docente.
  ```json
  {
    "usuario": "juanp",
    "password": "secreto"
  }
  ```
- `GET /apidocentes/v1/docente/listar/id` — Obtiene un docente por ID (en query params o body).
  `/apidocentes/v1/docente/listar/id?id=1`
- `GET /apidocentes/v1/docente/listar` — Lista todos los docentes.
  `/apidocentes/v1/docente/listar`
- `GET /apidocentes/v1/docente/materias` — Lista las materias asociadas a un docente (por ID en query/body).
  `/apidocentes/v1/docente/materias?id=1`

### Materias

- `POST /apidocentes/v1/materia/crear` — Crea una nueva materia.
  ```json
  {
    "nombre": "Matemáticas",
    "codigo": "MAT101"
  }
  ```
- `PATCH /apidocentes/v1/materia/editar` — Edita los datos de una materia.
  ```json
  {
    "id": 1,
    "nombre": "Matemáticas Avanzadas"
  }
  ```
- `DELETE /apidocentes/v1/materia/eliminar` — Elimina una materia por ID.
  ```json
  {
    "id": 1
  }
  ```
- `DELETE /apidocentes/v1/materia/eliminar/todo` — Elimina todas las materias.
  ```json
  {}
  ```
- `GET /apidocentes/v1/materia/docentes` — Lista los docentes asociados a una materia (por ID en query/body).
  `/apidocentes/v1/materia/docentes?id=1`
- `GET /apidocentes/v1/materia/listar/id` — Obtiene una materia por ID.
  `/apidocentes/v1/materia/listar/id?id=1`
- `GET /apidocentes/v1/materia/listar` — Lista todas las materias.
  `/apidocentes/v1/materia/listar`

### Matrículas

- `POST /apidocentes/v1/matricula/crear` — Crea una nueva matrícula.
  ```json
  {
    "id_estudiante": 1,
    "id_materia": 2
  }
  ```
- `POST /apidocentes/v1/matricula/crear/matriculas` — Crea varias matrículas en lote.
  ```json
  {
    "matriculas": [
      {"id_estudiante": 1, "id_materia": 2},
      {"id_estudiante": 2, "id_materia": 3}
    ]
  }
  ```
- `POST /apidocentes/v1/matricula/crear/matricula/id` — Crea matrículas por ID de materia.
  ```json
  {
    "id_materia": 2,
    "estudiantes": [1, 2, 3]
  }
  ```
- `DELETE /apidocentes/v1/matricula/eliminar` — Elimina una matrícula por ID.
  ```json
  {
    "id": 1
  }
  ```
- `GET /apidocentes/v1/matricula/listar/estudiante` — Lista matrículas por ID de estudiante.
  `/apidocentes/v1/matricula/listar/estudiante?id=1`
- `GET /apidocentes/v1/matricula/listar/materia` — Lista matrículas por ID de materia.
  `/apidocentes/v1/matricula/listar/materia?id=2`

---

## 📝 Notas

- Siempre activa el entorno virtual antes de instalar dependencias o ejecutar la aplicación.
- Usa variables de entorno para evitar exponer información sensible.
- Realiza las migraciones antes de iniciar el servidor si hay cambios en los modelos.
- El archivo de configuración `conf.py` centraliza la lectura de variables de entorno.

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un issue o un pull request para sugerencias o mejoras.
