from flask_restful import Resource, reqparse
from models.TestModel import TestModel

class Test(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("prn", type=int, required=True, help="cannot blank")
    parser.add_argument("math", type=int, required=True, help="cannot blank")
    parser.add_argument("english", type=int, required=True, help="cannot blank")
    parser.add_argument("science", type=int, required=True, help="cannot blank")

    def get(self, prn):
        test=TestModel.find_by_prn(prn)
        if test:
            return test.json()
        return {"message":"not found"}
    
    def post(self, prn):
        data=Test.parser.parse_args()
        test=TestModel.find_by_prn(prn)
        if test:
            return {"message":"Already Exist"}
        test=TestModel(prn,data['math'],data['english'],data['science'])
        test.insert_in_db()
        return {"message":"Test Done"}

    def delete(self, prn):
        test=TestModel.find_by_prn(prn)
        if test:
            test.delete_from_db()
            return {"message":"test record deleted"},201
        return {"message":"record not found"},404