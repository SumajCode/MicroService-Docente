from infra.db.Query import insertarEnTabla
def test_query_insert():
    consulta = insertarEnTabla(
        nombreTabla="test",
        datos={
            "id": 1,
            "name": "test",
            "email": "test"
        }
    )
    assert isinstance(consulta, str)