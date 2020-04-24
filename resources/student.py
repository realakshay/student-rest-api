from flask_restful import Resource, reqparse
from models.StudentModel import StudentModel

class Student(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True, help="cannot blank")
    parser.add_argument("prn", type=str, required=True, help="cannot blank")

    def get(self,prn):
        student=StudentModel.find_by_prn(prn)
        if student:
            return student.json()
        return {"message":"Student not found"},201
    
    def post(self,prn):
        data=Student.parser.parse_args()
        student=StudentModel.find_by_prn(prn)
        if student:
            return {"message":"Already Exist"},201
        student=StudentModel(data['name'],data['prn'])
        student.insert_in_db()
        return {"message":"Insert Success"},201