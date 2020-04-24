from flask_restful import Resource, reqparse
from models.UserModel import UserModel

class User(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="cannot blank")
    parser.add_argument("password", type=str, required=True, help="cannot blank")

    def post(self,username):
        data=User.parser.parse_args()
        user=UserModel.find_by_username(data['username'])
        if user:
            return {"message":"username already exist"}
        user=UserModel(**data)
        user.insert_in_db()
        return {"message":"success"}
