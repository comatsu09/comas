from flask import Flask
from flask import request
from flask import render_template
from janome.tokenizer import Tokenizer
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)
t = Tokenizer()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base/test.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Text(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    text = db.Column(db.String,nullable=False)

@app.route('/',  methods=["GET"])
def get():
    return render_template('index.html', \
    title = '文節分けをします(get)', \
    message = '文章を入力して下さい。')

@app.route('/',  methods=["POST"])
def janome():
    text = request.form['text']
    tokens = t.tokenize(text, wakati=True)
    res = ""
    for token in tokens:
        res += token
        res += '*'

    num = number(res)

    text_res = Text(id = num,text = res)
    db.session.add(text_res)
    db.session.commit()

    return render_template('index.html', \
    title = '文節分けをします(post)', \
    message = '結果： {}'.format(res))

def number(bun):
    if not bun =='':
        cnt += 1
        return cnt

if __name__ == '__main__':
    app.run()
