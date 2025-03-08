# PR2_APICitas

**PR2_APICitas** es una API RESTful para la gestión de citas, desarrollada con FastAPI, SQLAlchemy y Pydantic. Este proyecto permite a los usuarios crear, consultar, actualizar y eliminar citas, gestionando además información de usuarios y clínicas. Además, se crean automáticamente las tablas en la base de datos y se inserta una clínica genérica si no existe.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Tecnologías](#tecnologías)
- [Instalación](#instalación)
- [Uso](#uso)

## Descripción

Este proyecto implementa una API para la gestión de citas (appointments). La API permite:
- Crear, consultar, actualizar y eliminar citas.
- Gestionar usuarios.
- Validar la integridad de los datos mediante Pydantic.
- Crear automáticamente las tablas en la base de datos y generar una clínica genérica.

## Características

- **CRUD completo** para citas y usuarios.
- **Validación de datos** usando Pydantic.
- **Generación automática de tablas** mediante SQLAlchemy.
- **Documentación automática** con Swagger UI y Redoc.
- **Inserción de clínica genérica** al iniciar la aplicación, en caso de que no exista.

## Tecnologías

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Uvicorn](https://www.uvicorn.org/)
- **SQLite** (o cualquier otra base de datos configurada)

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/jv-goncalves/PR2_APICitas.git
   cd PR2_APICitas
2. **Crea y activa un entorno virtual (opcional pero recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate      # En Linux/Mac
   venv\Scripts\activate         # En Windows
3. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt


## Uso

1. **Configura las variables de entorno (si es necesario):**  
   Si tu aplicación requiere configurar parámetros (por ejemplo, la conexión a la base de datos), crea un archivo `.env` basado en un ejemplo (por ejemplo, `.env.example`) e ingresa los valores correspondientes.

2. **Ejecuta la aplicación:**  
   Levanta el servidor con Uvicorn utilizando el modo de recarga para desarrollo:
   
   ```bash
   uvicorn main:app --reload
   
3. **Accede a la documentación de la API:**  
   La documentación se genera automáticamente y está disponible en:  
   - **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
   - **Redoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

4. **Probar los Endpoints:**  
   Utiliza herramientas como Swagger, Postman o cURL para interactuar con la API.  
   Algunos de los endpoints principales son:  
   - **Usuarios:**  
     - `POST /usuarios/` - Crear un usuario.  
     - `GET /usuarios/{nif}` - Consultar un usuario.  
     - `PUT /usuarios/{nif}` - Actualizar un usuario.  
     - `DELETE /usuarios/{nif}` - Eliminar un usuario.
   - **Citas:**  
     - `POST /citas/` - Crear una cita.  
     - `GET /citas/{cita_id}` - Consultar el detalle de una cita.  
     - `PUT /citas/{cita_id}` - Actualizar una cita.  
     - `DELETE /citas/{cita_id}` - Eliminar una cita.

5. **Verificar la Base de Datos:**  
   Al iniciar la aplicación, se crean automáticamente las tablas (si no existen) y se inserta una clínica genérica. Puedes revisar la base de datos (por ejemplo, abriendo el archivo SQLite si es el motor elegido) para confirmar que los datos se han insertado correctamente.
