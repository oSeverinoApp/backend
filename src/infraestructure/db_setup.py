from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy

DATABASE_URL = "postgresql://severinoapp:severinoapp@localhost:5433/severinoapp_db"


engine = create_engine(DATABASE_URL, echo=True)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SQLAlchemy()