from sqlalchemy import create_engine
import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://myuser:password@localhost/fastapi_postgres"

engine = _sql.create_engine(DATABASE_URL)

#creamos la session
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
#aqui vamos a poder cargar nuestros modelos
Base = _declarative.declarative_base()

