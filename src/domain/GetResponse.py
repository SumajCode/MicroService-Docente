from scripts.execute import Ejecutar
from scripts.formater import Formater
from infra.db.sql.SelectSQL import SelectSQL

class RespuestaGet:

    def __init__(self):
        self.ejecutor = Ejecutar()
        self.formater = Formater()
        self.selectSQL = SelectSQL()
    
    def getDatosDB(self, opciones):
        """
        Consulta los datos de una tabla y los devuelve en formato JSON
        ordenados de acuerdo a las opciones dadas.

        opciones (dict): Diccionario con las opciones de consulta.
                Debe contener las claves 'tabla', 'columnas', 'columnaOrden',
                'asc', 'desc' y 'columnaAgrupar'.
        Returns:
            JSON con los datos de la tabla ordenados de acuerdo a las opciones
            dadas.
        """
        temporalDatos = None
        if opciones['columnas'] is not None:
            temporalDatos = self.ejecutor.ejecutarConsulta(self.selectSQL.ordenarPor(
                    opciones['tabla'],
                    opciones['columnas'],
                    opciones['columnaOrden'],
                    opciones['asc'],
                    opciones['desc'],
                    opciones['columnaAgrupar']
                ))
        return self.formater.json(self.formater.formatoResSQL(opciones['columnas'], temporalDatos))

    def rget(self, datos):
        """
        Responde a una petici n GET con los datos obtenidos
        directamente de la base de datos.

        datos (dict): Diccionario que contiene los datos obtenidos y
            las opciones de consulta.

        Returns:
            Un objeto JSON con los datos obtenidos y el mensaje 'OK'
            o un objeto JSON con un mensaje de error y el status 500.
        """
        try:
            datosObtenidos = datos['datosObtenidos']
            opciones = datos['opciones']
            # condiciones = datos['condiciones']
            if datosObtenidos is None and 'tabla' in opciones.keys():
                return self.getDatosDB(opciones)
            # if condiciones is not None:
            #     return self.getDatosDBJoin(opciones, condiciones)
            return self.formater.json(datosObtenidos)
        except Exception as excep:
            return self.formater.json({
                'message' : str(excep),
                'status' : 500
            })