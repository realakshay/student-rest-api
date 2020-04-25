from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, jwt_required
from resources.student import Student
from resources.test import Test
from resources.user import User
from security import authenticate,identity

app=Flask(__name__)
api=Api(app)

app.secret_key="secret"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
jwt=JWT(app,authenticate,identity)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Student,'/student/<int:prn>')
api.add_resource(Test,'/test/<int:prn>')
api.add_resource(User,'/user/<string:username>')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)