from pydantic import BaseModel
from typing import List

class Nota(BaseModel):
    id: int
    valor: float

class Curso(BaseModel):
    id: int
    nombre: str
    notas: List[Nota]

class Alumno(BaseModel):
    id: int
    nombre: str
    cursos: List[Curso]
