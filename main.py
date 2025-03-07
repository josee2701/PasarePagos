
from fastapi import FastAPI

from configs.db import create_db_and_tables
from models.model import *
from routes.user import router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(router, prefix="/user") # ⚡️ Incluir el router de usuario
