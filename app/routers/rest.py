from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import List
from ..db import db
from ..schemas.models import Alumno
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
def create_alumno(alumno: Alumno):
    new_id = len(db) + 1
    new_alumno = alumno.dict()
    new_alumno["id"] = new_id
    db.append(new_alumno)
    return new_alumno
