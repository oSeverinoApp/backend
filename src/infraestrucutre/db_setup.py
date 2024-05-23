from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from infraestrucutre.models import UserTable, Base


DATABASE_URL = "postgresql://severinoapp:severinoapp@localhost:5433/severinoapp_db"


engine = create_engine(DATABASE_URL, echo=True)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)