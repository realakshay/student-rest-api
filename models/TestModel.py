from db import db

class TestModel(db.Model):
    __tablename__='tests'

    id=db.Column(db.Integer, primary_key=True)
    prn=db.Column(db.Integer, unique=True)
    math=db.Column(db.Integer)
    english=db.Column(db.Integer)
    science=db.Column(db.Integer)

    student=db.relationship('StudentModel', lazy='dynamic')

    def __init__(self, prn, math, english, science):
        self.prn=prn
        self.math=math
        self.english=english
        self.science=science
    
    def json(self):
        return {"prn":self.prn, "math":self.math, "english":self.english, "science":self.science, "student info":[s.json() for s in self.student.all()]}
    
    def insert_in_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.commit()
        
    @classmethod
    def find_by_prn(cls,prn):
        return cls.query.filter_by(prn=prn).first()