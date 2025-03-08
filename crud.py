from models import Usuario, Citas, Clinica
from sqlalchemy.orm import Session
from schemas import UsuarioCreate, CitasCreate, UsuarioUpdate, CitaUpdate
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder


def crear_usuario(db: Session, usuario: UsuarioCreate):
    nuevo_usuario = Usuario(
        nif_nie_usuario=usuario.nif_nie_usuario,
        contraseña=usuario.contraseña,
        nombre_usuario=usuario.nombre_usuario,
        apellido1_usuario=usuario.apellido1_usuario,
        apellido2_usuario=usuario.apellido2_usuario,
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def get_usuario(db: Session, nif: str):
    return db.query(Usuario).filter(Usuario.nif_nie_usuario == nif).first()


def update_usuario(db: Session, nif: str, usuario_update: UsuarioUpdate):
    usuario = db.query(Usuario).filter(Usuario.nif_nie_usuario == nif).first()
    if not usuario:
        return None
    
    update_data = usuario_update.dict(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(usuario, key, value)
    
    db.commit()
    db.refresh(usuario)
    return usuario



def delete_usuario(db: Session, nif: str):
    usuario = db.query(Usuario).filter(Usuario.nif_nie_usuario == nif).first()
    if not usuario:
        return None
    db.delete(usuario)
    db.commit()
    return usuario











def crear_cita(db: Session, cita: CitasCreate):
    usuario = db.query(Usuario).filter(Usuario.nif_nie_usuario == cita.nif_nie_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    clinica = db.query(Clinica).filter(Clinica.cif == cita.cif_clinica).first()
    if not clinica:
        raise HTTPException(status_code=404, detail="Clínica no encontrada")
    
    nueva_cita = Citas(
        nif_nie_usuario=cita.nif_nie_usuario,
        cif_clinica=cita.cif_clinica, 
        especialista_cita=cita.especialista_cita,
        fecha_cita=cita.fecha_cita,
        razon_cita=cita.razon_cita,
    )
    db.add(nueva_cita)
    db.commit()
    db.refresh(nueva_cita)

    # Devolvemos los datos completos con el usuario
    return jsonable_encoder({
        "id_cita": nueva_cita.id_cita,
        "nif_nie_usuario": nueva_cita.nif_nie_usuario,
        "cif_clinica": nueva_cita.cif_clinica,
        "especialista_cita": nueva_cita.especialista_cita,
        "fecha_cita": nueva_cita.fecha_cita,
        "razon_cita": nueva_cita.razon_cita,
        "nombre_usuario": usuario.nombre_usuario,
        "apellido1_usuario": usuario.apellido1_usuario,
        "apellido2_usuario": usuario.apellido2_usuario,
    })

def sacar_cita(db: Session, cita_id: int):
    resultado = (
        db.query(Citas, Usuario)
        .join(Usuario, Citas.nif_nie_usuario == Usuario.nif_nie_usuario)
        .filter(Citas.id_cita == cita_id)
        .first()
    )

    if not resultado:
        return None
    
    cita, usuario = resultado  # Desempaquetamos la tupla
    
    return {
        "id_cita": cita.id_cita,
        "nif_nie_usuario": cita.nif_nie_usuario,
        "cif_clinica": cita.cif_clinica,
        "especialista_cita": cita.especialista_cita,
        "fecha_cita": cita.fecha_cita,
        "razon_cita":cita.razon_cita,
        "nombre_usuario": usuario.nombre_usuario,
        "apellido1_usuario": usuario.apellido1_usuario,
        "apellido2_usuario": usuario.apellido2_usuario
    }




def update_cita(db: Session, cita_id: int, cita_data: CitaUpdate):
    cita = db.query(Citas).filter(Citas.id_cita == cita_id).first()
    if not cita:
        return None

    update_data = cita_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(cita, key, value)

    db.commit()
    db.refresh(cita)

    # Buscar los datos del usuario
    usuario = db.query(Usuario).filter(Usuario.nif_nie_usuario == cita.nif_nie_usuario).first()

    return {
        "id_cita": cita.id_cita,
        "nif_nie_usuario": cita.nif_nie_usuario,
        "cif_clinica": cita.cif_clinica,
        "especialista_cita": cita.especialista_cita,
        "fecha_cita": cita.fecha_cita,
        "razon_cita":cita.razon_cita,
        "nombre_usuario": usuario.nombre_usuario if usuario else None,
        "apellido1_usuario": usuario.apellido1_usuario if usuario else None,
        "apellido2_usuario": usuario.apellido2_usuario if usuario else None
    }

def delete_cita(db: Session, cita_id: int):
    cita = sacar_cita(db, cita_id)
    if not cita:
        return None
    db.delete(cita)
    db.commit()
    return cita