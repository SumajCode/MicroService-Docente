from conn import connect_sql, connect_postgres

def create_table(table: str, props: dict):
    columns = props.keys()
    attributes = [props[key] for key in columns]
    
    print(columns)
    pass

