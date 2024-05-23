from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from infraestrucutre.models import Base
from flask_sqlalchemy import SQLAlchemy

DATABASE_URL = "postgresql://severinoapp:severinoapp@localhost:5433/severinoapp_db"


engine = create_engine(DATABASE_URL, echo=True)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SQLAlchemy()

def init_db():
    Base.metadata.create_all(bind=engine)
