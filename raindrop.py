from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = "postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@localhost:5432/flaskapp"

db = SQLAlchemy(app)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/users/<name>')
def user(name):
    return f'<h1> Hello, {name}!</h1>'
