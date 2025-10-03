import strawberry
from strawberry.fastapi import GraphQLRouter
from typing import List
from ..db import db

@strawberry.type
class Nota:
    id: int
    valor: float

@strawberry.type
class Curso:
    id: int
    nombre: str
    notas: List[Nota]

@strawberry.type
class Alumno:
    id: int
    nombre: str
    cursos: List[Curso]

def dict_to_nota(nota_dict):
    return Nota(id=nota_dict["id"], valor=nota_dict["valor"])

def dict_to_curso(curso_dict):
    return Curso(
        id=curso_dict["id"],
        nombre=curso_dict["nombre"],
        notas=[dict_to_nota(nota) for nota in curso_dict["notas"]]
    )

def dict_to_alumno(alumno_dict):
    return Alumno(
        id=alumno_dict["id"],
        nombre=alumno_dict["nombre"],
        cursos=[dict_to_curso(curso) for curso in alumno_dict["cursos"]]
    )

# Query
@strawberry.type
class Query:
    @strawberry.field
    def alumnos(self) -> List[Alumno]:
        return [dict_to_alumno(alumno) for alumno in db]

# Mutation
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_alumno(self, nombre: str) -> Alumno:
        new_id = len(db) + 1
        nuevo_alumno = {
            "id": new_id,
            "nombre": nombre,
            "cursos": []
        }
        db.append(nuevo_alumno)
        return dict_to_alumno(nuevo_alumno)

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
