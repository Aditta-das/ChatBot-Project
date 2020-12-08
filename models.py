
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost:5432/bot"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Signin(db.Model):
    __tablename__ = 'signin'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String())
    password = db.Column(db.String())
    
    def __init__(self, email, password):
        self.email = email
        self.password = password
        
    def __repr__(self):
        return f"<email {self.email}>"