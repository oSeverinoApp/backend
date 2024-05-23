from flask import Flask
from infraestrucutre.db_setup import init_db
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://severinoapp:severinoapp@localhost:5433/severinoapp_db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados
init_db()

app.run(debug=True)
