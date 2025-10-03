from pydantic import BaseModel
from typing import List, Optional

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

# Modelo para crear alumnos (sin ID, se genera automáticamente)
class AlumnoCreate(BaseModel):
    nombre: str
    cursos: List[Curso] = []

# Modelo para PATCH (campos opcionales)
class AlumnoPatch(BaseModel):
    nombre: Optional[str] = None
    cursos: Optional[List[Curso]] = None
