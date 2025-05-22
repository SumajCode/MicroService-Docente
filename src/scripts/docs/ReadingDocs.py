import openpyxl
import pdfplumber

from ...scripts.formater import Formater

class ReadingDocs:
    def __init__(self):
        pass

    def leerXLS(ruta: str):
        print(ruta)
        lector = openpyxl.load_workbook(ruta).active
        nombreColumnas = [lector.cell(row=1, column=i).value for i in range(1, lector.max_column + 1)]
        return Formater().formatoJSONDesdeXLS(nombreColumnas, lector)

    def leerPDF(ruta: str):
        with pdfplumber.open(ruta) as pdf:
            preTabla = pdf.pages[0].extract_table()
            tabla = []
            for fila in preTabla:
                if None in fila:
                    fila.insert(fila.index(None), '')
                    fila.remove(None)
                tabla.append(fila)
            nombreColumnas = tabla[0]
            preValores = [fila for fila in tabla[1:]]
        return Formater().formatoJSONDesdePDF(nombreColumnas, preValores)