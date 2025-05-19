from ..scripts.execute import Ejecutar

def test_conectarPostgres():
    conn = Ejecutar().ejecutarConsulta("SELECT * FROM socio;")
    print(conn)

test_conectarPostgres()