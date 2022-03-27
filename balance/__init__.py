from flask import Flask

#Ruta de la base de datos
app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")


from balance.routes import *