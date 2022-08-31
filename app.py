"""API que nos permite gestionar wiw."""
import os
from flask import Flask
from flask_jwt_extended import JWTManager
from pony.flask import Pony

# Importo el Api  de la carpeta API
from api import api


# Configuramos el Secreto
strSecrtoJWT =  os.getenv("FLASK_JWT_SUPER_SECRTET" , "n/a")



app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = strSecrtoJWT  # Change this!
jwt = JWTManager(app)
Pony(app)
api.init_app(app)


if __name__ == "__main__":
    app.run(debug=True, threaded=False)
