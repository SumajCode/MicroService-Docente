from flask import jsonify

class Formater:
    def __init__(self):
        pass

    def formatoResSQL(self, columnas, temporalDatos):
        """
        Convierte una lista de filas de datos y una lista de nombres de columnas
        en una lista de diccionarios, donde cada diccionario representa una fila
        con sus respectivos valores asociados a cada columna.

        Args:
            columnas (list): Lista de nombres de columnas.
            temporalDatos (list): Lista de filas de datos.

        Returns:
            list: Lista de diccionarios, cada diccionario representa una fila con
            sus respectivos valores asociados a cada columna.
        """
        datos =[]
        for fila in temporalDatos:
            datosEstructurados = {}
            for nombreColumna in columnas:
                datosEstructurados[nombreColumna] = fila[nombreColumna]
            datos.append(datosEstructurados)
        return datos

    def json(self, datos):
        """
        Convierte una lista de datos en un objeto JSON con las siguientes
        claves:
        
        - data: la lista de datos
        - message: 'OK'
        - status: 200

        :param datos: lista de datos
        :return: objeto JSON con las claves mencionadas
        """
        nuevosDatos = []
        for dato in datos:
            datosEstructurados = {}
            for key, value in dato.items():
                datosEstructurados[key] = value if value is not None else ""
            nuevosDatos.append(datosEstructurados)
        return jsonify({
            'data':nuevosDatos,
            'message':'OK',
            'status':200
        })
    
    def formatoJSONDesdeXLS(self, nombreColumnas, lector):
        """
        Toma una lista de nombres de columnas y un objeto de lectura de excel 
        (openpyxl) y devuelve una lista de diccionarios, donde cada diccionario 
        representa una fila con sus respectivos valores asociados a cada columna.
        
        :nombreColumnas: una lista de strings que representan los nombres de 
        las columnas
        :lector: un objeto de lectura de excel (openpyxl)
        :return: una lista de diccionarios, donde cada diccionario representa una fila
        con sus respectivos valores asociados a cada columna
        """
        valoresIntro = []
        valoresColumna = []
        for j in range(2, lector.max_row + 1):
            for i in range(1, lector.max_column + 1):
                value = lector.cell(row=j, column=i).value
                valoresIntro.append(value)
            valoresColumna.append(valoresIntro)
            valoresIntro = []
        return self.formatoJSON(nombreColumnas, valoresColumna)

    def formatoJSONDesdePDF(self, nombreColumnas, preValores):
        """
        Toma una lista de nombres de columnas y una lista de listas (cada lista 
        representa una fila de datos) y devuelve una lista de diccionarios, donde
        cada diccionario representa una fila con sus respectivos valores asociados
        a cada columna.

        Se utiliza para formatear los datos leidos desde PDFs.

        Args:
        nombreColumnas (list): Nombres de las columnas
        preValores (list[list]): Valores de las columnas

        Returns:
        list[dict]: lista de diccionarios con los valores asociados a cada columna
        """

        valores = []
        for fila in preValores:
            preFila = []
            for valor in fila:
                preFila.append(valor)
            valores.append(preFila)
        return self.formatoJSON(nombreColumnas, valores)

    def formatoJSON(self, nombreColumnas: list, datos: list[list]):
        """
        Toma una lista de nombres de columnas y una lista de listas (cada lista 
        representa una fila de datos) y devuelve una lista de diccionarios, donde
        cada diccionario representa una fila con sus respectivos valores asociados
        a cada columna.

        Args:
        nombreColumnas (list): Lista de nombres de columnas.
        datos (list[list]): Lista de listas (cada lista representa una fila de datos).

        Returns:
        list: Lista de diccionarios, cada diccionario representa una fila con sus
        respectivos valores asociados a cada columna.
        """
        nuevosValores=[]
        for dato in datos:
            datosEstruturados = {}
            for i in range(len(nombreColumnas)):
                datosEstruturados[nombreColumnas[i]] = str(dato[i]) if isinstance(dato[i],str) and not dato[i].isdigit() else int(dato[i])
            nuevosValores.append(datosEstruturados)
        return nuevosValores