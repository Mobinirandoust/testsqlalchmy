from flask import (Flask,redirect,render_template,request,session)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"
app.secret_key = "Flask"

db = SQLAlchemy(app)

class UserTabel(db.Model):
    _id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    
with app.app_context():
    db.create_all()

@app.before_request
def createDB():
    db.create_all()

@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "POST":
        email = request.form["email"]
        user = UserTabel(
        email = email)
        db.session.add(user)
        db.session.commit()
        print(user)
        person = f'{user}'
        session['User'] = person
        return "missing success"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)