import hashlib

class RespuestaPost:

    def __init__(self, formater, ejecutar, insert):
        self.ejecutor = ejecutar
        self.formater = formater
        self.insert = insert

    def rpost(self, data):
        """
        Maneja la respuesta para una peticion POST.

        Devuelve un JSON con los datos de la respuesta de la consulta, si no
        hubo errores en la consulta. Si hubo errores, devuelve un JSON con
        el mensaje de error y el codigo de estado.

        :param data: Diccionario con los datos de la peticion.
        :type data: dict
        :return: Un JSON con los datos de la respuesta de la consulta.
        :rtype: json
        """
        try:
            datosCripto = data
            keys = datosCripto['datos'].keys()
            if 'password' in keys:
                datosCripto['datos']['password'] = hashlib.sha256(datosCripto['datos']['password'].encode()).hexdigest()
            query = self.insert.insertarEnTabla(datosCripto['tabla'], datosCripto['datos'])
            dataQuery = self.ejecutor.ejecutarConsulta(query)
            return self.formater.json(dataQuery)
        except Exception as excep:
            return self.formater.json({
                'message' : str(excep),
                'status' : 500
            })
    
    def rallpost(self, data):
        """
        Maneja la respuesta para una peticion POST con multiples datos.

        Devuelve un JSON con los datos de la respuesta de la consulta, si no
        hubo errores en la consulta. Si hubo errores, devuelve un JSON con
        el mensaje de error y el codigo de estado.

        data: Diccionario con los datos de la peticion.
        
        return: Un JSON con los datos de la respuesta de la consulta.
        """
        try:
            query = self.insert.insertarTodoEnTabla(data['tabla'], data['datos'])
            data = self.ejecutor.ejecutarConsulta(query)
            return self.formater.json(data)
        except Exception as excep:
            return self.formater.json({
                'message' : str(excep),
                'status' : 500
            })