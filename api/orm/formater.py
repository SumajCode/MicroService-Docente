
def format_sql_insert(table: str, columns: list, values: list) -> list:
  query = f"INSERT INTO {table} (" + ",".join(columns) + ") VALUES "
  return query + ",".join(["(" + ",".join(value) + ")" for value in values])

