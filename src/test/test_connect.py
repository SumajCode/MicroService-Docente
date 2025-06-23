from scripts.execute import Ejecutar
from config.conf import BaseConf
def test_conectar():
    conn = Ejecutar().ejecutarConsulta(f"SHOW FULL TABLES FROM {BaseConf.SQL_DB};")
    if conn: 
        print("Conectado.")

test_conectar()