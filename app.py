import pymysql
from flask import Flask, render_template
from models import Member
# 1번을 실행 해 주세요
from db_connect import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:12345678@localhost:3306/member"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db.init_app(app)


@app.route("/")
def home():
    # Elice, Dodo, Cheshire, Queen 데이터를 추가하세요.
    member = Member("Elice",15)
    member.id = 1
    db.session.add(member)
    member1 = Member("Dodo",16)
    member1.id = 2
    db.session.add(member1)
    member2 = Member("Cheshire",17)
    member2.id = 3
    db.session.add(member2)
    member3 = Member("Queen",18)
    member3.id = 4
    db.session.add(member3)  
    # 추가한 데이터를 DB에 저장하세요.
    db.session.commit()

    return "good"


@app.route("/check")
def check():
    data = db.session.query(Member).all()
        
    return render_template('member_list.html',member_list=data)

if __name__ == '__main__':
    app.run(debug=True)