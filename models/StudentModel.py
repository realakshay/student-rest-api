from db import db

class StudentModel(db.Model):
    __tablename__='students'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    prn=db.Column(db.Integer, db.ForeignKey('tests.prn'), unique=True)
    test=db.relationship('TestModel')


    def __init__(self, name, prn):
        self.name=name
        self.prn=prn
    
    def json(self):
        return {"name":self.name, "prn":self.prn}

    def insert_in_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.commit()

    @classmethod
    def find_by_prn(cls,prn):
        return cls.query.filter_by(prn=prn).first()

    
    

