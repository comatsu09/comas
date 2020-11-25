from flask import Flask
from flask import request
from flask import render_template
from janome.tokenizer import Tokenizer
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
t = Tokenizer()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

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

    return render_template('index.html', \
    title = '文節分けをします(post)', \
    message = '結果： {}'.format(res))

if __name__ == '__main__':
    app.run()
