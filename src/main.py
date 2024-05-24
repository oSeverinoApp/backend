# main.py
from flask import Flask
from interfaces.api.todas_as_rotas import rotas_controller
app = Flask(__name__)
app.register_blueprint(rotas_controller, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)