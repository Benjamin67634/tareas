from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, time

class UsuariosSchema(BaseModel):
    Nombre : str = Field(min_length=3, max_length=100)
    correo= EmailStr
    contra = str = Field(min_length=8)
    
class TareasSchema(BaseModel):
    Nombre_tarea: str = Field(min_length=1, max_length=200)
    descripcion= Optional[str] = None
    prioridad: str = "medio"
    tipo: str = "personal"