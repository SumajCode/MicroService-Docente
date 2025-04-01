from db import Table, Column
from db.DataType import *

class Student:
    
    def __init__(self):
        self.student = Table(
            'student',
            Column('id', DataType.Integer(), primary_key = True),
            Column('nombre', DataType.String())
            )

    def __str__(self):
        return f"Estudiante: {self.student.query_table()}"
    