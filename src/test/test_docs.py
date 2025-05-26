from src.scripts.docs.ReadingDocs import ReadingDocs

def test_xls():
    print("=====================XLSX=====================")
    datos = ReadingDocs.leerXLS("C:/Users/USER/Downloads/Test de insercion de datos a database.xlsx")
    assert isinstance(datos, list)
    assert all(isinstance(row, dict) for row in datos)
    # assert all()

def test_pdf():
    print("=====================PDF======================")
    datos = ReadingDocs.leerPDF("C:/Users/USER/Downloads/Test de insercion de datos a database.pdf")
    assert isinstance(datos, list)
    assert all(isinstance(row, dict) for row in datos)