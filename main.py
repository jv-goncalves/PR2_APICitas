from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import CitasOut, UsuarioCreate, UsuarioOut, CitasCreate, UsuarioUpdate, CitaUpdate
import crud
from models import Clinica

from database import SessionLocal, engine, Base
#TAREAS COMPLETAR - COMPLETADO
#CRUD USUARIOS ---> CRUD
#CRUD CITAS ------> CRUD


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()






def insertar_Clinica():
    db = SessionLocal()
    try:
        # Verifica si ya existe la clínica con CIF "GENERICA"
        clinica_existente = db.query(Clinica).filter(Clinica.cif == "GENERICA").first()
        if not clinica_existente:
            clinica_gen = Clinica(
                cif="GENERICA",
                nombre_clinica="Clínica Genérica",
                direccion_clinica="Dirección Genérica",
                capacidad_clinica=20
            )
            db.add(clinica_gen)
            db.commit()
            print("Clinica genérica insertada.")
        else:
            print("La clínica genérica ya existe.")
    finally:
        db.close()




Base.metadata.create_all(bind=engine)
insertar_Clinica()
app = FastAPI()










@app.post("/usuarios/", response_model=UsuarioOut)
def crear_usuario_endpoint(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return crud.crear_usuario(db, usuario)

@app.post("/citas/", response_model=CitasOut)
def crear_cita_endpoint(cita: CitasCreate, db: Session = Depends(get_db)):
    return crud.crear_cita(db, cita)

@app.get("/usuarios/{nif}", response_model=UsuarioOut)
def obtener_usuario(nif: str, db: Session = Depends(get_db)):
    usuario = crud.get_usuario(db, nif)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.get("/citas/{cita_id}", response_model= CitasOut)
def read_cita(cita_id: int, db: Session = Depends(get_db)):
    cita = crud.sacar_cita(db, cita_id)
    if not cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita




@app.delete("/usuarios/{nif}", response_model=UsuarioOut)
def eliminar_usuario(nif: str, db: Session = Depends(get_db)):
    usuario = crud.delete_usuario(db, nif)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.delete("/citas/{cita_id}", response_model=CitasOut)
def delete_cita(cita_id: int, db: Session = Depends(get_db)):
    cita_eliminada = crud.delete_cita(db, cita_id)
    if not cita_eliminada:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita_eliminada

@app.put("/usuarios/{nif}", response_model=UsuarioOut)
def actualizar_usuario(nif: str, usuario_update: UsuarioUpdate, db: Session = Depends(get_db)):
    usuario_actualizado = crud.update_usuario(db, nif, usuario_update)
    if not usuario_actualizado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario_actualizado




@app.put("/citas/{cita_id}", response_model=CitasOut)
def update_cita(cita_id: int, cita: CitaUpdate, db: Session = Depends(get_db)):
    cita_actualizada = crud.update_cita(db, cita_id, cita)
    if not cita_actualizada:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita_actualizada





# uvicorn main:app --reload