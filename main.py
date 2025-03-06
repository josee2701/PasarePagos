from typing import Annotated

from fastapi import Depends, FastAPI
from sqlmodel import Session

from configs.db import create_db_and_tables, engine, get_session

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

# Crear tablas en el evento de inicio
@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    
# Dependencia para obtener una sesión de la base de datos
def get_db():
    with Session(engine) as session:
        yield session