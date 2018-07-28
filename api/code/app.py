from flask import Flask
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

users = []

class User(Resource):
    def get(self,username):
        for user in users:
            if user['username'] == username :
               return user 
        return{'username':None},404
    def post(self, username):
        user={'username':username,'age':23}
        users.append(user)
        return user,201

api.add_resource(User,'/user/<string:username>')
app.run(port=5000)