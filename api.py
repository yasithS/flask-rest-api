from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)


class User(db.model):
    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String(80), unique=True, nullable=False)
    email = db.column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'User({self.name}, {self.email})'
    

@app.route('/')
def home():
    return '<h1>Welcome to the Flask API!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
