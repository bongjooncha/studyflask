# SQLAlchemy 객체를 이용해 Member 모델을 생성하세요.
from db_connect import db

class Member(db.Model):
    __tablename__ = "member"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(20), nullable = False)
    age = db.Column(db.Integer, nullable = False)

    # Member 클래스의 생성자 수정
def __init__(self, name=None, age=None):
    self.name = name
    self.age = age
