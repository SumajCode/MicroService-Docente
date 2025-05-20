from ..scripts.execute import Ejecutar

def test_conectarPostgres():
    conn = Ejecutar().ejecutarConsulta("SELECT ci_socio, nombre_socio, apellidos_socio, fecha_afiliacion FROM socio;")
    columnas = ['ci_socio', 'nombre_socio', 'apellidos_socio', 'fecha_afiliacion']
    for column in conn:
        for columna in columnas:

            print(f"{columna}: {column[columna]}")

test_conectarPostgres()