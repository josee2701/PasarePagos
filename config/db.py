from sqlmodel import MetaData, create_engine

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/bankingapp"
engine = create_engine(DATABASE_URL, echo=True)
meta = MetaData()

conn = engine.connect()

