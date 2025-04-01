import Column

class Table:
    def __init__(self, name: str, **columns: Column):
        self.name = name
        self.columns = columns

    def query_table(self):
        values = [i.column_sql() for i in self.columns]
        return f"CREATE TABLE {self.name} ({",".join(values)})"