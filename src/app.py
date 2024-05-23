from flask import Flask
from infraestrucutre.db_setup import init_db, db
from api.todas_as_rotas import rotas_controller

app = Flask(__name__)
app.register_blueprint(rotas_controller, url_prefix='/api')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://severinoapp:severinoapp@localhost:5433/severinoapp_db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados
init_db()
db.init_app(app)
app.run(debug=True)