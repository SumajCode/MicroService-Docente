class Formater:
  def __init__(self):
    pass

  def formatoSQLInsertar(self, tabla: str, columnas: list, valores: list) -> list:
    query = f"INSERT INTO {tabla} (" + ",".join(columnas) + ") VALUES "
    return query + ",".join(["(" + ",".join(value) + ")" for value in valores])

