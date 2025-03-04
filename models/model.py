from sqlmodel import Column, ForeignKey, Integer, String, Table

from config.db import engine, meta

users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("password", String),
    Column("email", String),
    Column("address", String),
    Column("phote", String),
)
meta.create_all(engine)