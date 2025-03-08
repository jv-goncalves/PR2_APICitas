from datetime import date
from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    nif_nie_usuario: str
    nombre_usuario: str
    apellido1_usuario: Optional[str] = None
    apellido2_usuario: Optional[str] = None

class UsuarioCreate(Usuario):
    contraseña: str

class UsuarioOut(Usuario):
    class Config:
        orm_mode = True

class UsuarioUpdate(Usuario):
    nombre_usuario: Optional[str] = None
    apellido1_usuario: Optional[str] = None
    apellido2_usuario: Optional[str] = None
    contraseña: Optional[str] = None

    class Config:
        extra = "forbid"














class Clinica(BaseModel):
    cif: str
    nombre_clinica: str
    direccion_clinica: str
    capacidad_clinica: str 

class CitasOut(BaseModel):
    id_cita: int
    fecha_cita: date
    especialista_cita: str
    razon_cita: str | None
    nombre_usuario: str
    apellido1_usuario: str | None
    apellido2_usuario: str | None



class Citas(BaseModel):
    id_cita: int
    nif_nie_usuario: str
    cif_clinica: str
    especialista_cita: str
    fecha_cita: date
    razon_cita: str | None = None

class CitasCreate(BaseModel):  # Ya no hereda de Citas
    nif_nie_usuario: str
    cif_clinica: str
    especialista_cita: str
    fecha_cita: date
    razon_cita: str | None = None

class CitasOut(Citas):
    nombre_usuario: str
    apellido1_usuario: str
    apellido2_usuario: str

    class Config:
        from_attributes = True



class CitaUpdate(BaseModel):
    especialista_cita: Optional[str] = None
    fecha_cita: Optional[date] = None
    razon_cita: Optional[str] = None

    class Config:
        extra = "forbid"
