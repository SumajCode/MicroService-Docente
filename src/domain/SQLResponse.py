from scripts.execute import Ejecutar
from scripts.formater import Formater

class RespuestaSQL:

    def __init__(self):
        self.ejecutor = Ejecutar()
        self.formater = Formater()
    
    def rgetSQL(self, query):
        """
        Executes a SQL query and returns the result in JSON format.

        query: An SQL query string.

        return: The JSON formatted result of the query execution.
        """
        print("Consulta: ", query)
        return self.formater.json(self.ejecutor.ejecutarConsulta(query))
    
    def deleteAndGetSQL(self, querys):
        """
        Executes a sequence of SQL queries and returns the result of the first query.

        This method takes a list of SQL query strings and executes the first query.
        It then executes the second query, typically a delete operation, without
        returning its result. The result of the first query is returned in JSON format.

        querys: A list of SQL query strings, where the first query's result
                    is returned and the second query is executed without returning
                    its result.
        
        return: The JSON formatted result of the first query execution.
        """

        respuesta = self.ejecutor.ejecutarConsulta(querys[0])
        self.ejecutor.ejecutarConsulta(querys[1])
        return self.formater.json(respuesta)