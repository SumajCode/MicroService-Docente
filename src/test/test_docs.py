from scripts.docs.ReadingDocs import ReadingDocs
readingDocs = ReadingDocs()
def test_xls():
    print("=====================XLSX=====================")
    datos = readingDocs.leerXLS("C:/Users/USER/Downloads/Test de insercion de datos a database.xlsx")
    print(datos)
    assert isinstance(datos, list)
    assert all(isinstance(row, dict) for row in datos)
    # assert all()

def test_pdf():
    print("=====================PDF======================")
    datos = readingDocs.leerPDF("C:/Users/USER/Downloads/Test de insercion de datos a database.pdf")
    print(datos)
    assert isinstance(datos, list)
    assert all(isinstance(row, dict) for row in datos)

test_xls()

test_pdf()