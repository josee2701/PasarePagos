from sqlmodel import MetaData, Session, SQLModel, create_engine

# Configuración de la base de datos SQLite
sqlite_file_name = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Configura el motor de la base de datos
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

# Función para crear la base de datos y las tablas
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
# Función para obtener una sesión de la base de datos
def get_session():
    with Session(engine) as session:
        yield session