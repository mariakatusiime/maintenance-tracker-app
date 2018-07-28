from flask import Flask,request
from flask_restful import Resource, Api,reqparse
from flask_jwt import JWT,jwt_required
from .security import authenticate,identity

app = Flask(__name__)
app.secret_key = "maria"

api = Api(app)
jwt = JWT(app,authenticate,identity)

users = []
requests = []

parser = reqparse.RequestParser()
parser.add_argument('fname',
          type=str,
          required=True,
          help="First Name cannot be left blank"
         )
parser.add_argument('sname',
          type=str,
          required=True,
          help="Second Name cannot be left blank"
        
        )
parser.add_argument('username',
          type=str,
          required=True,
          help="Username cannot be left blank"
          )
parser.add_argument('password',
          type=str,
          required=True,
          help="Password cannot be left blank"
         )
parser.add_argument('rpassword',
          type=str,
          required=True,
          help="rPassword cannot be left blank"
         )
parser.add_argument('email',
          type=str,
          required=True,
          help="Email cannot be left blank"
          )
parser.add_argument('dept',
          type=str,
          required=True,
          help="Department cannot be left blank"
          )
    
    

class User(Resource):
    
    
    
           
    @jwt_required()
    def get(self,username):
        user = next(filter(lambda y:y['username']==username,users),None) 
        return{'user':user},200 if user else 404

    
    def delete(self, username):
        global users
        users = list(filter(lambda y:y['username']!=username,users))
        return{'mesage':"user deleted"}

    def put(self,username):
        #parser = reqparse.RequestParser()
        
        args = parser.parse_args()
        user = next(filter(lambda y:y['username']==username,users),None)
        if user is None:
            user={'username':username,'password':args['password'],
            'First name':args['fname'],'Second name':args['sname']
            ,'Department':args['dept'],'email':args['email']
            }
            users.append(user)
            return user,201
        else:
            user["password"]=args["password"]
            user["rpassword"]=args["rpassword"]
            user["First name"]=args["fname"]
            user["Second name"]=args["sname"]
            user["Department"]=args["dept"]
            user["email"]=args["email"]
            if user["password"]==user["rpassword"]:
                return user,200
            return{'message':"passwords must be equal"}
        

class Userlist(Resource):

    
    def get(self):
        return{'users':users}   
    def post(self):
         
        #parser = Userlist.reqparse.RequestParser()
        args =parser.parse_args()
        #if next(filter(lambda y:y['username']==username,users),None):
         #   return{'message':"user'{}'already exits.".format(username)},400
    
        user={'username': args['username'] ,'password':args['password'],
        'First name':args['fname'],'Second name':args['sname'],
        'Email':args['email'],'Department':args['dept'],
        'rpassword':args['rpassword']}
        if args['password']==args['rpassword']:
            users.append(user)
            return user,201
            
        return{'message':"make sure the passwords are equal"}


api.add_resource(User,'/user/<string:username>')
api.add_resource(Userlist,'/users')

#if __name__==(__main__):
app.run(debug=True)
