from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'e4f233ebf5042852ef08250828a3b1bc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from Meusite import routes

from Meusite import database, app

#with app.app_context():
  #database.drop_all()
  #database.create_all()



