from scripts.execute import Ejecutar

def test_conectar():
    conn = Ejecutar().ejecutarConsulta("SHOW FULL TABLES FROM otb_linde;")

test_conectar()