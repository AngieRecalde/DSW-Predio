from flask import Flask
from utils.db import db
from services.predio import predios
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION

appPredio=Flask(__name__)
appPredio.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION

#SQLAlchemy(app)

db.init_app(appPredio) 
appPredio.register_blueprint(predios)

with appPredio.app_context(): #se ejqcuta si la clase contacts no existiera
    db.create_all

if __name__=='__main__':
    appPredio.run(host='0.0.0.0',debug=True,port=5000)