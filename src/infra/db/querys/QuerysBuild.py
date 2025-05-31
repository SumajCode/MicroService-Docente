def consultaParaDocenteMaterias(idDocente):
    """
    Consulta para obtener todas las materias impartidas por un docente determinado junto con el número de estudiantes matriculados en cada materia.

    Parameters
    ----------
    idDocente : int
        Identificador del docente cuyas materias se quieren obtener.

    Returns
    -------
    str
        Consulta SQL para obtener las materias impartidas por el docente especificado, incluyendo el nombre de la materia, nivel de estudio, 
        y el número de estudiantes matriculados en cada materia.
    """

    return f"""
SELECT
    M.nombre_materia AS NombreMateria,
    M.nivel_estudio AS NivelEstudio,
    (SELECT COUNT(*) FROM matricula WHERE M.id = matricula.id_materia) as NumeroEstudiantes
FROM materia AS M
INNER JOIN docente AS D ON M.id_docente = D.id
WHERE D.id = {idDocente}
"""

def consultaParaMateriaDocentes(idMateria):
    """
    Consulta para obtener todos los docentes que imparten una materia determinada
    
    Parameters
    ----------
    idMateria : int
        Identificador de la materia en la que se quieren obtener los docentes
    Returns
    -------
    str
        Consulta SQL para obtener los docentes que imparten la materia
    """
    return f"""
SELECT
    D.nombre AS NombreDocente,
    D.apellidos AS ApellidosDocente,
    D.correo AS CorreoDocente,
    D.usuario AS UsuarioDocente
FROM docente AS D
INNER JOIN materia AS M ON D.id = M.id_docente
WHERE M.id = {idMateria}
"""

def consultaParaMateriaMatriculados(idMateria):
    """
    Consulta para obtener todos los estudiantes matriculados en una materia determinada
    
    Parameters
    ----------
    idMateria : int
        Identificador de la materia en la que se quieren obtener los estudiantes matriculados
    Returns
    -------
    str
        Consulta SQL para obtener los estudiantes matriculados en la materia
    """
    
    return f"""
SELECT * FROM matricula WHERE id_materia = {idMateria}
"""

def consultaPorId(id, columnas: list, nombreTabla):
    return f"""
SELECT DISTINCT {','.join(columnas)} FROM {nombreTabla} WHERE {nombreTabla}.id = {id};
"""

def eliminarDocenteYMateria(idDocente):
    return f"""
DELETE FROM docente WHERE docente.id = {idDocente};
DELETE FROM materia WHERE materia.id_docente = {idDocente};
"""

def eliminarMatriculadosPorMateria(idMateria):
    return [f"""SELECT * FROM matricula WHERE matricula.id = {idMateria}""", f"""
DELETE FROM materia WHERE materia.id = {idMateria};
DELETE FROM matricula WHERE matricula.id_materia = {idMateria};
"""]
