from flask import  Flask, request
from flask_restful import Resource, Api,reqparse
from flask_jwt import JWT,jwt_required
from security import authenticate,identity
app = Flask(__name__)
app.secret_key = "maria"
api = Api(app)
jwt = JWT(app,authenticate,identity)

requests = []

class Request(Resource):
     parser = reqparse.RequestParser()
     parser.add_argument('message',
        type=str,
        required=True,
        help="This filed cannot be left blank"
        )
     @jwt_required()
     def get(self,requestid):
        requestid = self.User.username
        request = next(filter(lambda y:y['requestid']==requestid,requests),None) 
        return{'request':request},200 if request else 404

     def post(self, requestid):
         if next(filter(lambda y:y['']==username,users),None):
            return{'message':"user'{}'already exits.".format(username)},400
         data = Request.parser.parse_args()
         request={'requestid':requestid,'message':data['message']}
         requests.append(request)
         return request,201

     def delete(self, requestid):
         global requests
         requests = list(filter(lambda y:y['requestid']!=requestid,requests))
         return{'message':"request message deleted"}

     def put(self,requestid):
         requestid = User.username
         
         parser = Request.reqparse.RequestParser()
        
         data = parser.parse_args()
         request = next(filter(lambda y:y['requestid']==requestid,requests),None)
         if request is None:
            request={'requestid':requestid,'message':data['message']}
            requests.append(request)
            return request,201
         else:
            request.update(data)
         return request

class Requestlist(Resource):
    def get(self):
        return{'requests':requests}        
     
 
