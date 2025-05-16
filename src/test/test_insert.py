from orm.db.Query import insertarEnTabla
def queryInsert():
    consulta = insertarEnTabla(
        nombreTabla="test",
        datos={
            "id": 1,
            "name": "test",
            "email": "test"
        }
    )
    print(consulta)

queryInsert()