from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import List
from ..db import db
from ..schemas.models import Alumno, AlumnoCreate, AlumnoPatch
from ..config import JWT_SECRET

router = APIRouter(prefix="/alumnos", tags=["REST"])

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.scheme != "Bearer" or credentials.credentials != JWT_SECRET:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido"
        )

#Get para todos los alumnos
@router.get("/", response_model=List[Alumno])
def get_alumnos():
    return db

#Get para un alumno por ID
@router.get("/{alumno_id}", response_model=Alumno)
def get_alumno_by_id(alumno_id: int):
    for alumno in db:
        if alumno["id"] == alumno_id:
            return alumno
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

#Post para crear un nuevo alumno
@router.post("/", response_model=Alumno, dependencies=[Depends(verify_token)])
def create_alumno(alumno: AlumnoCreate):
    new_id = len(db) + 1
    new_alumno = alumno.dict()
    new_alumno["id"] = new_id
    db.append(new_alumno)
    return new_alumno

#Put para reemplazar completamente un alumno
@router.put("/{alumno_id}", response_model=Alumno, dependencies=[Depends(verify_token)])
def replace_alumno(alumno_id: int, alumno_actualizado: Alumno):
    for i, alumno in enumerate(db):
        if alumno["id"] == alumno_id:
            updated_alumno = alumno_actualizado.dict()
            updated_alumno["id"] = alumno_id
            db[i] = updated_alumno
            return updated_alumno
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

#Patch para modificar parcialmente un alumno
@router.patch("/{alumno_id}", response_model=Alumno, dependencies=[Depends(verify_token)])
def update_alumno_partial(alumno_id: int, alumno_patch: AlumnoPatch):
    for i, alumno in enumerate(db):
        if alumno["id"] == alumno_id:
            # Solo actualizar campos que no sean None
            if alumno_patch.nombre is not None:
                db[i]["nombre"] = alumno_patch.nombre
            if alumno_patch.cursos is not None:
                db[i]["cursos"] = alumno_patch.cursos
            return db[i]
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

#Delete para eliminar un alumno
@router.delete("/{alumno_id}", dependencies=[Depends(verify_token)])
def delete_alumno(alumno_id: int):
    for i, alumno in enumerate(db):
        if alumno["id"] == alumno_id:
            deleted_alumno = db.pop(i)
            return {"message": f"Alumno {deleted_alumno['nombre']} eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Alumno no encontrado")
