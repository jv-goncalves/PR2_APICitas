from sqlalchemy import Column, Integer, String, ForeignKey, Date
from database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    nif_nie_usuario = Column(String, primary_key=True, unique=True, nullable=False)
    contraseña = Column(String, nullable=False)
    nombre_usuario = Column(String, nullable=False)
    apellido1_usuario = Column(String, nullable=True)
    apellido2_usuario = Column(String, nullable=True)


class Clinica(Base):
    __tablename__ = "clinicas"
    
    cif = Column(String, primary_key=True, index=True)
    nombre_clinica = Column(String, nullable=False)
    direccion_clinica = Column(String, nullable=False)
    capacidad_clinica = Column(Integer, nullable=False)


class Citas(Base):
    __tablename__ = "citas"
    
    id_cita = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nif_nie_usuario = Column(String, ForeignKey("usuarios.nif_nie_usuario"), nullable=False) 
    cif_clinica = Column(String, ForeignKey("clinicas.cif"), nullable=False)
    especialista_cita = Column(String, nullable=False)
    fecha_cita = Column(Date, nullable=False)
    razon_cita = Column(String, nullable=True)
