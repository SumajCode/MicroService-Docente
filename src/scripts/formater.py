# 
class Formater:
  def __init__(self):
    pass

  def formatoJSONDesdeXLS(self, nombreColumnas, lector):
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
    valores = []
    for fila in preValores:
      preFila = []
      for valor in fila:
        preFila.append(valor)
      valores.append(preFila)
    return self.formatoJSON(nombreColumnas, valores)

  def formatoJSON(self, nombreColumnas: list, datos: list[list]):
    nuevosValores=[]
    for dato in datos:
      datosEstruturados = {}
      for i in range(len(nombreColumnas)):
        datosEstruturados[nombreColumnas[i]] = str(dato[i]) if isinstance(dato[i],str) and not dato[i].isdigit() else int(dato[i])
      nuevosValores.append(datosEstruturados)
    return nuevosValores