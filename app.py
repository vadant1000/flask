from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mp3.db'
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intro = db.Column(db.String(300), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text(300), nullable=False)
    da = db.Column(db.String(300), nullable=False)

class Article(db.Model):
    time = db.Column(db.Integer(10, 15), primary_key=True)
    id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)


@app.route('/')
def index():
    return render_template("id1.html")


@app.route('/h')
def hello_world3():  
    return 'Гена лох'


if __name__ == '__main__':
    app.run(debug=True)
