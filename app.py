from flask import Flask, render_template, redirect ,url_for, request
from flask_sqlalchemy import SQLAlchemy



# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)




class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    
with app.app_context():
    db.create_all()
    
    

@app.route('/add',methods=['GET','POST'])
def add():
    name = request.form.get('title')
    new_todo = Todo(title=name, complete = False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/')
def index():
    #show all todos
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template("base2.html",todo_list=todo_list)

if __name__ == "__main__":
    
    app.run(debug=1)