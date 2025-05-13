from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)
api = Api(app)


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'User({self.name}, {self.email})'
    

user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, required=True, help='Name cannot be blank')
user_args.add_argument('email', type=str, required=True, help='Email cannot be blank')

user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String
}

class Users(Resource):
    # GET method to retrieve all users
    @marshal_with(user_fields)
    def get(self):
        users = UserModel.query.all()
        return users
    
    # POST method to create a new user
    @marshal_with(user_fields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(name=args['name'], email=args['email'])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 201

class User(Resource):

    # GET method to retrieve a user by ID
    @marshal_with(user_fields)
    def get(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, f"User with {id} not found")
        return user
    
    # PUT method to update a user by ID
    @marshal_with(user_fields)
    def patch(self, id):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, f"User with {id} not found")
        user.name = args['name']
        user.email = args['email']
        db.session.commit()
        return user
    
    # DELETE method to delete a user by ID
    @marshal_with(user_fields)
    def delete(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, f"User with {id} not found")
        db.session.delete(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 204
        
api.add_resource(Users, '/api/users/')
api.add_resource(User, '/api/users/<int:id>')

@app.route('/')
def home():
    return '<h1>Welcome to the Flask API!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
